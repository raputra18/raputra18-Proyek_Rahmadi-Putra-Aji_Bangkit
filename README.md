Bike Rental Analysis Dashboard
Proyek ini bertujuan untuk menganalisis data peminjaman sepeda berdasarkan dua dataset yang mencakup data sewa sepeda per hari dan per jam. Dataset tersebut dianalisis dan divisualisasikan menggunakan Streamlit untuk membuat sebuah dashboard interaktif.

Struktur Proyek
scss
Salin kode
submission
├───dashboard
│    └───app.py                 (Berkas Streamlit untuk dashboard)
├───data
│    ├───day.csv                (Dataset CSV yang digunakan)
│    └───hour.csv               (Dataset CSV yang digunakan)
├───notebook.ipynb              (Berkas Jupyter Notebook atau Google Colab)
├───README.md                   (Berkas dokumentasi)
└───requirements.txt            (Berkas daftar library Python)
Deskripsi Dataset
day.csv: Dataset yang berisi data sewa sepeda per hari, dengan berbagai fitur seperti cuaca, musim, dan hari libur.
hour.csv: Dataset yang berisi data sewa sepeda per jam, memuat informasi lebih rinci tentang pola peminjaman sepeda pada setiap jam.
Tujuan Proyek
Menganalisis tren sewa sepeda berdasarkan berbagai faktor, seperti cuaca, musim, hari libur, dan lain-lain.
Membuat dashboard interaktif menggunakan Streamlit untuk memvisualisasikan data dan memungkinkan pengguna untuk eksplorasi lebih lanjut.
Menyediakan visualisasi yang mudah dipahami untuk mendukung keputusan terkait pengelolaan sepeda sewa.
Langkah-langkah Penggunaan
Instalasi

Untuk memulai, pastikan kamu sudah memiliki Python dan pip terinstal di sistem kamu. Kemudian, install semua dependensi dengan menjalankan perintah berikut:

bash
Salin kode
pip install -r requirements.txt
Menjalankan Aplikasi Dashboard

Setelah dependensi terinstal, kamu bisa menjalankan aplikasi Streamlit dengan menjalankan perintah berikut di terminal:

bash
Salin kode
streamlit run dashboard/app.py
Aplikasi Streamlit akan terbuka di browser kamu, menampilkan dashboard interaktif untuk eksplorasi data.

Eksplorasi dan Analisis

Gunakan Jupyter Notebook (notebook.ipynb) untuk eksplorasi awal data, analisis statistik, dan pembersihan data.
Visualisasi dan interaktivitas tersedia di aplikasi dashboard yang dibuat menggunakan Streamlit.
Penggunaan Data
Data yang digunakan dalam proyek ini terdiri dari dua file CSV:

day.csv: Dataset ini berisi data sewa sepeda berdasarkan per hari, mencakup variabel seperti cuaca, musim, dan jumlah sewa.
hour.csv: Dataset ini berisi data per jam, lebih rinci dan mencakup lebih banyak variabel.
Requirements
Proyek ini membutuhkan beberapa library Python untuk dapat berjalan dengan baik. Semua library yang diperlukan tercantum di berkas requirements.txt, antara lain:

pandas
numpy
streamlit
matplotlib
seaborn
Kontribusi
Jika kamu ingin berkontribusi pada proyek ini, silakan lakukan fork repositori ini dan buat pull request dengan perubahan yang diinginkan. Jangan ragu untuk membuka issue jika kamu menemui masalah atau memiliki pertanyaan.

Lisensi
Proyek ini menggunakan lisensi MIT License. Lihat berkas LICENSE untuk informasi lebih lanjut.

