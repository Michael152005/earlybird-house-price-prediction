# Early Bird Bengkel Koding — Prediksi Harga Rumah Depok

## Panduan
1. Buka `Early_Bird_Prediksi_Harga_Rumah_Colab.ipynb` di Google Colab.
2. Unggah `Raw-Final-Rumah.csv` ke Colab; jalankan **Runtime → Run all**.
3. Notebook menyimpan `earlybird_outputs/house_price_model.joblib`, grafik, tabel audit, dan metrik. Unduh ZIP output.
4. Untuk deployment Streamlit Cloud, unggah `app.py`, `requirements.txt` dan `house_price_model.joblib` ke root repositori GitHub. Di Streamlit Cloud pilih repo dan `app.py`.
5. Uji aplikasi dengan beberapa input yang wajar sebelum presentasi. Simpan URL GitHub, Colab dan Streamlit pada PDF pengumpulan.

## Catatan validitas
- Target adalah harga **penawaran** (bukan transaksi).
- Direct modeling = baseline dengan konversi teks/numerik minimum untuk kompatibilitas estimator.
- Kedua tahap menggunakan contoh dan pembagian data yang sama; test hanya diakses setelah pemilihan model via validation.
- Dedup tanpa Page bisa menyatukan properti yang terlihat sama tetapi sebenarnya berbeda; dicatat sebagai keterbatasan.
- Batas studi sementara Rp100 juta–Rp50 miliar dan 1–15 kamar tidur; perlu dibahas dalam presentasi.
- Link deployment bukan otomatis tercipta dari kode; harus deploy manual melalui GitHub dan Streamlit Cloud.
