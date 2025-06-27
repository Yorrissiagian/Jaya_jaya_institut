# Proyek Akhir: Prediksi Dropout Mahasiswa Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan lembaga pendidikan tinggi yang berdiri sejak tahun 2000. Namun, beberapa tahun terakhir, kampus menghadapi tantangan tingginya angka mahasiswa yang *dropout*. Hal ini berdampak pada reputasi, efisiensi anggaran beasiswa, dan keberhasilan akademik mahasiswa.

Proyek ini bertujuan membantu manajemen dalam mendeteksi risiko dropout mahasiswa secara dini dengan pendekatan prediktif berbasis machine learning.

## Permasalahan Bisnis

1. Tingginya persentase mahasiswa yang tidak menyelesaikan studi.
2. Tidak ada sistem monitoring risiko dropout secara real-time.
3. Belum tersedia sistem prediktif untuk intervensi akademik.

## Cakupan Proyek

* Eksplorasi dan identifikasi faktor risiko dropout.
* Pembuatan dan evaluasi model prediktif.
* Pembuatan dashboard bisnis interaktif.
* Deployment aplikasi prediksi berbasis Streamlit.

## Sumber Data & Setup

* Dataset: https://github.com/dicodingacademy/dicoding\_dataset/blob/main/students\_performance/data.csv
* Informasi mencakup latar belakang demografis, akademik, dan finansial mahasiswa.
* Model akhir disimpan sebagai `model.pkl`, encoder sebagai `label_encoder.pkl`

## Data Understanding & EDA

* Mahasiswa *dropout* dan *graduate* memiliki proporsi yang signifikan.
* Performa akademik rendah dan keterlambatan bayar jadi indikator dropout kuat.
* Distribusi fitur numerik menunjukkan ketimpangan pada fitur keuangan & akademik.
* Korelasi tinggi antar fitur akademik semester 1 dan 2.

##  Modeling & Evaluation

### Algoritma

* Menggunakan **Random Forest Classifier** karena stabil, interpretatif, dan mampu menangani data campuran.

### Preprocessing

* Numerik: `StandardScaler`
* Kategorikal: `OneHotEncoder`
* Pipeline lengkap dibangun menggunakan `ColumnTransformer` → `Pipeline`

### Split Data

* 80% data latih, 20% data uji
* Label `Status` di-*encode* menjadi biner (Dropout = 1, Graduate = 0)

### Hasil Evaluasi Akhir

* **Akurasi:** 91.87%
* **Precision (Dropout):** 0.95
* **Recall (Dropout):** 0.84
* **F1-Score (Dropout):** 0.89
* **Confusion Matrix:**

  * TP: 238, FN: 46
  * FP: 13, TN: 429

### Fitur Terpenting:

1. `Tuition_fees_up_to_date`
2. `Scholarship_holder`
3. `Debtor`
4. `Age_at_enrollment`
5. `Admission_grade`

## Deployment

### Aplikasi Streamlit

* File utama: `app.py`
* Input: usia, gender, status nikah, beasiswa, tunggakan, nilai akademik, dst.
* Output: prediksi `GRADUATE` atau `DROPOUT`

### Jalankan Aplikasi

bash
streamlit run app.py

### Setup Environment

#### Terminal:

pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt

### Hosting:

* Hosted via Streamlit Cloud: [https://jayajayainstitut-k75cbyntzam6qn66aabwtv.streamlit.app/]
##  Business Dashboard (Metabase)

* Email: root@mail.com
* Password: h9VQfK?AeaZeTx

* Fitur Dashboard:

* Distribusi Status Mahasiswa
  Menampilkan proporsi antara mahasiswa yang Graduate dan Dropout, termasuk jumlah total mahasiswa.

* Dropout Berdasarkan Gender
  Menyajikan jumlah dropout berdasarkan gender, dengan label gender berupa angka (0, 1, 1.13).

* Perbandingan Nilai Masuk & Unit Lulus berdasarkan Status
  Menampilkan rata-rata nilai masuk (admission_grade), rata-rata unit saat lulus (rata_unit_lulus), dan rata-rata nilai unit lulus (rata_nilai_unit) berdasarkan status Dropout atau Graduate.

* Distribusi Usia Mahasiswa dan Jumlah Dropout
  Menampilkan jumlah dropout berdasarkan usia saat masuk kuliah. Terlihat tren usia muda mendominasi dropout.

* Faktor Ekonomi dan Persentase Dropout
  Menunjukkan kombinasi faktor ekonomi (utang, status beasiswa, keterlambatan bayar) terhadap jumlah dan persentase dropout.

##  Conclusion

Model prediktif berhasil mengidentifikasi mahasiswa berisiko dropout dengan akurasi tinggi.

**Karakteristik Mahasiswa Dropout:**

* Tidak membayar tepat waktu
* Tidak menerima beasiswa
* Memiliki utang
* Usia masuk > 30 tahun
* Performa akademik rendah di awal

Model ini siap digunakan kampus sebagai alat bantu pengambilan keputusan dan intervensi berbasis data.

##  Rekomendasi Tindakan

1. Sistem pengingat pembayaran.
2. Skema bantuan finansial khusus.
3. Monitoring mahasiswa usia >30 atau IP rendah.
4. Penggunaan sistem prediksi secara proaktif oleh akademik & keuangan.
