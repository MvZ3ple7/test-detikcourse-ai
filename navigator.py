import streamlit as st
from streamlit_tags import st_tags
import openai

# flake8: noqa
# Set the OpenAI API key
openai.api_key = st.secrets["openai_key"]


# Define the function to call GPT-3.5-turbo API
def ask_gpt3_turbo(message, chat_log=None):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Anda adalah AI agent yang bertindak sebagai navigator handal yang bisa memberikan rute perjalanan untuk setiap kurir yang akan bertugas. Anda adalah navigator yang sangat ahli dalam perjalanan di Indonesia khususnya di daerah Jakarta dan Jawa Barat. Setiap kurir tidak akan mengunjungi tempat yang sama dalam satu kali perjalanan.",
            },
            {"role": "user", "content": message},
        ],
    )
    # Returning the response
    return response.choices[0].message.content


# Streamlit app
def main():
    st.title("Rute perjalanan driver")

    lokasi_keberangkatan = st.text_input(
        "Berangkat darimana? (Misalnya: Sunter, Grogol, PIK)"
    )
    # list_lokasi_keberangkatan = st.radio(
    #     "Lokasi keberangkatan?", ("Ruko ITC Cempaka Mas (Jakarta Pusat)")
    # )
    jumlah_driver = st.number_input(
        "Untuk berapa orang Driver yang akan bertugas hari ini?", min_value=1, max_value=5, step=1
    )
    list_lokasi = st.multiselect("Preferensi lokasi",
     [
       "Mall Taman Anggrek (Jakarta Pusat)"
     , "Mall Kelapa Gading (Jakarta Utara)"
     , "Mall Sunter (Jakarta Utara)"
     , "Mall Artha Gading (Jakarta Utara)"
     , "Mall Ciputra (Jakarta Barat)"
     , "Aeon Mall Bekasi (Bekasi)"
     , "Aeon Mall Serpong (Tangerang)"
     , "Botani Square Mall Bogor (Bogor)"
     , "AEON Mall Sentul City (Bogor)"
     , "Pondok Indah Mall (Jakarta Selatan)"
     , "Mall Ciputra Tangerang (Tangerang)"
     , "Summarecon Mall Serpong (Tangerang)"
     , "Living World Alam Sutera (Tangerang)"
     , "Summarecon Mall Bekasi (Bekasi)"
     , "Bekasi Trade Center Mall (Bekasi)"
     , "Summarecon Mall Karawang (Karawang)"
     , "Resinda Park Mall Karawang (Karawang)"
     , "Butik Synthesis Square (Jakarta Selatan)"
     ]
    )

    # ramah_anak = st.radio("Opsi makanan ramah anak", ("Tidak", "Ya"))
    # agama_budaya = st.text_input(
    #     "(optional) Apakah Anda memiliki batasan seperti halal atau vegetarian?"
    # )
    # kompleks = st.radio(
    #     "Anda mencari resep yang sederhana dan cepat atau yang lebih kompleks?",
    #     ("Sederhana dan cepat", "Kompleks"),
    # )
    # metode = st.multiselect("Preferensi metode memasak", ["goreng", "rebus", "bakar"])
    # jenis = st.radio(
    #     "Anda mencari resep untuk?", ("sarapan", "makan siang", "makan malam")
    # )
    # porsi = st.number_input(
    #     "Untuk berapa orang Anda akan memasak?", min_value=1, max_value=5, step=1
    # )

    if st.button("Kirim"):

        prompt = f"""
          Petakan saya rute untuk setiap kurir saya agar semua kurir dapat melakukan pekerjaan deliverynya cepat selesai dan seefisiensi mungkin untuk jarak dan waktu.
          Pembagian daerah disesuaikan dengan perjalanan masing-masing kurir dari satu tempat ke tempat tujuan selanjutnya.
          Setiap kurir akan kembali lagi ke lokasi keberangkatan sebagai tujuan akhir.
          Berikan juga total perkiraan setiap perjalanan.

          Lokasi keberangkatan: {lokasi_keberangkatan}
          Jumlah driver: {jumlah_driver}
          List lokasi: {list_lokasi}

          Format output:
          #[Kurir A]
          ##Rute-rute:
          1. [Lokasi keberangkatan] -> [Tempat Tujuan 1] [x jam]
          2. [Tempat Tujuan 1] -> [Tempat Tujuan 2] [x jam]
          3. ...
          ...
          x. [Tempat Tujuan terakhir] -> [Lokasi keberangkatan] [x jam]

          Total waktu perjalanan: x jam

          #[Kurir B]
          ##Rute-rute:
          1. [Lokasi keberangkatan] -> [Tempat Tujuan 1] [x jam]
          2. [Tempat Tujuan 1] -> [Tempat Tujuan 2] [x jam]
          3. ...
          ...
          x. [Tempat Tujuan X] -> [Lokasi keberangkatan] [x jam]

          Total waktu perjalanan: x jam

          dan seterusnya.


        """

        # user_input += additional_prompt
        ai_response = ask_gpt3_turbo(prompt)

        # print(ai_response)
        st.markdown(f"{ai_response}", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
