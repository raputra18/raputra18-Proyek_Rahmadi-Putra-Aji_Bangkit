import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the data
day_data = pd.read_csv(r"D:\PERKULIAHAN TRIK21\MBKM 2\Proyek_Rahmadi Putra Aji_Bike-sharing-dataset\dataset\day.csv")
hour_data = pd.read_csv(r"D:\PERKULIAHAN TRIK21\MBKM 2\Proyek_Rahmadi Putra Aji_Bike-sharing-dataset\dataset\hour.csv")

# Clean the data (drop unnecessary columns and fill missing values)
day_data.drop(columns=['instant'], inplace=True)

# Memeriksa jika ada kolom yang hilang sebelum pengisian
st.write("Jumlah Nilai yang Hilang pada Day Data sebelum pengisian:")
st.write(day_data.isnull().sum())

# Mengisi nilai yang hilang untuk data numerik saja
day_data.fillna(day_data.select_dtypes(include='number').mean(), inplace=True)
hour_data.fillna(hour_data.select_dtypes(include='number').mean(), inplace=True)

# Memeriksa nilai yang hilang setelah pengisian
st.write("Jumlah Nilai yang Hilang pada Day Data setelah pengisian:")
st.write(day_data.isnull().sum())

# Streamlit layout setup
st.title("Analisis Data Bike-Sharing")
st.write("Proyek Analisis Data: [Bike-sharing-dataset]")
st.write("Nama: Rahmadi Putra Aji")
st.write("Email: m008b4ky3624@bangkit.academy")
st.write("ID Dicoding: raputra")

# Descriptive Statistics
st.subheader("Statistik Deskriptif")
st.write("### Day Data")
st.write(day_data.describe())
st.write("### Hour Data")
st.write(hour_data.describe())

# Distribution of Daily Rentals
st.subheader("Distribusi Jumlah Peminjaman Sepeda Harian")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(day_data['cnt'], kde=True, ax=ax)
ax.set_title('Distribusi Jumlah Peminjaman Sepeda Harian')
ax.set_xlabel('Jumlah Peminjaman')
ax.set_ylabel('Frekuensi')
st.pyplot(fig)

# Question 1: Pengaruh Cuaca Terhadap Jumlah Peminjaman Sepeda
st.subheader("Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x=day_data['weathersit'], y=day_data['cnt'], ax=ax)
ax.set_title('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')
ax.set_xlabel('Cuaca')
ax.set_ylabel('Jumlah Peminjaman')
ax.set_xticklabels(['Clear', 'Cloudy', 'Rain', 'Fog'])
st.pyplot(fig)

# Question 2: Hubungan antara Suhu dan Jumlah Peminjaman Sepeda
st.subheader("Hubungan antara Suhu dan Jumlah Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x=day_data['temp'], y=day_data['cnt'], ax=ax)
ax.set_title('Hubungan antara Suhu dan Jumlah Peminjaman Sepeda')
ax.set_xlabel('Suhu (normalized)')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)

# Question 3: Jumlah Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan
st.subheader("Jumlah Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x=day_data['workingday'], y=day_data['cnt'], ax=ax)
ax.set_title('Jumlah Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan')
ax.set_xlabel('Hari Kerja (0 = Akhir Pekan, 1 = Hari Kerja)')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)

# Question 4: Jumlah Peminjaman Sepeda Berdasarkan Musim
st.subheader("Jumlah Peminjaman Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x=day_data['season'], y=day_data['cnt'], ax=ax)
ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)

# Time Series Analysis
st.subheader("Analisis Deret Waktu Peminjaman Sepeda per Hari")
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
day_data.set_index('dteday', inplace=True)
daily_rentals = day_data['cnt'].resample('D').sum()
fig, ax = plt.subplots(figsize=(12, 6))
daily_rentals.plot(ax=ax)
ax.set_title('Jumlah Peminjaman Sepeda per Hari')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)

# Clustering (Optional Analysis)
st.subheader("Clustering Berdasarkan Suhu dan Jumlah Peminjaman Sepeda")
from sklearn.cluster import KMeans

features = day_data[['temp', 'hum', 'windspeed', 'weathersit']]
kmeans = KMeans(n_clusters=3, random_state=42)
day_data['cluster'] = kmeans.fit_predict(features)

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x=day_data['temp'], y=day_data['cnt'], hue=day_data['cluster'], palette='viridis', ax=ax)
ax.set_title('Clustering berdasarkan Suhu dan Jumlah Peminjaman Sepeda')
ax.set_xlabel('Suhu (normalized)')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)

# Conclusion
st.subheader("Kesimpulan")
st.write(""" 
- **Pengaruh Cuaca**: Cuaca mempengaruhi jumlah peminjaman sepeda. Peminjaman lebih rendah saat cuaca buruk seperti hujan atau kabut.
- **Hubungan Suhu**: Suhu lebih tinggi menyebabkan lebih banyak peminjaman sepeda. Orang lebih cenderung menyewa sepeda ketika suhu lebih hangat.
- **Hari Kerja vs Akhir Pekan**: Peminjaman lebih tinggi pada hari kerja dibandingkan akhir pekan, menunjukkan bahwa sepeda lebih banyak digunakan untuk transportasi harian.
- **Pengaruh Musim**: Musim panas cenderung memiliki jumlah peminjaman yang lebih tinggi dibandingkan musim lainnya.
""")

# Footer
st.write("Terima kasih telah melihat analisis ini. Jika ada pertanyaan, silakan hubungi saya melalui email.")
