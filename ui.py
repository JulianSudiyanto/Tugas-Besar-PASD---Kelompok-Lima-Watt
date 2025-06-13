import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np
# import pickle

# with open("rf_churn_model.pkl", "rb") as f:
#     model = pickle.load(f)
train_url = 'https://raw.githubusercontent.com/JulianSudiyanto/Tugas-Besar-PASD---Kelompok-Lima-Watt/refs/heads/main/dataset/Clean_Data_Restaurant_Final.csv'
df = pd.read_csv(train_url)
def rf():
    drop_cols = ['Unnamed: 0', 'Order ID', 'Order Date', 'Bulan', 'Last Visit Date', 'Customer ID']
    df.drop(columns=[col for col in drop_cols if col in df.columns], inplace=True)
    
    encoders = {}
    if 'Churn' in df.columns:
        le = LabelEncoder()
        df['Churn'] = le.fit_transform(df['Churn'])

    for col in ['Category', 'Payment Method', 'Item']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        

rf()
# Salin data asli
data = df.copy()

# Pisahkan fitur dan target
X = data.drop(columns='Churn')
y = data['Churn'].astype(int)

# Bagi data menjadi data train dan test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

def rf_model():
    from sklearn.model_selection import GridSearchCV
    rf = RandomForestClassifier(random_state=42, class_weight='balanced')

    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    grid_search = GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        cv=5,  # 5-fold cross validation
        n_jobs=-1,
        verbose=1,
        scoring='f1_weighted'
    )

    # Jalankan grid search
    grid_search.fit(X_train, y_train)

    # Evaluasi model terbaik di test set
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)

    return best_model

best_model = rf_model()

########################################

st.set_page_config(page_title="KasirKita", layout="wide")
st.title("Analisis KasirKita")
st.write("Selamat datang di aplikasi KasirKita.")

df = pd.read_csv(r"D:\PASD\Tugas-Besar-PASD---Kelompok-Lima-Watt\data_gabungan.csv")
# Membaca CSV menjadi DataFrame
if df is not None:
    rf()
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
        st.subheader("Laporan Penjualan")
        st.dataframe(df)

        # Total pendapatan
        if 'Order Total' in df.columns:
            total = df['Order Total'].sum()
            st.metric("Total Pendapatan", f"Rp {total:,.0f}")
        else:
            st.warning("Kolom 'Order Total' tidak ditemukan.")
        
        st.subheader("Prediksi Churn")
        prediction = best_model.predict(df)

        df['Churn_Predicted'] = prediction

        total = len(prediction)
        churn_count = sum(prediction == 1)
        not_churn_count = sum(prediction == 0)

        churn_percent = churn_count / total * 100
        not_churn_percent = not_churn_count / total * 100

        # Tampilkan hasil
        st.write(f"Total data: {total}")
        st.write(f"Jumlah pelanggan **churn**: {churn_count} ({churn_percent:.1f}%)")
        st.write(f"Jumlah pelanggan **tidak churn**: {not_churn_count} ({not_churn_percent:.1f}%)")
        fig, ax = plt.subplots()
        ax.pie(
            [churn_percent, not_churn_percent],
            labels=["Churn", "Tidak Churn"],
            autopct='%1.1f%%',
            colors=["red", "green"],
            startangle=90
        )
        ax.axis("equal")
        st.pyplot(fig)
        if churn_percent > not_churn_percent:
            st.write("Sayang sekali, restoran Anda memiliki sedikit pelanggan setia. Semangat dalam meningkatkan jumlah pelanggan setia. Terus perbaiki kualitas layanan kepada pelanggan Anda melalui pelayanan yang ramah dan kualitas menu yang baik.")
        else:
            st.write("Keren sekali, restoran Anda memiliki banyak pelanggan setia! Tingkatkan terus kualitas layanan kepada pelanggan Anda!")

    elif selected == "Analisis Tren Produk":
        st.subheader("Tren Penjualan per Produk")

        if 'Item' in df.columns and 'Quantity' in df.columns:
            produk_terlaris = df.groupby("Item")["Quantity"].sum().sort_values(ascending=False)
            st.bar_chart(produk_terlaris)

            st.subheader("Top 5 Produk Terjual")

            top_produk = produk_terlaris.head(5).sort_values(ascending=True)  # ascending biar produk paling laku di bawah

            fig, ax = plt.subplots(figsize=(8, 4))
            ax.barh(top_produk.index, top_produk.values, color="purple")
            ax.set_xlabel("Jumlah Terjual")
            ax.set_ylabel("Produk")
            ax.set_title("Top 5 Produk Terlaris")
            st.pyplot(fig)
        else:
            st.warning("Kolom 'item' atau 'quantity' tidak ditemukan.")

else:
    st.info("Tidak ada file yang diterima.")