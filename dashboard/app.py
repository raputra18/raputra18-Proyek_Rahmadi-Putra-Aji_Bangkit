import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Muat dataset
day_data = pd.read_csv(r"D:\PERKULIAHAN TRIK21\MBKM 2\Proyek_Rahmadi Putra Aji_Bike-sharing-dataset\dataset\day.csv")
hour_data = pd.read_csv(r"D:\PERKULIAHAN TRIK21\MBKM 2\Proyek_Rahmadi Putra Aji_Bike-sharing-dataset\dataset\hour.csv")

# Pembersihan Data (Hapus kolom 'instant' yang tidak diperlukan)
day_data.drop(columns=['instant'], inplace=True)
hour_data.drop(columns=['instant'], inplace=True)

# Judul dan penjelasan aplikasi
st.title("Dashboard Analisis Peminjaman Sepeda")
st.write("Aplikasi ini menampilkan visualisasi mengenai pengaruh faktor-faktor tertentu terhadap jumlah peminjaman sepeda.")

# Menu Pilihan
option = st.sidebar.selectbox(
    "Pilih Visualisasi",
    ("Pengaruh Cuaca", "Pengaruh Suhu", "Pengaruh Hari Kerja", "Pengaruh Musim", "Analisis Deret Waktu")
)

# Visualisasi Pengaruh Cuaca
if option == "Pengaruh Cuaca":
    st.subheader("Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda")
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='weathersit', y='cnt', data=day_data)
    plt.title('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')
    plt.xlabel('Cuaca')
    plt.ylabel('Jumlah Peminjaman')
    plt.xticks([0, 1, 2, 3], ['Cerah', 'Berawan', 'Hujan', 'Kabut'])
    st.pyplot(plt)

# Visualisasi Pengaruh Suhu
elif option == "Pengaruh Suhu":
    st.subheader("Pengaruh Suhu terhadap Jumlah Peminjaman Sepeda")
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=day_data)
    plt.title('Hubungan antara Suhu dan Jumlah Peminjaman Sepeda')
    plt.xlabel('Suhu (dinormalisasi)')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(plt)

# Visualisasi Pengaruh Hari Kerja
elif option == "Pengaruh Hari Kerja":
    st.subheader("Pengaruh Hari Kerja terhadap Jumlah Peminjaman Sepeda")
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='workingday', y='cnt', data=day_data)
    plt.title('Jumlah Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan')
    plt.xlabel('Hari Kerja (0 = Akhir Pekan, 1 = Hari Kerja)')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(plt)

# Visualisasi Pengaruh Musim
elif option == "Pengaruh Musim":
    st.subheader("Pengaruh Musim terhadap Jumlah Peminjaman Sepeda")
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='season', y='cnt', data=day_data)
    plt.title('Jumlah Peminjaman Sepeda Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(plt)

# Visualisasi Analisis Deret Waktu
elif option == "Analisis Deret Waktu":
    st.subheader("Jumlah Peminjaman Sepeda per Hari")
    
    day_data['dteday'] = pd.to_datetime(day_data['dteday'])
    day_data.set_index('dteday', inplace=True)
    daily_rentals = day_data['cnt'].resample('D').sum()
    
    plt.figure(figsize=(12, 6))
    daily_rentals.plot()
    plt.title('Jumlah Peminjaman Sepeda per Hari')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(plt)
