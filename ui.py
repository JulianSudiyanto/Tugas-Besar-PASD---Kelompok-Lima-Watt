import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import numpy as np
from model import preprocessing_rf, split_data, rf_model

train_url = 'https://raw.githubusercontent.com/JulianSudiyanto/Tugas-Besar-PASD---Kelompok-Lima-Watt/refs/heads/main/dataset/Clean_Data_Restaurant_Final.csv'
df = pd.read_csv(train_url)
       
df_visualisasi = df.copy(deep=True)
preprocessing_rf(df)

# Salin data asli
data = df.copy()
X_train, X_test, y_train, y_test = split_data(df)
best_model = rf_model(X_train, X_test, y_train)

########################################

st.set_page_config(page_title="KasirKita", layout="wide")
st.title("Analisis KasirKita")
st.write("Selamat datang di aplikasi KasirKita.")

df = pd.read_csv(r"D:\PASD\Tugas-Besar-PASD---Kelompok-Lima-Watt\data_gabungan.csv")
# Membaca CSV menjadi DataFrame

# Functional Programming untuk menghitung persentase churn
def churn_percentage(data, total):
    return data * total / 100

# Functional Programming untuk menghitung total pendapatan
def total_pendapatan(df):
    total = df['Order Total'].sum()
    return total

def laporan_penjualan(df):
    st.subheader("Laporan Penjualan")
    st.dataframe(df)
    # Total pendapatan
    if 'Order Total' in df.columns:
        total = total_pendapatan(df)
        st.metric("Total Pendapatan", f"Rp {total:,.0f}")
    else:
        st.warning("Kolom 'Order Total' tidak ditemukan.")
    
    st.subheader("Prediksi Churn")
    prediction = best_model.predict(df)
    df['Churn_Predicted'] = prediction
    total = len(prediction)
    churn_count = sum(prediction == 1)
    not_churn_count = sum(prediction == 0)
    churn_percent = churn_percentage(churn_count, total)
    not_churn_percent = churn_percentage(not_churn_count, total)
    # Tampilkan hasil
    st.write(f"Total data: {total}")
    st.write(f"Jumlah pelanggan **churn**: {churn_count} ({churn_percent:.1f}%)")
    st.write(f"Jumlah pelanggan **tidak churn**: {not_churn_count} ({not_churn_percent:.1f}%)")
    fig, ax = plt.subplots()
    ax.pie(
        [churn_percent, not_churn_percent],
        labels=["Churn", "Tidak Churn"],
        autopct='%1.1f%%',
        colors=["#f6c09f", "#f87f76"],
        startangle=90
    )
    ax.axis("equal")
    st.pyplot(fig)
    if churn_percent > not_churn_percent:
        st.write("Sayang sekali, restoran Anda memiliki sedikit pelanggan setia. Semangat dalam meningkatkan jumlah pelanggan setia. Terus perbaiki kualitas layanan kepada pelanggan Anda melalui pelayanan yang ramah dan kualitas menu yang baik.")
    else:
        st.write("Keren sekali, restoran Anda memiliki banyak pelanggan setia! Tingkatkan terus kualitas layanan kepada pelanggan Anda!")

def analisis_produk(df_visualisasi):
    st.subheader("Tren Penjualan per Produk")
    if 'Item' in df_visualisasi.columns and 'Quantity' in df_visualisasi.columns:
        produk_terlaris = df_visualisasi.groupby("Item")["Quantity"].sum().sort_values(ascending=False)
        st.bar_chart(produk_terlaris, color="#b8b8ff")
        st.subheader("Top 5 Produk Terjual")
        top_produk = produk_terlaris.head(5).sort_values(ascending=True)  # ascending biar produk paling laku di bawah
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(top_produk.index, top_produk.values, color="#82c0cc")
        ax.set_xlabel("Jumlah Terjual")
        ax.set_ylabel("Produk")
        ax.set_title("Top 5 Produk Terlaris")
        st.pyplot(fig)
    else:
        st.warning("Kolom 'item' atau 'quantity' tidak ditemukan.")

if df is not None:
    preprocessing_rf(df)
    if 'Churn' in df.columns:
        df = df.drop(columns=['Churn'])
    
    st.session_state['df'] = df
    st.success("File berhasil dibaca!")

    with st.sidebar:
        selected = option_menu(
            menu_title="Menu Utama",
            options=["Laporan Penjualan", "Analisis Tren Produk"],        
            icons=["clipboard-data", "clipboard-data"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical",
            styles={
                "container": {"padding": "0 !important", "background-color": "#f5f5f5"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "purple"},
            }
        )

    # Tampilan berdasarkan menu
    if selected == "Laporan Penjualan":
        laporan_penjualan(df)
    elif selected == "Analisis Tren Produk":
        analisis_produk(df_visualisasi)

else:
    st.info("Tidak ada file yang diterima.")

