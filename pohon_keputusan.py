import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Baca data dari file Excel
file_excel = r'C:\Users\jokos\Desktop\latihan pyton\training -ai2024\data_kepuasan.xlsx'
data = pd.read_excel(file_excel)

# Cek nama kolom
print("Nama kolom:", data.columns.tolist())

# Menghapus spasi di sekitar nama kolom
data.columns = data.columns.str.strip()

# Tampilkan data untuk pemeriksaan
print(data.head())

# Konversi data kategori ke nilai numerik (encoding)
data['Pendidikan'] = data['Pendidikan'].map({'SMA': 0, 'Diploma': 1, 'Sarjana': 2})
data['Daerah'] = data['Daerah'].map({'Jawa': 0, 'Luar Jawa': 1})
data['Kepuasan'] = data['Kepuasan'].map({'Tidak': 0, 'Ya': 1})

# Pisahkan fitur (X) dan target (y)
X = data[['Pendidikan', 'Daerah']]  # Fitur
y = data['Kepuasan']      # Target

# Buat model pohon keputusan
model = DecisionTreeClassifier()

# Latih model dengan data
model.fit(X, y)

# Visualisasi pohon keputusan
plt.figure(figsize=(10, 6))
tree.plot_tree(model, feature_names=['Pendidikan', 'Daerah'], class_names=['Tidak', 'Ya'], filled=True)
plt.title("Pohon Keputusan untuk Prediksi Kepuasan")
plt.show()

# Prediksi apakah seseorang puas dengan pemerintah
data_baru = pd.DataFrame([[2, 1]], columns=['Pendidikan', 'Daerah'])  # Contoh input: Sarjana, Luar Jawa
prediksi = model.predict(data_baru)
print("Prediksi:", "Puas" if prediksi == 1 else "Tidak Puas")
