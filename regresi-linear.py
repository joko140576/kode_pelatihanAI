import numpy as np
import tkinter as tk
from tkinter import messagebox
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Data
X = np.array([50, 60, 70, 80, 90]).reshape(-1, 1)  # Luas rumah dalam m²
Y = np.array([300, 350, 400, 450, 500])            # Harga rumah dalam juta IDR

# Membuat model regresi linear
model = LinearRegression()
model.fit(X, Y)

# Fungsi untuk memprediksi harga rumah
def prediksi_harga():
    try:
        luas_input = float(entry_luas.get())  # Mengambil input dari pengguna
        if luas_input < 0:
            raise ValueError("Luas tidak boleh negatif.")
        harga = model.predict(np.array([[luas_input]]))  # Prediksi harga
        messagebox.showinfo("Prediksi Harga", f"Harga yang diprediksi untuk rumah seluas {luas_input} m² adalah {harga[0]:.2f} juta IDR.")
        tampilkan_grafik(luas_input, harga[0])  # Tampilkan grafik dengan garis bantu
    except ValueError as e:
        messagebox.showerror("Input Tidak Valid", str(e))

# Fungsi untuk menampilkan grafik dengan garis bantu
def tampilkan_grafik(luas_input, harga_prediksi):
    plt.figure(figsize=(10, 6))  # Membuat figure baru
    plt.scatter(X, Y, color='blue', label='Data Harga Rumah')  # Titik data asli
    plt.plot(X, model.predict(X), color='red', label='Garis Regresi')  # Garis regresi

    # Menambahkan garis bantu
    plt.axvline(x=luas_input, color='green', linestyle='--', label=f'Luas {luas_input} m²')
    plt.axhline(y=harga_prediksi, color='orange', linestyle='--', label=f'Harga {harga_prediksi:.2f} juta IDR')

    # Menambahkan titik prediksi
    plt.scatter([luas_input], [harga_prediksi], color='purple', zorder=5, label='Titik Prediksi')

    # Pengaturan label dan judul
    plt.title('Prediksi Harga Rumah dengan Garis Bantu')
    plt.xlabel('Luas Rumah (m²)')
    plt.ylabel('Harga Rumah (juta IDR)')
    plt.legend()
    plt.grid()  # Menambahkan grid
    plt.show()  # Menampilkan grafik dalam jendela terpisah

# Membuat jendela aplikasi
root = tk.Tk()
root.title("Prediksi Harga Rumah")

# Membuat frame untuk memusatkan konten
frame = tk.Frame(root)
frame.pack(pady=20)

# Label dan Entry untuk input luas rumah
label_luas = tk.Label(frame, text="Masukkan luas rumah (m²):", font=("Helvetica", 20))
label_luas.pack(pady=10)

entry_luas = tk.Entry(frame, font=("Helvetica", 20))
entry_luas.pack(pady=10)

# Tombol untuk memprediksi harga
button_prediksi = tk.Button(frame, text="Prediksi Harga", command=prediksi_harga, font=("Helvetica", 20))
button_prediksi.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
