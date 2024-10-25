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
            "Departemen MEDKRAF",

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
            "https://drive.google.com/uc?export=view&id=1MUoy48hnTDmw862b__HBv84KzvsB1P2E",
            "https://drive.google.com/uc?export=view&id=1UE8koIJO0QFZiw1syIXW8x0VIgR6AAS5",
            "https://drive.google.com/uc?export=view&id=1j93CZAzBcWfl1BOvknA_QznVyDe9437X",
            "https://drive.google.com/uc?export=view&id=1aq38Xj9nTdSZL8XgBGOLAN3oREyxtdhK",
            "https://drive.google.com/uc?export=view&id=1uVuhFJ8APh-2bpfdEXbSty7_KQPq5tya",
            "https://drive.google.com/uc?export=view&id=1IjcK89ecGINA--F6IDLnHrOf5mi-KH-p",
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
                "kesan": "Abang ini punya pengetahuan yang luas",  
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
                "pesan":"semangat terus bang"# 1
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
                "pesan":"semangat terus kak"# 1
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
                "pesan":"semangat terus kak"
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
                "pesan":"semangat terus kakak !!!"
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
                "pesan":"semangat terus kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=138unPpPfnex4eHeQS5OFRzE00rI_BLEz",
            "https://drive.google.com/uc?export=view&id=1i-G72_aSknAR5YCzswphhMcuPeRIzudv",
            "https://drive.google.com/uc?export=view&id=18FvIi-_-goWdCgZL3WBwFErgJDCmHc1Q",
            "https://drive.google.com/uc?export=view&id=1CBWB3k63m74FfMVXluOhzlCCsXZrITlU",
            "https://drive.google.com/uc?export=view&id=1N5fBKp4w0pPnpkpZfb2Ia_Qj6GlehRhj",
            "https://drive.google.com/uc?export=view&id=1-x4vdxyRLFjxE7VXfoGjvhnEq8N1Jzt_",
            "https://drive.google.com/uc?export=view&id=1kE-Vf2bXzTWuegDkJGRJqwKrM4MJrjj4",
            "https://drive.google.com/uc?export=view&id=1dvjCPjDmPRq4wHJgZHReNEDT8tMRomhH",
            "https://drive.google.com/uc?export=view&id=1uO0agW2O9BVa7qyP-PuqKVxpVc9UyMRa",
            "https://drive.google.com/uc?export=view&id=1cGyjJd87QdI2aaMp1uEXTDhs7dFEPICg",
            "https://drive.google.com/uc?export=view&id=1u_iSPSN5hDhrc3Oryx_--UsgJbTXd6Od",
            "https://drive.google.com/uc?export=view&id=1aoK6kfwuExdrSPGJG6YdaNcVCEQ8kGQc",
            "https://drive.google.com/uc?export=view&id=17zZ9IYQ3pVDKIUagZlkENjRXOY7-Lic2",
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
                "kesan": "Kakak ini menyenangkan banget",  
                "pesan":"semangat terus kuliahnya dan jaga kesehatan!"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "122450000",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Hui",
                "hobbi": "Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini baik dan ramah banget",  
                "pesan":"semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "Kakak ini asik",  
                "pesan":"semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini asik banget",  
                "pesan":"semangat terus kuliahnya kak!"
            },
            {
                "nama": "Anisa Fitriyani",
                "nim": "122450019",
                "umur": "19",
                "asal": "Bernung, Pesawaran",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Drakor",
                "sosmed": "@ansftynn_",
                "kesan": "Kakak ini menyenangkan",
                "pesan": "semangat dan sukses terus kak!"
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "Abang ini baik dan ramah.",
                "pesan": "Sukses terus bang!"
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Baca Al-Qur’an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak ini baik dan ramah",
                "pesan": "Semangat kuliahnya kak!"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak ini ramah banget",
                "pesan": "Semangat terus kak"
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang ini baik dan ramah",
                "pesan": "Semangat kuliahnya bang"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal": "Ogan Ilir",
                "alamat": "Natar",
                "hobbi": "Nyari Sinyal di Gedung F",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini menyenangkan banget",
                "pesan": "Semangat kuliahnya kak"
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450126",
                "umur": "22",
                "asal": "Surakarta",
                "alamat": "Sukarame",
                "hobbi": "Melukis",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abang ini ramah banget",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal": "Sumatra Barat",
                "alamat": "Way Huwi",
                "hobbi": "Baca Buku, Ngoding, Ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini baik dan ramah",
                "pesan": "Semangat kuliahnya kak"
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Billabong, Gedong Air",
                "hobbi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang ini baik dan ramah",
                "pesan": "Semangat kuliahnya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TnU0arNMv-kXSeD5AHsim59_Zb1_kA0_", #20
            "https://drive.google.com/uc?export=view&id=1At6lkXB4pT2wY0iE0iSfvtPZdNhM81Pv", #21
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kos Putri Rahayu",
                "hobi": "Bernyanyi",
                "sosmed": "@annisalutfia_",
                "kesan": "Kakak ini asik sekali, friendly, public speakingnya juga bagus, tegas, dan memiliki pemahaman yang luas",  
                "pesan":"Semangat terus kuliahnya kak, semoga sehat selalu, dan jangan lupa untuk terus tersenyum" #20
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang ini tegas, asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus bang" #21
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def departemenpsda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1NcUcdC7OnzBewdFTtjDBA2FxV8DBYc9I", #22
            "https://drive.google.com/uc?export=view&id=1HuvD1X9ffARDvtI0f6MhRetQdJ3echd8", #23
            "https://drive.google.com/uc?export=view&id=1ROwkaQx-TdIHgkImMAY68glWMEkC2YC_", #24
            "https://drive.google.com/uc?export=view&id=1oi7ksKS4VX3NiWAPJV4hGXox1E3Pv5if", #25
            "https://drive.google.com/uc?export=view&id=1kc3L4WDz_rU2I4w64hWPmS3ahHAo019J", #26
            "https://drive.google.com/uc?export=view&id=1tpp3oW03lcDf1Ja3cYctAFJBk1DsRuEL", #27
            "https://drive.google.com/uc?export=view&id=1QzbbWQGFO3d8J3nhTqiTY2YKXStYe2Pi", #28
            "https://drive.google.com/uc?export=view&id=1-Jwk4QD73N-eqgVHThxcCBKcYiqbnviM", #29
            "https://drive.google.com/uc?export=view&id=14h1CfeEZ_0l0USQ29LO3pIViBTZNTn3S", #30
            "https://drive.google.com/uc?export=view&id=1SLaMwTobBogriMe3C9D4DbzT8f-0XtE_", #31
            "https://drive.google.com/uc?export=view&id=1UT1n8axPkDBFHWWRkEVmCwS0zndCDmWR", #32
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #33
            "https://drive.google.com/uc?export=view&id=1HNmT_UIDwKfNlIOQop1bFlTrvDzvjuDL", #34
            "https://drive.google.com/uc?export=view&id=13RbHt4K3B-NkwX0UNufDgE2BqtaSAO4f", #35
            "https://drive.google.com/uc?export=view&id=1nrs4kPPxWNyrYyrPvfFMPTwsO_Jt4ZuF", #36
            "https://drive.google.com/uc?export=view&id=1uZZi5rcn8rWELyr3csaBfnQhUW7R1kjZ", #37
            "https://drive.google.com/uc?export=view&id=1_13f7Eyk-JBHphIKwhl8-WH1AtLrYjOy_R", #38
            "https://drive.google.com/uc?export=view&id=1tWcHQoYtStLAC3R1ggsWL1gXrlcfl0Ic", #39
            "https://drive.google.com/uc?export=view&id=1YTEVLJr4KAbeEMNYQRgw5oxOFue9KZ4L", #40
            "https://drive.google.com/uc?export=view&id=1YLe6a7Bkh9-oS4Li-xa6o9uG7YH3zIt3", #41
            "https://drive.google.com/uc?export=view&id=1F4GDJcmrpVzVQDsyny3x7iJchBC4jF9o", #42
            "https://drive.google.com/uc?export=view&id=1GAVpQHt2dE1uhoB5Z4hN8_s3UhOJ71d6", #43
            "https://drive.google.com/uc?export=view&id=1zgTjoEa7VLpz-8CZbz8aoNn31QJMbIvF", #44
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Khobam",
                "hobi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abang ini asik sekali, punya pemikiran yang luas, tegas, dan seru untuk diajak diskusi",  
                "pesan":"Semangat terus kuliahnya bang, semoga bisa cepat lulus dengan hasil yang memuaskan" #22
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabeth",
                "kesan": "Kakak ini asik",  
                "pesan":"Semangat terus kak" #23
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Marahin orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak ini asik, friendly",  
                "pesan":"Semangat terus kak kuliahnya" #24
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobi": "Main",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak ini asik, dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya" #25
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Metro",
                "hobi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak, jangan lupa untuk tersenyum" #26
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini murah senyum, baik, dan seru",  
                "pesan":"Semangat kuliahnya kakak" #27
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Jalan Pangeran Senopati Raya 18",
                "hobi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang ini asik, baik, seru diajak ngobrol",  
                "pesan":"Semangat terus bang kuliahnya, semoga hasil yang didapat bagus" #28
            },
            {
                "nama":  "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobi": "Ngukur jalan",
                "sosmed": "@dransyh_",
                "kesan": "Abang ini asik, baik, seru diajak ngobrol",  
                "pesan":"Semangat terus bang" #29
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak ini asik, baik, dan murah senyum",  
                "pesan":"Semangat terus kuliahnya kak" #30
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "1214500148",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Pulau Damar Kobam",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abang ini asik, baik, ramah, friendly, dan suka ngelawak, seru diajak ngobrol",  
                "pesan":"Semangat terus bang kuliahnya, semoga cepat lulus dan mendapatkan pekerjaan sesuai dengan apa yang diinginkang bang" #31
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Kakak ini asik, baik dan ramah",  
                "pesan":"Semangat terus kak kuliahnya" #32
            },
            {
                "nama": " Ibnu Farhan Al-Ghifari",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@-",
                "kesan": "Abang ini asik",  
                "pesan":"Semangat terus bang" #33
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "Abang ini tegas, asik, dan friendly",  
                "pesan":"Semangat terus bang kuliahnya" #34
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Golf Asri",
                "hobi": "Ngetik print hello dunia",
                "sosmed": "@kemasverii",
                "kesan": "Abang ini pinter, baik, asik, seru diajak ngobrol dan diskusi",  
                "pesan":"Semangat terus bang kuliahnya, semoga apa yang di cita-citakan bisa terwujud" #35
            },
            {
                "nama": "Leonard Andreas Napitupulu",
                "nim": " ",
                "umur": " ",
                "asal":" ",
                "alamat": " ",
                "hobi": " ",
                "sosmed": "@-",
                "kesan": "Abang ini tegas, asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus bang" #36
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobi": "Dengerin The Adams",
                "sosmed": "@presilliamg",
                "kesan": "Kakak ini asik, baik, dan murah senyum",  
                "pesan":"Semangat terus kak kuliahnya" #37
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450122",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak ini asik, mempunyai pikiran serta public speaking yang bagus, dan murah senyum",  
                "pesan":"Semangat terus kuliahnya kakak" #38
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok, Jawa Barat",
                "alamat": "Jalan Airan Raya",
                "hobi": "Dengerin juicy luicy",
                "sosmed": "@sahid_maul19",
                "kesan": "Abang ini asik, mempunyai pikiran serta public speaking yang bagus, dan cocok diajak diskusi",  
                "pesan":"Semangat terus bang" #39
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Perum Korpri",
                "hobi": "Minum kopi, belajar, bikin Deyvan senang",
                "sosmed": "@roselivness__",
                "kesan": "Kakak ini tegas, asik, mempunyai pikiran serta public speaking yang bagus,",  
                "pesan":"Semangat terus kuliahnya kak" #40
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abang ini, asik, orangnya santai, friendly, suka menolong dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus bang kuliahnya, semoga bisa cepat lulus dengan hasil yang memuaskan" #41
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar, Game, Baca Komik",
                "sosmed": "@gedemoenaa",
                "kesan": "Abang ini asik, baik, dan ramah",  
                "pesan":"Semangat terus bang kuliahnya semoga cepat lulus dengan nilai yang bagus" #42
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinaclcv",
                "kesan": "Kakak ini asik, dan mempunyai pikiran serta public speaking yang bagus",  
                "pesan":"Semangat terus kak" #43
            },
            {
                "nama":  "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abang ini asik, baik, dan ramah",  
                "pesan":"Semangat terus bang kuliahnya" #44
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()
# Tambahkan menu lainnya sesuai kebutuhan
