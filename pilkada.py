import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Fungsi untuk menambah suara Kandidat A
def tambah_suara_a():
    global suara_a
    suara_a += 1
    label_suara_a.config(text=str(suara_a))
    update_total_suara()
    update_grafik()

# Fungsi untuk menambah suara Kandidat B
def tambah_suara_b():
    global suara_b
    suara_b += 1
    label_suara_b.config(text=str(suara_b))
    update_total_suara()
    update_grafik()

# Fungsi untuk mengupdate total suara
def update_total_suara():
    total_suara = suara_a + suara_b
    label_total_suara.config(text=f"Total Suara: {total_suara}")

# Fungsi untuk mengupdate grafik suara
def update_grafik():
    # Bersihkan grafik lama
    grafik_ax.clear()
    
    # Update grafik batang dengan nilai suara baru
    kandidat = ['Kandidat A', 'Kandidat B']
    suara = [suara_a, suara_b]
    grafik_ax.bar(kandidat, suara, color=['blue', 'green'])
    
    # Pengaturan tampilan grafik
    grafik_ax.set_title("Grafik Suara Kandidat")
    grafik_ax.set_ylabel("Jumlah Suara")
    grafik_ax.set_ylim(0, max(suara_a, suara_b, 10))  # Setting batas atas grafik dinamis

    # Redraw grafik
    canvas.draw()

# Inisialisasi jumlah suara
suara_a = 0
suara_b = 0

# Membuat jendela utama dengan ukuran 1200x600
window = tk.Tk()
window.title("Pemungutan Suara")
window.geometry("1200x700")

# Load gambar Kandidat A dan Kandidat B
try:
    # Memastikan gambar sesuai path Anda
    image_a = Image.open("kandidat_a.png")
    image_b = Image.open("kandidat_b.png")
    
    # Resize gambar agar lebih besar (200x200) dan menggunakan LANCZOS untuk kualitas tinggi
    image_a = image_a.resize((200, 200), Image.LANCZOS)
    image_b = image_b.resize((200, 200), Image.LANCZOS)
    
    # Convert gambar menjadi format yang dapat digunakan oleh tkinter
    photo_a = ImageTk.PhotoImage(image_a)
    photo_b = ImageTk.PhotoImage(image_b)
except FileNotFoundError:
    print("Gambar tidak ditemukan. Pastikan gambar 'kandidat_a.jpg' dan 'kandidat_b.jpg' berada di direktori yang sama.")

# Frame Utama untuk memusatkan semua elemen
main_frame = tk.Frame(window)
main_frame.pack(expand=True, pady=20)

# Frame Kandidat A
frame_a = tk.Frame(main_frame)
frame_a.grid(row=0, column=0, padx=60, pady=10)

# Menampilkan gambar dan tombol Kandidat A
label_image_a = tk.Label(frame_a, image=photo_a)
label_image_a.pack()
tombol_suara_a = tk.Button(frame_a, text="Tambah Suara A", font=("Arial", 16), command=tambah_suara_a, width=15, height=2)
tombol_suara_a.pack(pady=10)
label_suara_a = tk.Label(frame_a, text="0", font=("Arial", 24))
label_suara_a.pack()

# Frame Kandidat B
frame_b = tk.Frame(main_frame)
frame_b.grid(row=0, column=1, padx=60, pady=10)

# Menampilkan gambar dan tombol Kandidat B
label_image_b = tk.Label(frame_b, image=photo_b)
label_image_b.pack()
tombol_suara_b = tk.Button(frame_b, text="Tambah Suara B", font=("Arial", 16), command=tambah_suara_b, width=15, height=2)
tombol_suara_b.pack(pady=10)
label_suara_b = tk.Label(frame_b, text="0", font=("Arial", 24))
label_suara_b.pack()

# Label untuk total suara
label_total_suara = tk.Label(window, text="Total Suara: 0", font=("Arial", 24))
label_total_suara.pack(pady=20)

# Grafik suara kandidat menggunakan matplotlib
fig = Figure(figsize=(6, 4), dpi=100)
grafik_ax = fig.add_subplot(111)

# Canvas untuk menampilkan grafik di tkinter
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(pady=20)

# Menjalankan aplikasi
window.mainloop()
