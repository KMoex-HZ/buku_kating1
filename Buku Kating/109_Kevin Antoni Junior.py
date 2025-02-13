
import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen MEDKRAF"
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nVqciR5qakWr6k3Rlu4F3h7Elj89IqUf",
            "https://drive.google.com/uc?export=view&id=1nWq9M81Uurl1non0b-AJm5dHZ1qkod3y",
            "https://drive.google.com/uc?export=view&id=1nYklRTEPIWhv3b8OGpQ1ihwcZmRGWsx-",
            "https://drive.google.com/uc?export=view&id=1nOGkizORQASlGLdVbWmRTHV1oAq1YrYT",
            "https://drive.google.com/uc?export=view&id=1MYIpqPg_hI78b22AVd2QOPAApalVhu0d",
            "https://drive.google.com/uc?export=view&id=1nMIhShY-81d6ExBiO3bIVyG2HS_FfIoC",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobbi": "Dengerin musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Kahim euy dingin",  
                "pesan":"sukses terus bang"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit Kemuning",
                "alamat": "Pawen 2 Sukarame",
                "hobbi": "Main Gitar",
                "sosmed": "@pndrinsni21",
                "kesan": "Abang ini asik",  
                "pesan":"semangat terus bang"# 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kotabaru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak ini asik dan lucu",  
                "pesan":"semangat dan sukses terus kak"# 3
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin  bang Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak ini lucu",  
                "pesan":"semangat terus kak"# 4
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak ini asik dan lucu",
                "pesan":"semangat terus kakak !!!"# 5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kotabaru",
                "hobbi": "Dengerin bang Pandra Gitaran",
                "sosmed": "@nadillaadr26",
                "kesan": "Kakak ini asik dan lucu",
                "pesan":"mangattt terus kakak !!!"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1legK8STqwYjUxtrQUdDFzwRzs-XVMv8W",
            "https://drive.google.com/uc?export=view&id=1l4LGZt1OCbILNr68x6IB8t3wegCNNJoG",
            "https://drive.google.com/uc?export=view&id=1ksEUlt09qsaYMuJ5dfb4coKn5SqhK1ML",
            "https://drive.google.com/uc?export=view&id=1lcr5vzdwBXamZkDYzOve-TUc4j0YL5mg",
            "https://drive.google.com/uc?export=view&id=1kubut7GlIBhpGJK88Q3xPf2z9XcTABgS",
            "https://drive.google.com/uc?export=view&id=1lc0Vgc5f2aShBiZI1dvpWCzrzYxs8wGv",
            "https://drive.google.com/uc?export=view&id=1kvcTU7dop1bdGbXCVovK28fH5Q7XVTUN",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1l-pMaA_vqOy3gmdvDqK2WhVoNnJHCO1n",
            "https://drive.google.com/uc?export=view&id=1lO2NAYJMt3FEpOz4y7VtSTxV6IWW8p_Q",
            "https://drive.google.com/uc?export=view&id=1l5AWICsH5TZNB_tiZfTV1ty4575hOVg_",
            "https://drive.google.com/uc?export=view&id=1kw_tpSRdQBu2it1s0aAGyBv9820gYZp_",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Bertanya sama GPT",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak ini asik sekali, friendly, public speakingnya juga bagus",  
                "pesan":"Semangat terus kuliahnya kak, semoga sehat selalu, dan jangan lupa untuk terus tersenyum" #7
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450124",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobbi": "Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!" #8
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!" #9
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": " @anisadini10",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!" #10
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal":"Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": " @ansftynn_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!" #11
            },
            {
                "nama": " Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!" #12
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-qur’an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!" #14
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!" #15
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!" #16
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450126",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": " Sukarame",
                "hobbi": "Melukis",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!" #17
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-qur’an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!" #18
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobbi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!" #19
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tip3Uz6k9eoIASSghkumceyHVa4F_2X4",# 1
            "https://drive.google.com/uc?export=view&id=1tg96eqzLzTFj3gu5mV85sKJlmLt_eiVM",# 2
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kos Putri Rahayu",
                "hobbi": "Bernyanyi",
                "sosmed": "@anissaluthfi_",
                "kesan": "Kakak ini cantik dan keren parahhh",  
                "pesan":"Semangat terus kak semoga sukses   "# 1
            },
            {
                "nama": "Ryan Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "keren bet calon senator hmsd",  
                "pesan":"sukses terus bang ,infokan catur"# 2
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
    
elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lpHSQT5ROLb_fWXnV95dVR_nA9-PhSwQ",#22
            "https://drive.google.com/uc?export=view&id=1AG_VaFeXbvaoj4UDN3OwQ_jEikZe1XUz",#23
            "https://drive.google.com/uc?export=view&id=1n-xu7L_rtAuhLPu_r3wg9EjLMm9gdQ6Y",#24
            "https://drive.google.com/uc?export=view&id=1lle-nJpGcGitBYG_87vpd4zHH4USZKDe",#25
            "https://drive.google.com/uc?export=view&id=1lrsrHCsjPyegYtzIoPlHa442rkpTYerB",#26
            "https://drive.google.com/uc?export=view&id=1m8SbHmabEaZBCNA-Qc7Mx1gDGZTB3TtQ",#27
            "https://drive.google.com/uc?export=view&id=1lmjwmLqZHal9fEmwESnE_3JpIlcNK3DM",#28
            "https://drive.google.com/uc?export=view&id=1lrEVC2hYOelJXZ9gaqIWqEdjicw8WD6F",#29
            "https://drive.google.com/uc?export=view&id=1mHL87i9UFJuEY-2ozY5Tuh_WoQmGM03a",#30
            "https://drive.google.com/uc?export=view&id=1mHLYkX4ls-RUMNFrhdxydxDSXphAWeTR",#31
            "https://drive.google.com/uc?export=view&id=1nEg7c06o3XjEG5vkTbFY8IgS9V9xRWZZ",#32
            "https://drive.google.com/uc?export=view&id=1mKU16IxoYcKGO08m9c5F0-WzVxA-RJ75",#34
            "https://drive.google.com/uc?export=view&id=1mTX2Xeztv9rEGblkOTjCLs14kxbrZAeK",#35
            "https://drive.google.com/uc?export=view&id=1m-MipOVbDe2U8rOrAALkiM2KU0z3rwLU",#37
            "https://drive.google.com/uc?export=view&id=1lx4RnaCZq19zBXMa_re6eaYbw_zS5mWS",#38
            "https://drive.google.com/uc?export=view&id=1mXovCGmq2jj8Tpz_6sebqvrw0jO3vig5",#39
            "https://drive.google.com/uc?export=view&id=1mLcTUQ8PjnLbDL94alrfKBOO-SZ4zjKf",#40
            "https://drive.google.com/uc?export=view&id=1mo4Z0OkHJ8WA2qXEvozbSEs-_QsQl5YJ",#41
            "https://drive.google.com/uc?export=view&id=1mYJ_n-CLG_tXHpH4edIXXfc8XaYHFouC",#42
            "https://drive.google.com/uc?export=view&id=1msTs-8v630UXR99F9tFD_9BbK3w57Mj5",#43
            "https://drive.google.com/uc?export=view&id=1meBWUKiZg5uc10PCBfn314vBpUE5kXVX",#44
        ]
        data_list = [
           {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Khobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Keren Punya pemikiran keren",  
                "pesan":"Semangat dan Semoga sukses bang" #22
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobbi": "Bernafas",
                "sosmed": "@celisabeth",
                "kesan": "Kakak ini asik",  
                "pesan":"jangan lupa tersenyum kakk semangat" #23
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Marahin orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak ini asik",  
                "pesan":"Semangat kak kuliahnya,btw jadi orang cantik cape gak si kak" #24
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi": "Main",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak ini asik,murah senyum, eksternal banget orangnya",  
                "pesan":"semangatt kak btw jenguk bang riski ayok" #25
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Metro",
                "hobbi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik",  
                "pesan":"Semangat terus kak, jangan lupa senyum" #26
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini murah senyum",  
                "pesan":"Semangat kuliahnya kakak" #27
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Jalan Pangeran Senopati Raya 18",
                "hobbi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang ini asik, baik, dan murah senyum,",  
                "pesan":"Semangat terus bang kuliahnya, semoga hasil yang didapat bagus" #28
            },
            {
                "nama":  "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobbi": "Ngukur jalan",
                "sosmed": "@dransyh_",
                "kesan": "Abang ini asik, baik, dan murah senyum",  
                "pesan":"Semangat terus bang, voli ayokk" #29
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak ini asik",  
                "pesan":"Semangat terus kuliahnya kak" #30
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "1214500148",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Pulau Damar Kobam",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Asik bet lu bang",  
                "pesan":"Semangat bang dee semoga cepat lulus dan mendapatkan pekerjaan sesuai dengan apa yang diinginkang bang lopyu" #31
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Kakak ini asik",  
                "pesan":"Semangat terus kak kuliahnya" #32
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobbi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "asik lu bang",  
                "pesan":"Semoga Sukses" #34
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Golf Asri",
                "hobbi": "Ngetik print hello dunia",
                "sosmed": "@kemasverii",
                "kesan": "Pj tugas sepuh coding , the best emang",  
                "pesan":"Semangat terus bang, semoga sukses" #35
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobbi": "Dengerin The Adams",
                "sosmed": "@presilliamg",
                "kesan": "Kakak ini asik",  
                "pesan":"Semangat terus kak kuliahnya" #37
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450122",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak ini asik",  
                "pesan":"Semangat terus kuliahnya kakak" #38
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok, Jawa Barat",
                "alamat": "Jalan Airan Raya",
                "hobbi": "Dengerin juicy luicy",
                "sosmed": "@sahid_maul19",
                "kesan": "Abang ini asik",  
                "pesan":"Semangat terus bang" #39
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Perum Korpri",
                "hobbi": "Minum kopi, belajar, bikin Deyvan senang",
                "sosmed": "@roselivness__",
                "kesan": "Jago bet basket",  
                "pesan":"Semangat terus kuliahnya kakk" #40
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Keren banget bang,support banget orangnya",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa cepat lulus dengan hasil yang memuaskan" #41
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobbi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Abang ini asik,support banget orangnnya",  
                "pesan":"Semangat terus bang kuliahnya semoga cepat lulus dengan nilai yang bagus" #42
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik",  
                "pesan":"Semangat terus kak" #43
            },
            {
                "nama":  "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abang ini asik dan ramah",  
                "pesan":"Semangat terus bang kuliahnya" #44
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()

elif menu == "Departemen MIKFES":
    def departemenmikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12ypJ6Gu4uxlbcg-DIrfxWxxeAX4mNtBd",#34
            "https://drive.google.com/uc?export=view&id=12oSane8dnxmnWYsgajWUnJoetLT_cpZ6",#35
            "https://drive.google.com/uc?export=view&id=12niNhdhHOZ9fVKdb3PC6gJc4a1J3adtS",#36
            "https://drive.google.com/uc?export=view&id=1lIabC2iu_V-mfWymntz2tz9SGnsvGm9A",#37
            "https://drive.google.com/uc?export=view&id=12iZp0RHZUk_oEM2nctinrM5rho1M-fDa",#37
            "https://drive.google.com/uc?export=view&id=13EsHpEaUkZLmX4fBCb9wKgWn603UfzlS",#38
            "https://drive.google.com/uc?export=view&id=131Po3Bs29ztcnUxwW0OH7UfypzPFE4z-",#39
            "https://drive.google.com/uc?export=view&id=12oq_Kprq09W_2i6s041VKkPb7lexSFRE",#40
            "https://drive.google.com/uc?export=view&id=131gb2JP68wCNS0_FO_YxYF7mXmjNppyO",#41
            "https://drive.google.com/uc?export=view&id=131qL6naWsLfdlZ52Ksy_NQE465HLDzxY",#42
            "https://drive.google.com/uc?export=view&id=13EsHpEaUkZLmX4fBCb9wKgWn603UfzlS",#43
            "https://drive.google.com/uc?export=view&id=12mouefRNePuxh0qGmi_ebMOdwCiYXlsL",#44
            "https://drive.google.com/uc?export=view&id=1lIabC2iu_V-mfWymntz2tz9SGnsvGm9A",#39
            "https://drive.google.com/uc?export=view&id=130Iue6ZyffJxJsY38oFMLI7ten1WUYfj",#34
            "https://drive.google.com/uc?export=view&id=12vE-GsDMvkGgkmtl8VCLoop7cirlrs_V",#35
            "https://drive.google.com/uc?export=view&id=12kB2N3SvJsuiLIHslQjMmDonFYnV2rf6",#36
            
            
           
            
           
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal": "Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "keren banget gaya abang ini",
                "pesan": "Sukses terus bang, semoga lancar sampai wisuda!"#1
            },
            {
                "nama": "Annisa Novantika",#2
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "keliatan fokus banget",
                "pesan": "Semoga semua yang kakak usahakan tercapai!"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abang ini asik",
                "pesan": "Semangat bang semoga sukses,tahun depan voli emas ini"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Kayaknya kakak ini rapi banget, selalu tampil oke.",
                "pesan": "Selalu semangat dan terus berkarya ya, Kak!"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi Sukarame",
                "hobbi": "Jadi admin ig mikfes.hmsd",
                "sosmed": "@mregiiii_",
                "kesan": "Kakak ini kayaknya punya energi positif, bikin suasana jadi hidup.",
                "pesan": "Jangan lupa bahagia dan nikmatin kuliah, Kak!"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Gg Yudhistira",
                "hobbi": "Baca Novel",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakak kayaknya bijak banget, cocok jadi role model.",
                "pesan": "Tetap humble dan jadi diri sendiri ya, Kak!"
            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal": "Bukittinggi",
                "alamat": "Korpri",
                "hobbi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "Kakak selalu kelihatan cool, kayaknya nggak gampang panik.",
                "pesan": "Jangan lupa tetap happy, Kak, walau sibuk."
            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Menonton Film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kakak kelihatan berwibawa, kayaknya bisa diandalkan.",
                "pesan": "Semangat terus ya, Kak, sampai jadi orang sukses!"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "",
                "sosmed": "@dindanababan_",
                "kesan": "Kakak sering terlihat enjoy aja, nggak pernah kelihatan stres.",
                "pesan": "Semoga kakak bisa capai semua mimpi-mimpinya!"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal": "Depok, Jawa Barat",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Liatin Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini kayaknya perhatian sama sekitarnya, ramah banget.",
                "pesan": "Semoga kakak selalu dikelilingi hal-hal positif!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal": "Batam, Kep.Riau",
                "alamat": "Gg. Nangka 3",
                "hobbi": "Resume Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak ini selalu terlihat serius, tapi kayaknya asik juga.",
                "pesan": "Semangat terus ya, Kak, jangan lupa senyum!"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Belwis",
                "hobbi": "Membaca",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini kelihatannya pintar banget, pasti banyak baca.",
                "pesan": "Semoga makin banyak inspirasi dari setiap buku, Kak!"
            },
            {
                "nama": "Abdurrahman Al-atsary",
                "nim": "121450128",
                "umur": "23",
                "asal": "Bandar Lampung",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Membaca",
                "sosmed": "@rahmn_abdr",
                "kesan": "Kakak ini terlihat bijak, kayaknya banyak pengalaman.",
                "pesan": "Semoga selalu sukses dalam setiap langkah, Kak!"
            },
            {
                "nama": "Aditya Rahman",
                "nim": "122450113",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Korpri",
                "hobbi": "Ngoding WISATA",
                "sosmed": "@rahm_adityaa",
                "kesan": "Kakak ini keliatan seru dan kreatif banget saat coding.",
                "pesan": "Semoga terus bikin proyek keren, Kak!"
            },
            {
                "nama": "Eggi Satria",
                "nim": "122450032",
                "umur": "20",
                "asal": "Sukabumi",
                "alamat": "Korpri",
                "hobbi": "Ngoding dan buat konten WISATA",
                "sosmed": "@egistr",
                "kesan": "Kakak ini kayaknya jago bikin konten, pasti banyak ide.",
                "pesan": "Semoga terus berkarya dan seru-seruan, Kak!"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Jl Kelengkeng Raya",
                "hobbi": "Nonton K-Drama",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakak ini keliatan fun dan pasti punya banyak rekomendasi K-Drama.",
                "pesan": "Semoga terus menikmati setiap episode yang ditonton, Kak!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmikfes()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Eksternal":
    def departemeneksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1H4TZJykTf0mBdW73facrR99CnMnliz9g",#34
            "https://drive.google.com/uc?export=view&id=1BDzfxwOSV3nBvflNLBNgnNVvHa1Ok0xT",#35
            "https://drive.google.com/uc?export=view&id=1XlOREggDvyd83MdQ1eYmhqlNdGtSu6q3",#36
            "https://drive.google.com/uc?export=view&id=15GadjXnt8hZ2Hg0aWXDMbIXVjIMtCJ_X",#37
            "https://drive.google.com/uc?export=view&id=1AwkwnrXemrVDUuj57SUajKbne7h71s6-",#38
            "https://drive.google.com/uc?export=view&id=1Ak1MWPgrU7hy-IWUeNjZCyOZttoJ8IC0",#39
            "https://drive.google.com/uc?export=view&id=1wPOFwEKgc1u9B6sPWlr3qQfKUUgMZyvB",#40
            "https://drive.google.com/uc?export=view&id=1nrwjMUS8PmE9laZnoVYAGse3d8EezpDO",#41
            "https://drive.google.com/uc?export=view&id=1o-916n1BnC0MuxIEGNtAU6hSOGLndbSQ",#42
            "https://drive.google.com/uc?export=view&id=1xYA0A0v-X8ua1ia5U3B4z1N5_y4LzPxa",#43
            "https://drive.google.com/uc?export=view&id=1tJ0oJEqmhEHznTbWaiGvl692tShNefOf",#44
            "https://drive.google.com/uc?export=view&id=1tPPPwmv4squFxeOU8VoYYl1WJXBQc5Wq",#34
            "https://drive.google.com/uc?export=view&id=14tpKvDsPfRO9j_ppgT4fG3-ULq5mIp1v",#37
            "https://drive.google.com/uc?export=view&id=1ufqY1h7xSHgEOCopCfZc20I8YJn0KlQ5",#38
            "https://drive.google.com/uc?export=view&id=1tedclqhwim4kWKgQS3Hb0OwKpHFhZ4C2",#39
            "https://drive.google.com/uc?export=view&id=12ZEKJMZuInJvm__PzLZ9RWL9GqDpOV0u",#40
            "https://drive.google.com/uc?export=view&id=1tXXQXLJu_-_5EHmKMtqfdmRiLbzAkj2z",#41
            
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jati Mulyo",
                "hobbi": "Bangun Pagi",
                "sosmed": "@yogyyy",
                "kesan": "Abang ini asik, tegas, baik, pemikirannya luas, dan bagus dalam publik speaking",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa lulus dengan hasil yang memuaskan" #66
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Way Kandis",
                "hobbi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakak ini asik, baik, dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya, semoga semua nilainya sesuai dengan yang kakak inginkan" #68
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobbi": "Main Game",
                "sosmed": "@",
                "kesan": "Abang ini asik, baik, dan seru diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya" #69
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaarsn",
                "kesan": "Kakak ini asik, baik, ramah, murah senyum, dan punya pemikiran yang luas",  
                "pesan":"Semangat terus kak kuliahnya, sukses selalu dimanapun kakak berada" #70
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450005",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Kirim BC-an",
                "sosmed": "@esteriars",
                "kesan": "Kakak ini asik, baik, ramah, dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya, sukses selalu ya kak" #71
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450",
                "umur": "20",
                "asal":"Saburai",
                "alamat": "Belwis",
                "hobbi": "Olahraga",
                "sosmed": "Tidur",
                "kesan": "Kakak ini asik, baik, bagus dalam komunikasi",  
                "pesan":"Semangat terus kakak kuliahnya dan bahagia selalu" #72
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jadi Humas",
                "sosmed": "@natee__15",
                "kesan": "Kakak ini asik, baik, ramah, dan murah senyum",  
                "pesan":"Semangat terus Kakak kuliahnya" #73
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Pulang malam",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus kakak kuliahnya semoga sehat selalu" #74
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobbi": "Berkebun",
                "sosmed": "@tobiassiagian",
                "kesan": "Abang ini keren",  
                "pesan":"Semangat terus bang kuliahnya, sukses selalu dimanapun abang berada tetep rangkul kitorang bang hehe" #75
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Menimba ilmu",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini asik, baik, murah senyum, seru untuk diajak diskusi, dan satu marga",  
                "pesan":"Semangat terus kak kuliahnya, bahagia terus kak" #76
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin Portofolio",
                "sosmed": "@rzkdrnnn ",
                "kesan": "Abang ini asik, baik, pemikirannya luas, dan bagus dalam komunikasi, serta seru untuk diajak diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga hasilnya sesuai dengan keinginan abang" #77
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara enim",
                "alamat": "Korpri",
                "hobbi": "Nyuci baju",
                "sosmed": "@-",
                "kesan": "Kakak ini asik, baik, pintar, dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya, ceria terus ya kak" #79
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abang ini asik, baik, friendly, dan murah senyum",  
                "pesan":"Semangat terus bang kuliahnya dan sukses terus bang" #81
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Masak",
                "sosmed": "@izzalutfia",
                "kesan": "Kakak ini asik, baik, friendly, pemikirannya luas, murah senyum dan bagus dalam komunikasi",  
                "pesan":"Semangat terus bang kuliahnya dan selalu bahagia ya kak" #82
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "daplok kelompok 1",
                "sosmed": "@alyaavanefi",
                "kesan": "cantik,baik,perhatian,merengutpun cantik perfect banget emang",  
                "pesan":"Semangat terus kak kuliahnya, bahagia terus dan sehat selalu semoga sukses kakk" #83
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Telat",
                "sosmed": "@rayths_",
                "kesan": "Abang ini baik, pintar, dan ramah",  
                "pesan":"Semangat terus bang kuliahnya dan sukses dimanapun abang berada" #84
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Membaca chat",
                "sosmed": "@triayunanni",
                "kesan": "Kakak ini asik , baik, ramah, dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya, bahagia selalu" #85
            },
         ]
        display_images_with_data(gambar_urls, data_list)
    departemeneksternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen Internal":
    def departemeninternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UEBj0AEAfa_aI6Hltaqk2Z6Xw4CsnMYa",#34
            "https://drive.google.com/uc?export=view&id=1JDuAWudKxSFVtYS9oSI3BSMhNhQeicJH",#35
            "https://drive.google.com/uc?export=view&id=1saa6N_y4izY39UAYrO0dCKHP9XOO8JO7",#36
            "https://drive.google.com/uc?export=view&id=1DJ06NkGeIi-ohpwJ-ZfwWXwIBj2h_s0n",#37
            "https://drive.google.com/uc?export=view&id=1TkEwcuHZJaMEiZ15AFia64i-WuufTzUt",#38
            "https://drive.google.com/uc?export=view&id=1haqAz7pndcxxLjmU6vlub1LoF9InalY2",#39
            "https://drive.google.com/uc?export=view&id=1JHHlzpdyfKvRDzSUooVktl9EpbuFsN-c",#40
            "https://drive.google.com/uc?export=view&id=1yOPcg-4_Zk7CNkM2b3yDQKjR8KFMgdG6",#41
            "https://drive.google.com/uc?export=view&id=1wwhVMvnu9Qnlnwvff37EH99tZLD2-yjs",#42
            "https://drive.google.com/uc?export=view&id=1YmgzoXmGUhKAQAuKBnwv9WbxWFAIHCqn",#44
            "https://drive.google.com/uc?export=view&id=1j8Tq8nVzfl4i9Zb4FuacWS1eTeY-I8d5",#34
            
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal": "Tangerang Selatan",
                "alamat": "Way Kandis (Kobam)",
                "hobbi": "Menunggu ayam jantan bertelur",
                "sosmed": "@dimzrky_",
                "kesan": "Keren banget orangnya",
                "pesan": "Semangatt terus bang semoga lulus dan dapet kerja sesuai kemauan,iklas kan bang 4ribu kemaren"
            },
            {
                "nama": "Chatrine Sinaga",
                "nim": "121450071",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan": "Kak Chatrine selalu punya rekomendasi novel yang menarik.",
                "pesan": "Semoga terus menemukan cerita yang inspiratif ya, Kak!"
            },
            {
                "nama": "M. Akbar Restika",
                "nim": "121450066",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Pasaruntung",
                "hobbi": "Mengoleksi Dino",
                "sosmed": "@akbar_restika",
                "kesan": "Kak Akbar punya pengetahuan yang luas tentang dinosaurus.",
                "pesan": "Tetap eksplorasi dan bagikan pengetahuanmu ya, Kak!"
            },
            {
                "nama": "Renita Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan": "Kak Renita selalu tenang dan sabar saat memancing.",
                "pesan": "Semoga dapat banyak tangkapan di setiap sesi memancing ya, Kak!"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan": "Kak Salwa selalu bisa memilih film yang menarik untuk ditonton.",
                "pesan": "Tetap berbagi rekomendasi film seru ya, Kak!"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobbi": "Menulis lagu",
                "sosmed": "@rendraepr",
                "kesan": "Kak Rendra memiliki bakat luar biasa dalam menulis lirik.",
                "pesan": "Semoga karya-karyamu selalu menginspirasi banyak orang, Kak!"
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "121450149",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi": "Nungguin ayam betina berkokok",
                "sosmed": "@yosiabanurea",
                "kesan": "Kak Yosia punya sabar yang luar biasa.",
                "pesan": "Semoga kesabaranmu selalu terbayar dengan hal-hal baik, Kak!"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi": "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "Kak Ari selalu antusias saat bermain futsal.",
                "pesan": "Terus semangat berolahraga dan jaga kesehatan ya, Kak!"
            },
            {
                "nama": "Josua Panggabean",
                "nim": "122450061",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi": "Ngejokes",
                "sosmed": "@josuapanggabean_",
                "kesan": "Kak Josua selalu bisa bikin orang tertawa.",
                "pesan": "Semoga terus membawa keceriaan bagi orang-orang di sekitar ya, Kak!"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@meirasty_",
                "kesan": "Kak Meira selalu tahu film-film terbaru yang menarik.",
                "pesan": "Tetap berbagi info film seru ya, Kak!"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi": "Berenang di Laut",
                "sosmed": "@rexander",
                "kesan": "Kak Rendi sangat suka tantangan saat berenang.",
                "pesan": "Semoga selalu menemukan tempat berenang yang seru, Kak!"
            }
        ]

        display_images_with_data(gambar_urls, data_list)
    departemeninternal()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen SSD":
    def departemenssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1QbEuO7Al1ULkcgWadN0W2mlBrsLTThvr",#34
            "https://drive.google.com/uc?export=view&id=1W2MfXINZjtrm3vMx4kmfNX8shMm19qES",#35
            "https://drive.google.com/uc?export=view&id=1sO7RSBQDJWMPq2ZhZm3HPv_8zNLum4kG",#36
            "https://drive.google.com/uc?export=view&id=1Cv8bFMRAWtzxST5hZ9Cd8GCfMeHSA2bo",#37
            "https://drive.google.com/uc?export=view&id=11mjY-bfu3Ha9O_cJKv-sdXaUam5k9qvJ",#38
            "https://drive.google.com/uc?export=view&id=13CLadFYChC983AhPreeD7at8BxupCp6x",#39
            "https://drive.google.com/uc?export=view&id=1gSbex1BFfUOqWpSuqomnqkH3VyNqjQVF",#40
            "https://drive.google.com/uc?export=view&id=1FxszIm4ydlD2Ad0oDh7QkcNJsuT4AyAY",#41
            "https://drive.google.com/uc?export=view&id=1PdcUKLrvP29gzU4jiIlUzGlgYDzGylV0",#41
            "https://drive.google.com/uc?export=view&id=1FWD4KyFcusq0K3_WDHAFVFZAt1bV4FDj",#42
           
        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumbangaol",
                "nim": "121450090",
                "umur": "21",
                "asal": "Panjibako",
                "alamat": "Jl. Bel",
                "hobbi": "Mencari Uang",
                "sosmed": "@andriangaol",
                "kesan": "Kak Andrian itu sangat pekerja keras dan penuh semangat!",
                "pesan": "Tetap semangat dalam mencari peluang ya, Kak!"
            },
            {
                "nama": "Adisty Syawaida Arianto",
                "nim": "121450136",
                "umur": "23",
                "asal": "Metro",
                "alamat": "Sukarame",
                "hobbi": "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan": "Kak Adisty selalu membawa keceriaan di setiap acara.",
                "pesan": "Jangan lupa share film rekomendasi ya, Kak!"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "21",
                "asal": "Simalungun",
                "alamat": "Airan",
                "hobbi": "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan": "Kak Nabila pintar dalam mengelola keuangan.",
                "pesan": "Ajarin kita semua tips keuangan ya, Kak!"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "122450085",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Airan",
                "hobbi": "Touring",
                "sosmed": "@dananghk_",
                "kesan": "best daplok",
                "pesan": "Semangat terus bang sehatt selalu"
            },
            {
                "nama": "Farel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Lapas",
                "hobbi": "Bebas",
                "sosmed": "@farel_julio",
                "kesan": "Kak Farel memiliki semangat yang positif!",
                "pesan": "Teruslah jadi inspirasi untuk kita semua, Kak!"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Bukittingi",
                "alamat": "Airan 1",
                "hobbi": "Badminton",
                "sosmed": "@ahmad.ris45",
                "kesan": "Kak Rizqi sangat antusias saat bermain badminton.",
                "pesan": "Semoga bisa main bareng di lapangan, Kak!"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122450040",
                "umur": "20",
                "asal": "Simalungun",
                "alamat": "Pemda",
                "hobbi": "Menulis",
                "sosmed": "@tesakanias",
                "kesan": "Kak Tessa selalu kreatif dalam berkarya.",
                "pesan": "Kirimkan karya-karyamu ya, Kak!"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "20",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan": "Kak Nabilah selalu tahu kapan waktu istirahat.",
                "pesan": "Jangan lupa menjaga kesehatan ya, Kak!"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan": "Kak Elia berbakat dalam musik, suaranya merdu!",
                "pesan": "Tunjukkan bakat musikmu di acara mendatang, ya Kak!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jl. Nangkal",
                "hobbi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Kak Dhafin sangat aktif dan energik.",
                "pesan": "Semoga bisa berolahraga bersama, Kak!"
            }
        ]

        display_images_with_data(gambar_urls, data_list)
    departemenssd()

