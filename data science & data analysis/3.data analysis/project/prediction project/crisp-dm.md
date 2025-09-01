# CRISP-DM: Model Prediksi Gagal Bayar Kartu Kredit

## Use Case

Membangun **model prediksi gagal bayar kartu kredit** untuk startup fintech imajiner bernama **FinanKu**.

---

## Latar Belakang

**FinanKu** adalah sebuah startup fintech yang menyediakan berbagai layanan simpanan dan pinjaman, di antaranya:

- Tabungan
- Deposito
- Pinjaman tanpa agunan
- Kartu kredit
- Pembiayaan kendaraan (mobil & motor)

Saat ini, FinanKu telah memiliki sekitar **20.000 pelanggan** yang tersebar di 3 kota besar di Indonesia: **Jakarta, Bandung, dan Surabaya**. Angka ini cukup besar mengingat FinanKu baru berjalan selama 1,5 tahun. Dalam 3 tahun ke depan, jumlah pelanggan diperkirakan akan mencapai **300.000+**.

Pertumbuhan cepat ini membuat **divisi kredit FinanKu** semakin berhati-hati dalam menyalurkan kredit, khususnya pada lini **Kartu Kredit** yang memiliki fitur _instant approval_ hanya dalam 1 menit.

---

## 1. Business Understanding

**Permasalahan**  
Dalam satu tahun terakhir, lebih dari **20% nasabah kartu kredit gagal bayar**. Hal ini mengganggu operasional bisnis mengingat skala FinanKu masih tergolong kecil.

**Tujuan Bisnis**  
Mengetahui lebih awal nasabah yang berpotensi gagal bayar.

**Tujuan Analisis**  
Membangun **model prediksi gagal bayar** untuk fasilitas **Kartu Kredit FinanKu**.

---

## 2. Data Understanding

Sebelum membuat model, perlu dipahami variabel-variabel yang tersedia dan dapat digunakan:

| Variabel            | Deskripsi                                                 |
| ------------------- | --------------------------------------------------------- |
| `branch`            | Lokasi cabang nasabah terdaftar                           |
| `city`              | Kota nasabah terdaftar                                    |
| `age`               | Umur nasabah pada tahun observasi                         |
| `avg_annual_income` | Rata-rata pendapatan tahunan nasabah                      |
| `balance`           | Rata-rata nominal tabungan nasabah di FinanKu             |
| `num_of_products`   | Jumlah produk FinanKu yang dimiliki nasabah               |
| `has_cr_card`       | Status kepemilikan kartu kredit (1 = memiliki, 0 = tidak) |
| `active_member`     | Status keaktifan nasabah berdasarkan transaksi            |

---

## 3. Data Preparation

Tahapan persiapan data meliputi:

- Pengecekan data duplikat dan data yang hilang.
- Menambah variabel/fitur baru (misalnya rata-rata, min, max).
- Transformasi data dengan melakukan **encoding** pada variabel kategorikal dan **standardisasi** pada variabel numerik.
- Mengulangi proses yang sama untuk dataset validasi.
- Mengecek korelasi antar-variabel.
- Membagi dataset menjadi **train** dan **test**.

---

## 4. Modeling

Proses pemodelan mencakup:

- Pemilihan algoritma (misalnya Logistic Regression, Random Forest, Gradient Boosting).
- Pencarian hyperparameter terbaik menggunakan **GridSearchCV**.
- Pembangunan model machine learning dengan parameter optimal.

---

## 5. Evaluation

Untuk mengukur performa model, digunakan beberapa metrik:

- **Recall** → Mengukur proporsi positif (gagal bayar) yang berhasil diidentifikasi.
- **Precision** → Mengukur seberapa banyak prediksi positif (gagal bayar) yang benar.
- **Accuracy** → Mengukur keseluruhan keberhasilan prediksi.

📌 Bobot penilaian: **50% akurasi** dan **50% recall**, agar model lebih seimbang dalam memprediksi kasus gagal bayar.

---

## 6. Deployment

Tahap deployment dilakukan dalam bentuk **Jupyter Notebook**, karena end-user dari sistem ini adalah **data scientist/engineer** yang membangun model tersebut.

---

✅ Dengan alur **CRISP-DM** ini, diharapkan FinanKu dapat meminimalisir risiko gagal bayar dan menjaga keberlangsungan bisnisnya.
