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
            st.write(f"Nama        : {data_list[i]['nama']}")
            st.write(f"NIM         : {data_list[i]['nim']}")
            st.write(f"Umur        : {data_list[i]['umur']}")
            st.write(f"Asal        : {data_list[i]['asal']}")
            st.write(f"Alamat      : {data_list[i]['alamat']}")
            st.write(f"Hobi       : {data_list[i]['hobi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan       : {data_list[i]['kesan']}")
            st.write(f"Pesan       : {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10JMTzZp346Jpvx4S7PRfMG7XXTYHmDXc",#1
            "https://drive.google.com/uc?export=view&id=1V00ajYtfybobCZxx3BtGLgxfgfgxMYvA",#2
            "https://drive.google.com/uc?export=view&id=1Tazku1SaObGy6LaXIviIlggP0FEWfPEy",#3
            "https://drive.google.com/uc?export=view&id=1bb-7cSuTgkoRezMkbdLUo-faMPZIdRMN",#4
            "https://drive.google.com/uc?export=view&id=1fC9Nho0n_A6sacyRUQzdPZ_Nt3q2W7ct",#5
            "https://drive.google.com/uc?export=view&id=1zp4MVBN-LEZdb5gvcFhf6zYmqlsC5ei2",#6
       
        ]
        data_list = [
            {
                "nama"  : "Kharisma Gumilang",
                "nim"   : "121450142",
                "umur"  : "21",
                "asal"  :"Palembang",
                "alamat": "Pulau Damar",
                "hobi" : "Dengerin musik",
                "sosmed": "@amsirahk",
                "kesan" : "Baik dan Keren banget",  
                "pesan" :"semangat terus kuliahnya bang"#1

            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450077",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobi": "Main gitar",
                "sosmed": "@pndrinsnptr2",
                "kesan": "Abangnya asik",  
                "pesan":"semangat terus kuliahnya bang"#2

            },
            {
               "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumsel",
                "alamat": "Kota Baru",
                "hobi": "Nonton drakor",
                "sosmed": "@azilem",
                "kesan": "Kakaknya lucu",  
                "pesan":"semangat terus kuliahnya kakak!"#3

            },
            {
                "nama": "Hartiti Fadhilaj",
                "nim": "12145031",
                "umur": "21",
                "asal":"Sumatera Selatan",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakaknya baik dan keren",  
                "pesan":"semangat terus kuliahnya kakak!" #4

            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Nangka 4",
                "hobi": "Dengerin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "kakaknya baik dan keren",  
                "pesan":"semangat terus kuliahnya kakak!"#5

            },
            {
               "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobi": "Dengerin bang Pandra Gitaran",
                "sosmed": "@azilem",
                "kesan": "kakaknya baik dan keren",  
                "pesan":"semangat terus kuliahnya kakak!" #6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ljb9SvoosMi5KmnZeK4zVxS7voKFkgcU",#1
            "https://drive.google.com/uc?export=view&id=1NjhtffCc82MtBFUSA2fzTAVC5_imxkkg",#2
            "https://drive.google.com/uc?export=view&id=10HlLY9RZ2J11NaAI-lcOv_6u1Ku6nBvh",#3
            "https://drive.google.com/uc?export=view&id=1Dp07vXIkUG2iC04B3wIEpvQCNVvxq4Z1",#4
            "https://drive.google.com/uc?export=view&id=1Ffk9SXS1tLeogQlM8nqmscilaqXUXQSE",#5
            "https://drive.google.com/uc?export=view&id=1gqKqs1xSchDmHs-yV6Hvbe2j_t7wNO3G",#6
            "https://drive.google.com/uc?export=view&id=1aHSlA8xzCqpjE3uVzhRNStT0zyX5POUo",#7
            "https://drive.google.com/uc?export=view&id=1mcaAXEfl3s1SelPYauHeh7YucCyRvxJn",#8
            "https://drive.google.com/uc?export=view&id=1XLwRMp-nUeR7mkaMEHv4Thx8NQKygWUg",#9
            "https://drive.google.com/uc?export=view&id=1hUiGkZy3YhqCfERBH08wPtevcIY9vPbM",#10
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",#11
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Bertanya sama GPT",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakaknya asik banget dan cara berkomunikasinya enak didengar",  
                "pesan":"semangat kak terus menginspirasi dan semangat kuliahnya!" #1

            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang Selatan",
                "alamat": "Way Hui",
                "hobi": "Membaca",
                "sosmed": "@annisacahyanisurya",
                "kesan": "kakaknya lucu dan asik",  
                "pesan":"semangat terus kuliahnya kak!" #2

            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Menonton Film",
                "sosmed": "@wlsbn0",
                "kesan": "kakaknya baik banget dan mukanya adem",  
                "pesan":"sukses terus kuliahnya kak!" #3

            },
            {
               "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "20",
                "asal":"Tanggerang",
                "alamat": "Jati Agung",
                "hobi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "cantik dan asik",  
                "pesan":"semangat terus kuliahnya kak!" #4

            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobi": "Sholat Dhuha",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya baik",  
                "pesan":"semangat terus kuliahnya bang!" #5

            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Baca Al-qur’an",
                "sosmed": "@fleurnsh",
                "kesan": "Kakaknya baik dan lucu",  
                "pesan":"semangat terus kuliahnya kak!" #6

            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Lampung Timur",
                "hobi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "kakanya baik banget",  
                "pesan":"semangat terus kuliahnya kak!" #7

            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450110",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan": "tinggi banget",  
                "pesan":"jangan lupa kasih makan kucing bang" #8

            },
            {
                "nama": "Muhammad fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta",
                "alamat": "Sukarame",
                "hobi": "Melukis",
                "sosmed": "@fhrul.pdf",
                "kesan": "abangnya baik banget",  
                "pesan":"semangat terus kuliahnya bang!" #9

            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Suka Bengong",
                "sosmed": "@jeremia_s_",
                "kesan": "Abangnya keren dan baik ",  
                "pesan":"semangat terus kuliahnya bang" #10

            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Way Huwi",
                "hobi": "Baca Buku, Ngoding, Ibadah",
                "sosmed": "@berlyyanda",
                "kesan": "kakaknya baik dan seru",  
                "pesan":"semangat terus kuliahnya kak!" #11
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1W416RWlfUso17VcEJ7JOF6mZk4U62WWo",#1
            "https://drive.google.com/uc?export=view&id=1Uo7U9JXLSgCoj6eCVV1gj8O3Z00JLEaJ",#2
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450093",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobi": "Bernyanyi",
                "sosmed": "@annisalutfia_",
                "kesan": "Kakaknya baik dan cara berkomunikasinya enak didengar",  
                "pesan":"semangat terus kuliahnya kak!" #1

            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kota baru",
                "hobi": "Tidur",
                "sosmed": "@bintangtwinkle",
                "kesan": "abangnya baik dan tegas",  
                "pesan":"semangat terus kuliahnya bang!" #2

            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
    
elif menu == "Departemen PSDA":
    def departemenpsda ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bGrtJvqxyagI71zr0yOgCYOATjcdjnSv", #bang econ
            "https://drive.google.com/uc?export=view&id=1hd_ZBV8YXCjifW3POxChGh5B9432VlOo", #kak abeth
            "https://drive.google.com/uc?export=view&id=1kJ1j6egF-fXTTkIuW06uhBannSIJiqPE", #kak afifah
            "https://drive.google.com/uc?export=view&id=1T1Y3AmgHVb38M74tIlajAdv0LU0a_BzY", #kak allya
            "https://drive.google.com/uc?export=view&id=1c1c6ZOytsjEGJeWPLiSPIFy9w56z-ioi", #kak eksanty
            "https://drive.google.com/uc?export=view&id=15O1wFRBBL-6CnyHdG03sZiObWNUIpNOf", #kak farahanum
            "https://drive.google.com/uc?export=view&id=1SJBR8830ArwIeedJJ5rpBZu4-uVP1jPZ", #bang ferdy
            "https://drive.google.com/uc?export=view&id=1Dkk4HDAX80mKS7KyeYuhAx3fKY-f45IO", #bang deri
            "https://drive.google.com/uc?export=view&id=1vfhH9Mdce6NDwSR4emT28Mj1EzmlroxN", #kak okta
            "https://drive.google.com/uc?export=view&id=1I1D_PIcLwCclXzN6l7Zmlnagt8nAlCrQ", #bang depan
            "https://drive.google.com/uc?export=view&id=1TXUm18LQjY9Vjesd-fC5joWipaepGa7l", #bang jo
            "https://drive.google.com/uc?export=view&id=1M2bkf0VH4oIOoN1cjJCqwBgg70PH_NAz", #bag kem
            "https://drive.google.com/uc?export=view&id=137TseVQV8bjwy8rpn7jFVH3Hdf-0HLXg", #kak presilia
            "https://drive.google.com/uc?export=view&id=1ChmIvTdvsivyaMx54qkCcHKr1Cq_oO5Z", #kak rafa
            "https://drive.google.com/uc?export=view&id=1OIJyWN2aU_A7NqdDMYghhCX3uutNS3Q7", #bang sahid
            "https://drive.google.com/uc?export=view&id=1o_Gu7xby0jCOwP50ngKqo-CkzjPS9dMq", #kak vanes 
            "https://drive.google.com/uc?export=view&id=1N8IaM0W29s9Pw1UV48uidylVqw6vdfPC", #bang ateng
            "https://drive.google.com/uc?export=view&id=1FgME2Ar8gTqa5X7to2dkLgsn0rG-8AS9", #bang gede
            "https://drive.google.com/uc?export=view&id=12kIyMuSNELwUt6GZk_lPGgBsY6I9Y2CB", #kak jaclin
            "https://drive.google.com/uc?export=view&id=1KyUWdpG4tnwBO98Izq3bB-nFT4qpF7iP", #bang rafly
            "https://drive.google.com/uc?export=view&id=1SngJUeMi49X6v7qNbO_OianmKTZvv4r9", #kak syalaisha
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya keren dan tegas",  
                "pesan":"Semangat terus kuliahnya bang" #bang econ

            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "18",
                "asal":"Tangerang",
                "alamat": "Kemiling",
                "hobi": "Bernafas",
                "sosmed": "@celisabeth",
                "kesan": "Kakaknya lucu dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #kak abeth
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Marahin orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya lucu dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #kak affifah

            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobi": "Main",
                "sosmed": "@allyaislami_",
                "kesan": "Kakaknya keren dan ramah",  
                "pesan":"Semangat terus kuliahnya kak!" #kak allya
            },
            {
                "nama": "Eksanty Febriana Sugma Islamiyati",
                "nim": "122450001",
                "umur": "20",
                "asal":"Jawa Barat",
                "alamat": "Metro",
                "hobi": "Nyopet",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya keren dan baik",  
                "pesan":"Semangat terus kuliahnya kak!" #Kak eksanty
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Bengong",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #kak farahanum
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Jalan Pangeran Senopati Raya 18",
                "hobi": "Baca Kitab Suci",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abangnya baik dan pendiam",  
                "pesan":"Semangat bang!" #bang ferdy

            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jalan Pagar Alam Kedaton",
                "hobi": "Ngukur Jalan",
                "sosmed": "@dransyh_",
                "kesan": "abangnya lucu dan asik",  
                "pesan":"semangat terus kuliahnya bang!" #bang deri

            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Huwi",
                "hobi": "Travelling",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "kakanya baik dan keren", 
                "pesan":"semangat terus kuliahnya kak!" #kak okta

            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Duri, Riau",
                "alamat": "Pulau Damar Kobam",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "abangnya lucu banget dan seru",  
                "pesan":"Jangan pernah cape menghibur orang ya bang" #bang depan
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jalan Lapas",
                "hobi": "Asprak",
                "sosmed": "@johanneskrsjnnn",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"semangat terus kuliahnya bang!" #bang jo
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Golf Asri",
                "hobi": "Ngetik print hello dunia",
                "sosmed": "@kemasverii",
                "kesan": "Abangnya seru banget, sepuh kodingan, dan baik banget",  
                "pesan":"Semangat terus kuliahnya bang!" #bang kemas
            },
            {
                "nama": "Presilia",
                "nim": "122450081",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Kota Baru",
                "hobi": "Dengerin The Adams",
                "sosmed": "@presilliamg",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #kak presilia

            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450122",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakaknya baik dan asik",  
                "pesan": "Semangat terus kuliahnya kak!" #kak rafa
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok, Jabar",
                "alamat": "Jalan Airan Raya",
                "hobi": "Dengerin juicy luicy",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya baik banget dan seru",  
                "pesan":"Semangat terus kuliahnya bang!" #bang sahid
            },
            {
                "nama": "Vanessa Olivia Rose",
                "nim": "121450108",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Perum Korpri",
                "hobi": "Minum kopi, belajar, bikin deyvan senang",
                "sosmed": "@roselivness__",
                "kesan": "Kakaknya jago basket dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #kak vanessa
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abangnya baik dan cara berkomunikasinya enak didengar",  
                "pesan":"Semangat terus kuliahnya bang!" #bang ateng
            },
            {
                "nama": "Gede Moana",
                "nim": "121450014",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Korpri Raya",
                "hobi": "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan": "Abangnya baik dan seru",  
                "pesan":"Semangat terus kuliahnya bang!" #bang gede
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "121450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #kak jaclin

            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main game",
                "sosmed": "@raflyy_pd2684",
                "kesan": "Abangnya baik dan seru",  
                "pesan": "Semangat terus kuliahnya bang!" #bang rafly

            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobi": "Baca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakaknya baik dan asik",  
                "pesan":"Semangat terus kuliahnya kak!" #kak syalaisha
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemenpsda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17PkJXwqPqa4lyeBMno1iCsnvqGy1ytYd", #bang rafi
            "https://drive.google.com/uc?export=view&id=1VV6PXcclOuKPR3mgIlaQ4H1Hljal7x3A", #kak anova
            "https://drive.google.com/uc?export=view&id=1Cziha9Z0PhCGP0fVjSDi4mM3KCF1cfo6", #bang ahmad
            "https://drive.google.com/uc?export=view&id=1SH5Ep3AglNZL-k1rkBGSmzKBD25iFGx0", #bang regi
            "https://drive.google.com/uc?export=view&id=1U7d0QQNQjA7SZuPS49q-lezyfmJv9by7", #kak syalaisha
            "https://drive.google.com/uc?export=view&id=1h00eL-OCFb9fgoTX6BRQSKVqKjFirDJw", #bang anwar
            "https://drive.google.com/uc?export=view&id=1tnIfxuKgWTPuwW5h4YrdnrIHD2iqtlGE", #kak deva
            "https://drive.google.com/uc?export=view&id=1bKU_PYXcMkF3IA6wdXRKYkDsB39k0cAc", #kak dinda
            "https://drive.google.com/uc?export=view&id=1ufAiRZrrKLPFSdZtEMviJAeGhqrLgfbE", #kak marleta
            "https://drive.google.com/uc?export=view&id=1VZkHwMbxchrmLkJZ_2nj3odt-mNVnmRJ", #kak rut
            "https://drive.google.com/uc?export=view&id=1qHkw0rNj60mtNRZi4az493RHbr5OYmWg", #kak syadza
            "https://drive.google.com/uc?export=view&id=1CXYxfH77XFnJ4ZbMXCjSwyVxxTcPopdc", #bang adit
            "https://drive.google.com/uc?export=view&id=10HtMXzV8oBASuu8L7UKsruQ_O3NmxmhB", #bang eggi
            "https://drive.google.com/uc?export=view&id=1Cp_sIhIu5a70rheKW0-_A5NXfv7cRNxj", #kak febiya
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #bang happy
            "https://drive.google.com/uc?export=view&id=1VXrs2jQNsJHC_aUDj2nV2KVQCufotrR4", #bang randa
        ]
        data_list = [
          {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal": "Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobi": "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal": "Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama"  : "Muhammad Regi Abdi Putra Amanta",
                "nim"   : "122450031",
                "umur"  : "19",
                "asal"  :"Palembang",
                "alamat": "Jl. Permadi",
                "hobi" : "Ngasprak ADS",
                "sosmed": "@mregiiii_",
                "kesan" : "",  
                "pesan" :""

            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gg. Yudistira",
                "hobi": "Review jurnal bu mika",
                "sosmed": "@dkselsd_31",
                "kesan": "",  
                "pesan":""

            },
            {
               "nama": "Natanael Oktavianus Partahan Sihombing",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""

            },
            {
                "nama": "Anwar Muslim",
                "nim": "122450117",
                "umur": "21",
                "asal":"Bukittinggi",
                "alamat": "Korpri",
                "hobi": "ML (Machine Learning)",
                "sosmed": "@here.am.ai",
                "kesan": "",  
                "pesan":"" 

            },
            {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobi": "Resume Webinar",
                "sosmed": "@anjaniiidev",
                "kesan": "",  
                "pesan":""

            },
            {
               "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Membaca jurnal bu mika",
                "sosmed": "@dindanababan",
                "kesan": "",  
                "pesan":"" 
            },
            {
                "nama"  : "Marleta Cornelia Leander",
                "nim"   : "122450092",
                "umur"  : "20",
                "asal"  :"Depok",
                "alamat": "Gg. Nangka 3",
                "hobi" : "Review jurnal bu mika",
                "sosmed": "@marletacornelia",
                "kesan" : "",  
                "pesan" :""
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kepulauan Riau",
                "alamat": "Gg. Nangka 3",
                "hobi": "Menghitung akurasi",
                "sosmed": "@junitaa_0406",
                "kesan": "",  
                "pesan":"" #kak rut

            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450074",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobi": "Membangkitkan bilangan",
                "sosmed": "@puspadrr",
                "kesan": "",  
                "pesan":"" 
            },
            {
                "nama"  : "Aditya Rahman",
                "nim"   : "122450113",
                "umur"  : "20",
                "asal"  :"Metro",
                "alamat": "Korpri",
                "hobi" : "Ngoding wisata",
                "sosmed": "@rahm.adityaa",
                "kesan" : "",  
                "pesan" :""
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri",
                "hobi": "Ngoding wisata",
                "sosmed": "@_egistr",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobi": "Review jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "",  
                "pesan":""

            },
            {
               "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main game",
                "sosmed": "@sudo.syahrulramadhan",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur dan Berkembang",
                "sosmed": "@randaandriana_",
                "kesan": "",  
                "pesan":"" 
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal ():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1K3gjaEX0QaFYeqnuuXJPpjuM7MIZ1nlk", #bang sae tama
            "https://drive.google.com/uc?export=view&id=1kYyuqz6v6nrerLvOB22lrXvgCTDL4eXr", #kak ramadhita
            "https://drive.google.com/uc?export=view&id=1WvZPP4-CUlByfUCnNsomsyNvdFqS63bX", #kak nazwa
            "https://drive.google.com/uc?export=view&id=1PTwxv9zYpSDhnl9Agto_ECllWiefRCtc", #bang bastian
            "https://drive.google.com/uc?export=view&id=1lTb-LMphsoR3weXlKQb21jMRJNUOV9rG", #kak dea
            "https://drive.google.com/uc?export=view&id=1XJR1jNP5eKI2zMTcli948IGUrUZKnhBz", #kak ester
            "https://drive.google.com/uc?export=view&id=1zM5hQyLBKyNIP66W2qOHVqmpoLGP5LSo", #kak natasya
            "https://drive.google.com/uc?export=view&id=1HvSxj500hgqIqxnaP7wYoDkHBYfIpGaY", #kak novelia
            "https://drive.google.com/uc?export=view&id=1y4vbk9B0FYMaq2gm68yTWzg4clw7Tcj6", #kak ratu
            "https://drive.google.com/uc?export=view&id=1VO-6ifn935lDzGa4RuIFS7av4CKBAc07", #bang tobias
            "https://drive.google.com/uc?export=view&id=15vZdjkoD6aCdIi0_rROH1ILSTwnwYdkV", #kak yohana
            "https://drive.google.com/uc?export=view&id=1ioiUQOdGSIBAUeWCbbLR3Hky7Ggq4xgb", #bang rizki
            "https://drive.google.com/uc?export=view&id=1YCcxZv-qPFsM7izvH489iz0toQmMCdmr", #bang arafi
            "https://drive.google.com/uc?export=view&id=1ZqI4mEx8i1_uOvNtKHVSnxjQcTmQfzVe", #kak asa
            "https://drive.google.com/uc?export=view&id=1KU4BcP7U4LLp0UBPRFUrWZWhFi3rdwr-", #kak chalifia
            "https://drive.google.com/uc?export=view&id=1oU4G-vUWZLe7Vgia70TprppiUW7-kU2_", #bang irvan
            "https://drive.google.com/uc?export=view&id=1io1qk6Y9aVbb33kEBuEBHmKxyjcotP6O", #kak izza
            "https://drive.google.com/uc?export=view&id=1wv-ANiAqBiA8PXkxVSYhKAmaCraMjNkc", #kak alyaa
            "https://drive.google.com/uc?export=view&id=1p2IRB8hNjsyo8GmUECT3g367spF-tvIV", #bang raid
            "https://drive.google.com/uc?export=view&id=1jvg21cKs7nQbXcvyI_JaRVRarUpSHMwW", #kak yuna
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "12145",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jati Mulyo",
                "hobi": "Bangun Pagi",
                "sosmed": "@yogyyy",
                "kesan": "",  
                "pesan":"" #bang sae tama

            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "TVRI",
                "hobi": "Jalan-jalan",
                "sosmed": "@ramadhitatifa",
                "kesan": "",  
                "pesan":"" #kak ramadhita
            },
             {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Way Kandis",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "",  
                "pesan":"Semangat terus kuliahnya bang!" #kak nazwa
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Main Game",
                "sosmed": "@bastiansilaban_",
                "kesan": "",  
                "pesan":"" #bang bastian
            },
            {
                "nama"  : "Dea Mutia Risani",
                "nim"   : "122450099",
                "umur"  : "20",
                "asal"  :"Sumatera Barat",
                "alamat": "Korpri",
                "hobi" : "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan" : "",  
                "pesan" :"" #kak dea
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450005",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Kirim BC-an",
                "sosmed": "@esteriars",
                "kesan": "",  
                "pesan":"" #kak ester
            },
            {
               "nama": " Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Jadi Humas",
                "sosmed": "@natee__15",
                "kesan": "",  
                "pesan":"" #kak natasya
            },
            {
                "nama": " Novelia Adinda",
                "nim": "122450104",
                "umur": "20",
                "asal":"Saburai",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "",  
                "pesan":"" #kak novelia

            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Pulang malam",
                "sosmed": "@jasminednva",
                "kesan": "",  
                "pesan":"" #kak ratu
            },
            {
               "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Pemda",
                "hobi": "Berkebun",
                "sosmed": "@tobiassiagian",
                "kesan": "",  
                "pesan":"" #bang tobias
            },
            {
                "nama"  : "Yohana Manik",
                "nim"   : "122450",
                "umur"  : "20",
                "asal"  :"Sumatera Utara",
                "alamat": "Belwis",
                "hobi" : "Menimba ilmu",
                "sosmed": "@yo_anamnk",
                "kesan" : "",  
                "pesan" :"" #kak yohana

            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "TVRI",
                "hobi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "",  
                "pesan":"" #bang rizki
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Way huwi",
                "hobi": "Imam TVRI",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "Kirain abangnya pendiam ternyata orangnya rame",  
                "pesan": "Semoga lucu terus bang" #bang arafi

            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal":"Muara enim",
                "alamat": "Korpri",
                "hobi": "Nyuci baju",
                "sosmed": "@u_yippy",
                "kesan": "",  
                "pesan":"" #kak asa
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Q-Time",
                "sosmed": "@chlfawww",
                "kesan": "",  
                "pesan":"" #kak chalifia

            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "",  
                "pesan":"" #bang irvan
            },
              {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "Kakaknya ramah banget dan asikk",  
                "pesan":"Semangat ngaspraknya kak, jangan cape liat kita" #kak izza
            },
            {
               "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Jadi daplok kelompok 1",
                "sosmed": "@alyaavanefi",
                "kesan": "Kakaknya lucu gemes, baik banget, dan seru",  
                "pesan":"Semangat terus kuliahnya ya kak dan jangan pernah cape ajarin kita" #kak alyaa

            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Telat",
                "sosmed": "@rayths_",
                "kesan": "",  
                "pesan":"" #bang raid
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal":"Way Kanan",
                "alamat": "Sukarame",
                "hobi": "Membaca chat",
                "sosmed": "@tria_y062",
                "kesan": "",  
                "pesan":"" #kak yuna
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1T-p_S1yFRkSIwtXB4PShNKRf_LMID3Rv", #bang dimas
            "https://drive.google.com/uc?export=view&id=1uyY8GKyHfBTbUKKWeYLWRItCeqeOkewv", #kak catherine
            "https://drive.google.com/uc?export=view&id=12ZdBE9sVhvJP87daxMutDX5M1MMc9CdW", #bang akbar
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak rani
            "https://drive.google.com/uc?export=view&id=10f49Q00x1DmXOGdU_nY8sCo0wows2Aeh", #bang rendra
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak salwa
            "https://drive.google.com/uc?export=view&id=1WvV7wEN1GqJsvu_dxXaXrRn9WX_ucIdZ", #bang ari
            "https://drive.google.com/uc?export=view&id=1neTbnPqJF2KbE1ymCRA1edeY_MQ8B2mQ", #kak azizah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak dearni
            "https://drive.google.com/uc?export=view&id=1IBiR6PkvU-0ZVzFZ2y6AdaVPUrV8VOne", #kak meira
            "https://drive.google.com/uc?export=view&id=1CxOxBUQwjb1QZNJsTdzTWSlsmiO0oseR", #bang rendi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak renta
            "https://drive.google.com/uc?export=view&id=1HC-IN_oBQ_lqdc-SdUWYiC4M5nnLS6d4", #bang yosia
        ]
        data_list = [
            {
                "nama": "Dimas Rizky Ramadhani",
                "nim": "121450027",
                "umur": "20",
                "asal":"Pamulang, Tangerang Selatan",
                "alamat": "Way Kandis Kobam",
                "hobi": "Manjat tower sutet",
                "sosmed": "@dimzrky",
                "kesan": "Pembawaan abangnya asik banget dan banyak bercandanya jadi seru",  
                "pesan": "Semangat terus bang kuliahnya semoga cepat lulus" #bang dimas
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca novel",
                "sosmed": "@Catherine.sinaga",
                "kesan": "",  
                "pesan":"" #kak catherine

            },
            {
                "nama": "Akbar Resdika",
                "nim": "121450066",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Dalam",
                "hobi": "Memelihara Dino",
                "sosmed": "@akbar_resdika",
                "kesan": "",  
                "pesan":"" #bang akbar
            },
            {
               "nama": "Rani Puspita sari",
                "nim": "122450030",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Rajabasa",
                "hobi": "Mengaji",
                "sosmed": "@rannipu",
                "kesan": "",  
                "pesan":"" #kak rani
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Jl. Lapas Raya",
                "hobi": "Nulis lagu",
                "sosmed": "@rendaepr",
                "kesan": "",  
                "pesan":"" #bang rendra

            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal":"Pesawaran",
                "alamat": "Airan raya",
                "hobi": "Ngeliat cogan",
                "sosmed": "@slwfn_694",
                "kesan": "",  
                "pesan":"" #kak salwa

            },
            {
                "nama": "Ari Sigit",
                "nim": "121450",
                "umur": "23",
                "asal":"Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobi": "Main Futsal",
                "sosmed": "@ari_sigit17",
                "kesan": "",  
                "pesan":"" #bang ari
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal":"Lampung Selatan",
                "alamat": "Jati Mulyo",
                "hobi": "Bangun Pagi",
                "sosmed": "@azizahksmh15",
                "kesan": "",  
                "pesan":"" #kak azizah
            },
            {
                "nama": "Dearni Monica Br Manik",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":"" #kak dearni
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":"" #kak meira
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":"" #bang rendi
            },
            {
                "nama": "Renta Siahaan",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":"" #kak renta
            },
            {
                "nama": "Yosia Retare Banurea",
                "nim": "",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":"" #bang yosia
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

    

