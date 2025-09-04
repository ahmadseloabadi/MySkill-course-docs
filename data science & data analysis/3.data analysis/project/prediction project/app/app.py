import streamlit as st
from streamlit_option_menu import option_menu
from src import load_data,explore_data,avg_balance_product

with st.sidebar :
    selected = option_menu('sentimen analisis',['home','business understanding','data understanding','data preparation','modelling',"evaluation"])

if(selected == 'home') :

    st.title('Credit Card Prediction for FinanKu from Myskill')

    st.write('Ahmad Selo Abadi - Data Analyst and data scientist enthusiast')

    st.subheader('Latar Belakang')
    st.write("FinanKu adalah sebuah startup fintech imajiner yang memberikan fasilitas simpanan dan pinjaman kepada nasabahnya. Jasa yang mereka tawarkan di antaranya tabungan, deposito, pinjaman tanpa agunan, kartu kredit, dan pembiayaan kendaraan mobil dan motor.")
    st.write("Saat ini, FinanKu memiliki pelanggan sebanyak ~20.000 yang tersebar di 3 kota besar di Indonesia; Jakarta, Bandung, dan Surabaya. Angka ini cukup besar mengingat FinanKu baru berjalan selama 1,5 tahun, di mana diekspektasikan dalam 3 tahun ke depan pelanggan mereka akan berjumlah 300.000+.")
    st.write("Perkembangan yang cepat ini membuat para stakeholders di divisi kredit FinanKu semakin berhati-hati dalam menyalurkan kredit yang dimiliki agar tidak mengalami gagal bayar, khususnya dari lini Kartu Kredit yang memiliki fitur instant approval dalam 1 menit.")

    st.subheader('**PROBLEM STATEMENT**')
    st.write("Kekhawatiran adanya keterlambatan pembayaran kartu kredit pada FinanKu yang akan merugikan bisnis. Sehingga orang-orang yang memiliki potensi untuk mengalami keterlambatan bayar bisa diprediksi lebih cepat untuk menentukan strategi yang sesuai dalam menghadapi kondisi di masa mendatang.")
    
    st.subheader('**OBJECTIVE**')
    st.write("Membuat sebuah model yang dapat memprediksi setidaknya 60% dari pelanggan yang akan mengalami telat bayar kartu kredit [Accuracy & Recall di atas 60%]")


if(selected == 'business understanding') :

    st.subheader("kesimpulan")
    st.write("dari latar belakang kita dapat menarik beberapa kesimpulan yaitu:")
    st.write(f"**Permasalahan** ")
    st.write("Dalam satu tahun terakhir, lebih dari **20% nasabah kartu kredit gagal bayar**. Hal ini mengganggu operasional bisnis mengingat skala FinanKu masih tergolong kecil.\n")
    st.write("**Tujuan Bisnis**")
    st.write("Mengetahui lebih awal nasabah yang berpotensi gagal bayar.") 
    st.write("**Tujuan Analisis**")
    st.write("Membangun **model prediksi gagal bayar** untuk fasilitas **Kartu Kredit FinanKu**.")

    st.subheader("experiment")
    st.markdown('''
Periode Tinjauan:\n
1. Nasabah direview selama satu tahun terakhir\n
2. Nasabah direview selama 6 bulan terakhir\n

Penyesuaian Variabel:\n
1. Balance dilihat dari rata-rata selama horizon waktu & dilihat perubahan pada akhir tinjauan dan awal tinjauan\n
2. Melihat kepemilikan jumlah produk dari rata-rata, maksimum, dan minimum pada periode tinjauan\n
3. Status keaktifan nasabah dilihat dalam bentuk bulan''')
if(selected == 'data understanding') :
    path_1 = "data/FinanKu Data All.csv"
    path_2 = "data/FinanKu Data Validasi.csv"
    df_all,df_val=load_data(path_1,path_2)
    st.subheader('Dataset keseluruhan')
    st.write("tampilan dataset keseluruhan dari Finanku")
    st.dataframe(df_all,use_container_width=True)
    st.subheader('Dataset validasi')
    st.write("tampilan dataset validasi dari Finanku")
    st.dataframe(df_val,use_container_width=True)
    st.markdown('''Dari dataset yang dimiliki terdapat beberapa data yang tersedia:

**1. Customer ID:** Unique ID Customer\n
**2. Branch:** Lokasi Cabang Nasabah Terdaftar\n
**3. City:** Lokasi Kota Nasabah Terdaftar\n
**4. Age:** Umur Nasabah Pada Periode Observasi\n
**5. Avg. Annual Income/Month:** Rata-rata penghasilan nasabah dalam satu tahun\n
**6. Balance (Q1-Q4):** Saldo mengendap yang dimiliki nasabah di akhir kuartal\n
**7. Num of Products (Q1-Q4):** Jumlah kepemilikan produk nasabah di akhir kuartal\n
**8. HasCrCard (Q1-Q4):** Status kepemilikan produk kartu kredit nasabah di akhir kuartal\n
**9. Active Member (Q1-Q4):** Status keaktifan nasabah\n
**10. Unpaid Tagging:** Status nasabah gagal bayar''')
    
    st.subheader("data exploration")
    groub = st.multiselect( "Pilih pengelompokan yang akan digunakan:",
                ['City', 'Age'])
    paid_status = st.multiselect( "Pilih status bayar nasabah :",
                ['Unpaid', 'paid','all'])

    if st.button("tampilkan hasil"):
        explore_data(df_all,groub,paid_status)

    st.subheader("check profile nasabah")
    profile = st.multiselect( "Pilih profile yang akan dilihat:",
            ['Total Balance', 'Avg Balance','Avg Product'])
    if st.button("tampilkan profile"):
        avg_balance_product(df_all,profile)

if(selected == 'data preparation') :
    st.write('ini adalah bagian data preparation')

if(selected == 'modelling') :
    st.write('ini adalah bagian modelling')

if(selected == 'evaluation') :
    st.write('ini adalah bagian evaluation')