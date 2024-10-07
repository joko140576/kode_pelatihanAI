import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox

# Definisikan rentang suhu dan kecepatan kipas
temperature = np.arange(0, 41, 1)  # Suhu dari 0 hingga 40 derajat Celsius
fan_speed = np.arange(0, 101, 1)    # Kecepatan kipas dari 0 hingga 100%

# Definisikan fungsi keanggotaan untuk suhu
temp_low = fuzz.trapmf(temperature, [0, 0, 15, 20])   # Rendah
temp_medium = fuzz.trimf(temperature, [15, 25, 35])  # Sedang
temp_high = fuzz.trapmf(temperature, [30, 35, 40, 40]) # Tinggi

# Definisikan fungsi keanggotaan untuk kecepatan kipas
fan_slow = fuzz.trapmf(fan_speed, [0, 0, 30, 50])     # Lambat
fan_medium = fuzz.trimf(fan_speed, [30, 50, 70])      # Sedang
fan_fast = fuzz.trapmf(fan_speed, [60, 80, 100, 100]) # Cepat

def fuzzy_control(input_temperature):
    # Fuzzifikasi
    temp_low_level = fuzz.interp_membership(temperature, temp_low, input_temperature)
    temp_medium_level = fuzz.interp_membership(temperature, temp_medium, input_temperature)
    temp_high_level = fuzz.interp_membership(temperature, temp_high, input_temperature)

    # Aturan fuzzy
    rule1 = temp_low_level  # Jika suhu rendah maka kecepatan kipas lambat
    rule2 = temp_medium_level  # Jika suhu sedang maka kecepatan kipas sedang
    rule3 = temp_high_level  # Jika suhu tinggi maka kecepatan kipas cepat

    # Implication untuk kecepatan kipas
    fan_slow_activation = np.fmin(rule1, fan_slow)
    fan_medium_activation = np.fmin(rule2, fan_medium)
    fan_fast_activation = np.fmin(rule3, fan_fast)

    # Agregasi hasil
    aggregated = np.fmax(fan_slow_activation, np.fmax(fan_medium_activation, fan_fast_activation))

    # Defuzzifikasi
    fan_speed_output = fuzz.defuzz(fan_speed, aggregated, 'centroid')
    return fan_speed_output

def show_result():
    try:
        input_temperature = float(entry_temperature.get())
        
        # Validasi input suhu
        if input_temperature < 0 or input_temperature > 40:
            messagebox.showwarning("Input Tidak Valid", "Masukkan suhu antara 0 hingga 40°C.")
            return

        fan_speed_output = fuzzy_control(input_temperature)

        # Tampilkan hasil
        messagebox.showinfo("Hasil", f"Kecepatan kipas yang direkomendasikan: {fan_speed_output:.2f}%")

        # Gambar grafik
        draw_graph(input_temperature)
    except ValueError:
        messagebox.showwarning("Input Tidak Valid", "Masukkan suhu yang valid.")

def draw_graph(input_temperature):
    # Bersihkan grafik sebelumnya
    plt.clf()

    # Gambar fungsi keanggotaan suhu
    plt.subplot(2, 1, 1)
    plt.title("Fungsi Keanggotaan Suhu")
    plt.plot(temperature, temp_low, 'b', label='Rendah')
    plt.plot(temperature, temp_medium, 'g', label='Sedang')
    plt.plot(temperature, temp_high, 'r', label='Tinggi')
    plt.axvline(input_temperature, color='k', linestyle='--', label=f'Temperatur Input: {input_temperature}°C')
    plt.xlabel("Suhu (°C)")
    plt.ylabel("Derajat Keanggotaan")
    plt.legend()
    plt.grid()

    # Gambar fungsi keanggotaan kecepatan kipas
    plt.subplot(2, 1, 2)
    plt.title("Fungsi Keanggotaan Kecepatan Kipas")
    plt.plot(fan_speed, fan_slow, 'b', label='Lambat')
    plt.plot(fan_speed, fan_medium, 'g', label='Sedang')
    plt.plot(fan_speed, fan_fast, 'r', label='Cepat')
    plt.xlabel("Kecepatan Kipas (%)")
    plt.ylabel("Derajat Keanggotaan")
    plt.legend()
    plt.grid()

    # Tampilkan grafik
    plt.tight_layout()
    plt.show()  # Ganti canvas.draw() dengan plt.show() untuk memastikan grafik tampil

# Setup Tkinter window
root = tk.Tk()
root.title("Kontrol Suhu AC dengan Logika Fuzzy")

# Frame untuk input
frame_input = tk.Frame(root)
frame_input.pack(pady=20)

# Input untuk suhu ruangan
tk.Label(frame_input, text="Masukkan Suhu Ruangan (°C):").pack(side=tk.LEFT)
entry_temperature = tk.Entry(frame_input)
entry_temperature.pack(side=tk.LEFT)

# Tombol untuk mencari rute
button_find = tk.Button(root, text="Cari Kecepatan Kipas", command=show_result)
button_find.pack(pady=10)

# Jalankan aplikasi
root.mainloop()
