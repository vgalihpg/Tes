import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Selamat Datang di Hasil Analisis Data untuk Bike Sharing Dataset!')

# Load data
data = pd.read_csv("day.csv")
df = pd.DataFrame(data)

# Fungsi untuk menampilkan plot 1
def plot_graph1():
    fig1, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=df['workingday'], y=df['cnt'], ci=None, palette="coolwarm", ax=ax)
    ax.set_title("Perbandingan Penyewaan Sepeda di Hari Kerja vs Akhir Pekan")
    ax.set_xlabel("Jenis Hari")
    ax.set_ylabel("Jumlah Penyewaan Sepeda")
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Akhir Pekan", "Hari Kerja"])
    st.pyplot(fig1)

# Fungsi untuk menampilkan plot 2
def plot_graph2():
    fig2, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=df['weathersit'], y=df['cnt'], ci=None, palette="coolwarm", ax=ax)
    ax.set_title("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")
    ax.set_xlabel("Kondisi Cuaca (1: Cerah, 2: Berawan, 3: Hujan)")
    ax.set_ylabel("Total Penyewaan")
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["Cerah", "Berawan", "Hujan"])
    st.pyplot(fig2)

# Fungsi untuk menampilkan plot 3
weather_palette = {1: "#1f77b4", 2: "#ff7f0e", 3: "#2ca02c"}

def plot_graph3():
    fig3, ax = plt.subplots(figsize=(8, 5))
    scatter = sns.scatterplot(x=df['temp'], y=df['cnt'], hue=df['weathersit'],
                              palette=weather_palette, alpha=0.7, ax=ax)
    
    handles, labels = scatter.get_legend_handles_labels()
    ax.legend(handles=handles, labels=["Cerah", "Berawan", "Hujan/Snow"], title="Cuaca")
    
    ax.set_title("Hubungan antara Suhu, Cuaca, dan Penyewaan Sepeda")
    ax.set_xlabel("Suhu (ternormalisasi)")
    ax.set_ylabel("Jumlah Penyewaan Sepeda")
    
    st.pyplot(fig3)

# Inisialisasi session_state untuk menyimpan status tombol
if "active_plot" not in st.session_state:
    st.session_state["active_plot"] = None

# Sidebar untuk tombol pemilihan analisis
st.write("### Pilih Analisis:")
if st.button("Analisis #1"):
    st.session_state["active_plot"] = "plot1" if st.session_state["active_plot"] != "plot1" else None

if st.button("Analisis #2"):
    st.session_state["active_plot"] = "plot2" if st.session_state["active_plot"] != "plot2" else None

if st.button("Kesimpulan"):
    st.session_state["active_plot"] = "plot3" if st.session_state["active_plot"] != "plot3" else None

# Menampilkan plot berdasarkan tombol yang ditekan
if st.session_state["active_plot"] == "plot1":
    st.header("Berikut adalah Hasil Analisis #1:")
    st.subheader("Apakah Hari Kerja dan Hari Libur Memiliki Pengaruh Terhadap Jumlah Penyewaan Sepeda?")
    plot_graph1()
    st.write("Jumlah penyewaan sepeda di hari kerja sedikit lebih banyak dibandingkan dengan akhir pekan. "
             "Perbedaannya tidak terlalu signifikan untuk jumlah penyewaan sepeda pada akhir pekan dan hari biasa "
             "mungkin disebabkan karena pada hari biasa orang menggunakan sepeda untuk alat transportasi sehari-hari, "
             "sedangkan untuk akhir pekan orang juga akan menyewa sepeda untuk berolahraga atau pergi rekreasi.")

elif st.session_state["active_plot"] == "plot2":
    st.header("Berikut adalah Hasil Analisis #2:")
    st.subheader("Apakah Kondisi Cuaca Memiliki Pengaruh Terhadap Jumlah Penyewaan Sepeda?")
    plot_graph2()
    st.write("Jumlah penyewaan sepeda sangat dipengaruhi oleh kondisi cuaca, di mana saat kondisi cuaca cerah jumlah penyewaan sepeda "
             "berada pada puncaknya, dan mengalami penurunan drastis ketika cuaca hujan.")
    plot_graph3()
    st.write("Suhu sangat berpengaruh terhadap jumlah penyewaan sepeda karena semakin tinggi suhu berarti semakin cerah cuacanya "
             "sehingga semakin banyak juga jumlah orang yang akan melakukan sewa sepeda.")

elif st.session_state["active_plot"] == "plot3":
    st.header("Kesimpulan Analisis")

    # Tambahkan dropdown
    selected_analysis = st.selectbox(
        "Pilih Kesimpulan yang Ingin Ditampilkan:",
        ("Pilih Kesimpulan", "Kesimpulan Pertama", "Kesimpulan Kedua")
    )

    # Tampilkan teks sesuai dengan pilihan
    if selected_analysis == "Kesimpulan Pertama":
        st.write("Jumlah penyewaan sepeda pada hari biasa sedikit lebih banyak dibandingkan jumlah penyewaan sepeda yang dilakukan pada akhir pekan. Hasil selisih yang sedikit ini mungkin disebabkan oleh karena pada hari biasa sebagian besar orang memerlukan sepeda sebagai alat transportasi, dan pada akhir pekan hanya beberapa orang tertentu saja yang ingin menyewa sepeda untuk pergi rekreasi atau berolahraga.")
    elif selected_analysis == "Kesimpulan Kedua":
        st.write("Jumlah penyewaan sepeda dipengaruhi oleh cuaca dan suhu. Karena suhu yang semakin tinggi menandakan cuaca yang semakin cerah membuat jumlah penyewaan terhadap sepeda semakin tinggi. Cuaca yang cerah mendorong orang untuk beraktivitas lebih baik di ruangan terbuka sehingga sepeda dibutuhkan sebagai salah satu alat transportasi paling efisien, sedangkan pada musim hujan akan merepotkan orang untuk beraktivitas di ruangan terbuka.")