# Tambahkan menu lainnya sesuai kebutuhan
elif menu == "Departemen MEDKRAF":
    def departemenmedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vB60Pr_yi0FK_DjVMCI4MxOkilQWypP9",#34
            "https://drive.google.com/uc?export=view&id=1ujKwrfuSbVLvlRp1Lc8iYQRJyv2rmeL2",#35
            "https://drive.google.com/uc?export=view&id=1u3mo2PgPuQHumkwl2uVYC-M6W1nlJUOT",#37
            "https://drive.google.com/uc?export=view&id=1tpbUqFCPVB5kZ5qLHwDVrlvFeo5hwypf",#38
            "https://drive.google.com/uc?export=view&id=1uioMZJV-DgPj9N7YOdsqk_6t8qatfUC7",#39
            "https://drive.google.com/uc?export=view&id=1uS3vxPw8xAvpENHPPTu6MRTrujV5MGOE",#40
            "https://drive.google.com/uc?export=view&id=1v1YEfIEmYdSXOmbJDjA5ngHygEGVBvcK",#41
            "https://drive.google.com/uc?export=view&id=1urztPqWi90pGkySz4cht8HKW6YCpshTl",#42
            "https://drive.google.com/uc?export=view&id=1uVOEZTYyCACeLzHap3d6XEt9I3VLy9QC",#43
            "https://drive.google.com/uc?export=view&id=1umvSmWqg9dEuWcwTKViBJdYEVdvIDez6",#44
            "https://drive.google.com/uc?export=view&id=1uK5qbmNa2NXmwJpocDlM355ZCWtwT9qk",#34
            "https://drive.google.com/uc?export=view&id=1u5Wz_YEtJIWDWhyErRYnkbz9WEyQ6OoQ",#35
            "https://drive.google.com/uc?export=view&id=1txS5Q9xd7qvxnqyimLVkEtUW40w69G1C",#36
            "https://drive.google.com/uc?export=view&id=1tyQjdgI7CHqHZ3WcApHwH8N3nvSDeVHB",#40
            "https://drive.google.com/uc?export=view&id=1uKJa0EmAd3GXJrz6p7EMuVFQLHRqi6dk",#37
            "https://drive.google.com/uc?export=view&id=1tzLfU8j-ieSFXY05S_dJHDpPvS7Uc99I",#38
            "https://drive.google.com/uc?export=view&id=1uTcKbwt0QFQCbpCVo6mk1voqmdQzNTl0",#39
            "https://drive.google.com/uc?export=view&id=1tqvKq_gCIWSO80eNRq0JIRYhsFDYIJgy",#39
            
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobbi": "Nonton",
                "sosmed": "@",
                "kesan": "Kak Wahyu kelihatan berwibawa dan visioner. Salut sama dedikasinya di departemen.",
                "pesan": "Semangat terus, Kak! Jangan lupa istirahat di tengah kesibukan, ya."
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Editing",
                "sosmed": "@elokfiola",
                "kesan": "Kak Elok keliatan cekatan dan teliti. Profesional banget kalau kerja!",
                "pesan": "Tetap semangat, Kak Elok! Jangan lupa sisihkan waktu buat diri sendiri juga!"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi": "Lagi Nyari",
                "sosmed": "@dino_kiper",
                "kesan": "Kak Kaisar keliatan santai tapi tetap bisa diandalkan, keren banget!",
                "pesan": "Tetap semangat ya, Kak! Jangan lupa sisihkan waktu buat refreshing juga."
            },
            {
                "nama": "Muhammad Arsal Ranjana Putra",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka 4",
                "hobbi": "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan": "Kak Arsal pasti kreatif banget, hasil desainnya keren-keren!",
                "pesan": "Lanjut terus, Kak Arsal! Semoga makin sukses dan makin kreatif ya."
            },
            {
                "nama": "Cintya Bella",
                "nim": "122450066",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi": "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan": "Kak Cintya kelihatan aktif dan energik. Inspirasi buat tetap produktif.",
                "pesan": "Semoga makin semangat, Kak! Jaga kesehatan juga ya."
            },
            {
                "nama": "Eka Fidiya Putri",
                "nim": "122450045",
                "umur": "20",
                "asal": "Natar, Lampung Selatan",
                "alamat": "Natar, Lampung Selatan",
                "hobbi": "Menyibukkan Diri",
                "sosmed": "@ekafdyaptri",
                "kesan": "Kak Eka terlihat rajin dan aktif, selalu semangat dalam segala hal.",
                "pesan": "Semangat terus, Kak! Jangan lupa nikmati waktu luang juga ya."
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatra Utara",
                "alamat": "Airan",
                "hobbi": "Menulis, Membaca, fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan": "Kak Najla kelihatan kreatif dan punya banyak ide keren.",
                "pesan": "Tetap semangat ya, Kak Najla! Keep inspiring with your creativity."
            },
            {
                "nama": "Patricia Leondra Diajeng Putri",
                "nim": "122450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton Film",
                "sosmed": "@patriciadiajeng",
                "kesan": "Kak Patricia kayaknya santai tapi produktif, selalu ada ide baru.",
                "pesan": "Semoga makin sukses ya, Kak Patricia! Keep up the good work!"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak Rahma kelihatan rajin dan tekun, pasti keren dalam coding!",
                "pesan": "Semoga selalu semangat, Kak! Terus berkembang dalam coding ya!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kak Try Yani kelihatan ceria dan suka bikin suasana jadi santai.",
                "pesan": "Tetap semangat ya, Kak! Terus berkarya dan jangan lupa have fun juga!"
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi": "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan": "Kak Dwi kelihatan tenang dan selalu detail kalau mengerjakan sesuatu.",
                "pesan": "Semangat terus, Kak Dwi! Teruslah menginspirasi dengan ketelitianmu."
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Kak Gym kelihatan santai dan suka berbagi hal-hal yang seru.",
                "pesan": "Jaga semangatmu, Kak! Terus jadilah inspirasi buat yang lain ya."
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi": "Nonton Drakor",
                "sosmed": "@nsywanaf",
                "kesan": "Kak Nasywa kelihatan aktif dan seru diajak ngobrol. Antusias banget!",
                "pesan": "Keep up the energy, Kak Nasywa! Teruslah jadi sumber keceriaan tim."
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi": "Baca Novel yang Bikin Nangis",
                "sosmed": "@prskslv",
                "kesan": "Kak Priska kayaknya penyayang dan empati banget sama sekitar.",
                "pesan": "Jangan lupa tersenyum, Kak Priska! Terus tebar energi positifmu ya."
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa, Labuhan Dalam",
                "hobbi": "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan": "Kak Abit kelihatan fokus dan passion-nya di coding patut diacungi jempol.",
                "pesan": "Tetap semangat, Kak Abit! Semoga makin jago coding dan terus berprestasi."
            },
            {
                "nama": "Akmal Faiz Abdillah",
                "nim": "122450114",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi": "Main HP",
                "sosmed": "_akmal.faiz",
                "kesan": "Kak Akmal santai tapi selalu siap kalau dibutuhkan. Orang yang bisa diandalkan!",
                "pesan": "Semangat terus, Kak! Terus produktif dan tetap keep cool ya."
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Dekat Jalan Tol (Wisma Hana Hani)",
                "hobbi": "Bengong/Membaca Buku",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Kak Hermawan kelihatan kalem dan penuh ide. Kayaknya orangnya thoughtful banget.",
                "pesan": "Terus semangat dan inspirasi, Kak! Jangan lupa buat nikmati waktu luang juga."
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi": "Mengerjakan Tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kak Khusnun rajin dan selalu disiplin, hebat banget!",
                "pesan": "Semangat terus ya, Kak Khusnun! Jangan lupa ambil waktu buat rileks juga."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenmedkraf()
        

# Tambahkan menu lainnya sesuai kebutuhan
