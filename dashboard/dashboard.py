import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import os

data_path = r"data"

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

hour_df = pd.read_csv(os.path.join(data_dir, 'hour.csv'))
day_df = pd.read_csv(os.path.join(data_dir, 'day.csv'))

# --- Streamlit dashboard ---
st.title("Analisis Data Bike Sharing")
st.caption('Berikut ini hasil analisis dari data Bike Sharing')
st.caption('Pertanyaan 1:')
st.caption('Apakah cuaca mempengaruhi penggunaan sepeda sharing lebih besar pada pengguna casual atau terdaftar?')
st.subheader("Matriks Korelasi")
correlation = hour_df[['cnt', 'casual', 'registered', 'temp', 'atemp', 'hum', 'windspeed', 'weathersit']].corr()
st.dataframe(correlation)

st.subheader("Korelasi Temperatur dan Jumlah Penyewaan")

plt.figure(figsize=(8, 6))
plt.scatter(hour_df['temp'], hour_df['cnt'])
plt.xlabel('Temperatur')
plt.ylabel('Jumlah Penyewaan')
plt.title('Korelasi Temperatur dan Jumlah Penyewaan')
st.pyplot(plt)

st.subheader("Distribusi Jumlah Penyewaan Sepeda")

plt.figure(figsize=(8, 6))
plt.hist(hour_df['cnt'], bins=20)
plt.xlabel('Jumlah Penyewaan')
plt.ylabel('Frekuensi')
plt.title('Distribusi Jumlah Penyewaan Sepeda')
st.pyplot(plt)

st.caption('Hasil akhir dari analisis:')
st.subheader("Perbandingan Distribusi Penyewaan antara Casual dan Registered")

plt.figure(figsize=(8, 6))
plt.boxplot([hour_df[hour_df['casual'] > 0]['cnt'], hour_df[hour_df['registered'] > 0]['cnt']],
            labels=['Casual', 'Registered'], showmeans=True)
plt.ylabel('Jumlah Penyewaan')
plt.title('Perbandingan Distribusi Penyewaan antara Casual dan Registered')
st.pyplot(plt)

# --- Daily Analysis ---
st.caption('Pertanyaan 2:')
st.caption('Bagaimana pola penggunaan sepeda sharing di Washington DC berubah setiap hari selama seminggu?')
st.subheader("Analisis Harian")

if 'cnt' in day_df.columns:
    group_day = day_df.groupby('weekday')[['cnt', 'casual', 'registered']].mean()
    st.dataframe(group_day)

    st.subheader("Tren Penggunaan Sepeda Per Hari dalam Seminggu")
    plt.figure(figsize=(8, 6))
    plt.plot(day_df.groupby('weekday')['cnt'].mean())
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Jumlah Penyewaan')
    plt.title('Tren Penggunaan Sepeda Per Hari dalam Seminggu')
    st.pyplot(plt)
    
    st.subheader("Rata-Rata Penggunaan Sepeda Per Hari")
    plt.figure(figsize=(8, 6))
    plt.bar(group_day.index, group_day['cnt'])
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Jumlah Penyewaan')
    plt.title('Rata-Rata Penggunaan Sepeda Per Hari')
    st.pyplot(plt)
