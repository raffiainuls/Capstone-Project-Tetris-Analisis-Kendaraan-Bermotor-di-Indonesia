import streamlit as st
from capstone_project_gaikindo_automatic import plot_10_sales_brand, plot_sales_category, plot_top_brand_category,plot_lineup_brand_category, category_area,plot_top_car_by_category_double_cabin,plot_top_car_by_category_lcgc,plot_top_car_by_category_mpv,plot_top_car_by_category_sedan,plot_top_car_by_category_hatchback,plot_top_car_by_category_suv_crossover,plot_line_top_car_mpv,plot_line_top_car_sedan,plot_line_top_car_lcgc,plot_line_top_car_suv_crossover,plot_line_top_car_hatchback,plot_line_top_car_double_cabin,plot_electric,sales
from PIL import Image



st.set_page_config(page_title = 'Capstone Project Analisis Sales Kendaraan Bermotor',layout="wide")


header_image = Image.open("image/header.jpg")
header_image = header_image.resize((1300, 400))
st.markdown("<h1 style = 'text-align : center; color : white; font_size : 40 px; font-family : Arial'><b>Analisis Penjualan Kendaraan Bermotor di Indonesia<b></h1>", unsafe_allow_html= True)
st.image(header_image,  use_column_width=False)
st.markdown("------")
st.markdown("Created by [Raffi Ainul Afif](linkedin.com/in/raffi-ainul-afif-9811a411b/)")

paragraf1 = """<p style = 'font-size: 14px; font-family : Arial; '> Sebagai Negara berkembang dan jumlah penduduk yang banyak, tentunya juga mempengaruhi 
perkembangan didalam sektor otomotif. Perkembangan sektor otomotif di Indonesia bisa dikatakan cukup baik. pada kesempatan kali ini akan dicoba melakukan analisis penjualan
mobil yang ada di Indonesia dari berbagai variabel, apakah benar industri otomotif khususnya mobil di indonesia dari tahun ke tahun terus berkembang?, dan sebenarnya mobil seperti apa yang 
sangat diminati oleh masyarakat Indonesi?, mari kita coba bahas </p>"""
st.markdown(paragraf1, unsafe_allow_html= True)
sentence1= ''' <p style = 'font-size: 14px; font-family: Arial;'> <strong>Pertama- tama mari kita lihat sebenarnya Brand mobil apa yang sangat diminati di Indonesia ya?<strong> </p>'''
st.markdown(sentence1, unsafe_allow_html= True)


st.plotly_chart(plot_10_sales_brand, use_container_width=True, height=500)
paragraf2 = """<p style = 'font-size: 14px; font-family : Arial; '> Ternyata brand yang menduduki kasta teratas di Indonesia adalah Toyota diikuti oleh Daihatsu, Honda, 
Mitsubishi Motor, dst. Lalu kira-kira kenapa ya Brand - Brand mobil tersebut menjadi yang paling diminati oleh masyarakat Indonesia?, mari kita coba analisis lebih jauh </p>"""
st.markdown(paragraf2, unsafe_allow_html= True)

st.markdown("<h1 style = 'text-align : left; color : white; font-size : 20px; font-family : Arial'> <b>Analisist Berdasarkan Category Car<b></h1>", unsafe_allow_html= True)
st.plotly_chart(plot_sales_category, use_container_width=True, height=500)
paragraf3 = """<p style = 'font-size: 14px; font-family : Arial'> Jika dilihat dari Pie Plot diatas ternyata category mobil MPV paling diminati oleh masyarakat Indonesia
dengan 29.3% penjualan diminili oleh category mobil MPV. Dari data tersebut bisa diantirkan masyarakat Indonesia lebih suka dengan mobil category MPV yang merupakan size mobil yang pada umumnya 
besar dan dapat memuat banyak orang didalamnya, kemudian apakah hal ini ada kaitannya dengan grafik yang sebelumnya?</p>
"""
st.markdown(paragraf3, unsafe_allow_html= True)
paragraf4= '''<p style = 'font-size: 14px; font-family: Arial'> Bisa kita lihat grafik dibawah yang menunjukan penjualan per-category pada masing-masing top brand. Toyota yang merupakan Brand
terfavorit menurut data sebelumnya memiliki jumlah penjualan untuk kategori MPV yang sangat banyak, bahkan jika dibandingkan dengan top brand lainnya masih kalah cukup jauh. Mengapa bisa demikian ya?</p>
'''
st.markdown(paragraf4, unsafe_allow_html=True)
st.plotly_chart(plot_top_brand_category,use_container_width=True, height = 500)
paragraf5= '''<p style = 'font-size: 14px; font-family: Arial'> Jika ditelisik lebih detail lagi ternyata kemungkinan penyebab penjualan mobil category MPV Toyota sangat banyak berbanding lurus dengan jumlah
lineup mobil yang dimiliki oleh Toyota lebih detailnya bisa dilihat digrafik berikut ini</p>
'''
st.markdown(paragraf5,unsafe_allow_html=True)
st.plotly_chart(plot_lineup_brand_category, use_container_width=True, height = 500)
paragraf6 = '''<p style = 'font-size : 14px; font-family : Arial'> Wah sekarang kita sudah mendapatkan informasi bahwa Toyota bisa menjadi raja di Industri Otomotif di Indonesia 
Sekarang ini juga dipengaruhi lineup yang dimiliki Toyota itu sendiri juga banyak, dan tentunya ada faktor-faktor lain yang menyebabkan Toyota dapat menguasai di industri ini salah satunya mungkin kualitas 
dan harga yang sesuai dimana masyarakat Indonesia</p>
'''
st.markdown(paragraf6,unsafe_allow_html=True)
paragraf7 = '''<p style = 'font-size: 14px; font-family : Arial'> Sebelumnya kita udah mendapatkan informasi bahwa category mobil MPV menjadi yang paling diminati di Indonesia. Namun apakah category selalu mendominasi dari
setiap tahunnya dari dulu sampai sekarang? mari coba kita lihat grafik dibawah ini</p>
'''
st.markdown(paragraf7, unsafe_allow_html=True)
st.plotly_chart(category_area, use_container_width=True, height = 500)
paragraf8 ='''<p style = 'font-size :14px; font-family : Arial'> Setelah kita amati grafik area chart diatas yang merupakan perkembangan penjualan untuk tiap category dari tahun ke tahun
memang benar dulu MPV berkuasa namun seiring berjalannya waktu MPV mulai tersaingi oleh category SUV/CROSSOVER, mungkin hal ini diakibatkan karena mobil SUV/CROSSOVER saat ini memiliki karakteristik yang 
menyerupai MPV dari segi akomodasi penumpang dan tentunya secara umum mobil dengan category SUV/CROSSOVEER lebih terlihat keren atau menarik dan juga bisa jadi dari segi fitu secara umum mungkin SUV/CROSSOVER saat ini lebih baik
jika dibandingkan dengan category MPV </p>
'''
st.markdown(paragraf8, unsafe_allow_html=True)

st.markdown("<h1 style = 'text-align : left; color : white; font-size : 20px; font-family : Arial'> <b>Analisist Top Car dari Top Brand<b></h1>", unsafe_allow_html= True)

options = ['MPV','SUV/CROSSOVER','SEDAN','DOUBLE CABIN', 'LCGC', 'HATCHBACK']
category = st.radio('Category apa yang mau dilihat?', options, key = 'category')

if category == 'MPV':
    st.plotly_chart(plot_top_car_by_category_mpv,use_container_width=True, height = 500)
elif category == 'SUV/CROSSOVER':
    st.plotly_chart(plot_top_car_by_category_suv_crossover)
elif category == 'SEDAN':
    st.plotly_chart(plot_top_car_by_category_sedan, use_container_width=True, height = 500)
elif category == 'DOUBLE CABIN':
    st.plotly_chart(plot_top_car_by_category_double_cabin, use_container_width=True, height = 500)
elif category == 'LCGC':
    st.plotly_chart(plot_top_car_by_category_lcgc, use_container_width=True, height = 500)
elif category == 'HATCHBACK':
    st.plotly_chart(plot_top_car_by_category_hatchback)

sentence2 = '''<p style = 'font-size : 14px; font-family : Arial'> Pada grafik diatas bisa dilihat penjualan mobil top brand di Indonesia dari setiap category mobil yang ada, dan dibawah ini merupakan grafik perkembangan
penjualan top car dari top brand berdasarkan categorynya. </p>
'''
st.markdown(sentence2, unsafe_allow_html=True)

if category == 'MPV':
    st.plotly_chart(plot_line_top_car_mpv,use_container_width=True, height = 500)
elif category == 'SUV/CROSSOVER':
    st.plotly_chart(plot_line_top_car_suv_crossover, use_container_width=True, height = 500)
elif category == 'SEDAN':
    st.plotly_chart(plot_line_top_car_sedan, use_container_width=True, height = 500)
elif category == 'DOUBLE CABIN':
    st.plotly_chart(plot_line_top_car_double_cabin, use_container_width=True, height = 500)
elif category == 'LCGC':
    st.plotly_chart(plot_line_top_car_lcgc, use_container_width=True, height = 500)
elif category == 'HATCHBACK':
    st.plotly_chart(plot_line_top_car_hatchback, use_container_width=True, height = 500)

st.markdown("<h1 style = 'text-align : left; color : white; font-size : 20px; font-family : Arial;'> <b>Analisis Mobil Listrik di Indonesia<b></h1>", unsafe_allow_html= True)
paragraf9= '''<p style = 'font-size : 14px; font-family : Arial;'> Perkembangan teknologi di dunia saat ini sangat pesat, dan hal tersebut tentunya juga terjadi di sektor industri otomotif. Pada saat ini sudah banyak mobil yang mempunyai teknologi yang canggih,
contoh penerapan teknologi itu dapat dilihat dari munculnya mobil listrik yang sudah mulai banyak berkeliaran di Indonesia. Tentunya hal ini juga untuk mengatasi pencemaran udara yang bisa diakibatkan oleh penggualaan bahan bakar mobil konvensional. Di Indonesia sendiri
tecatat oleh data sudah ada 3 jenis mobil electrik yaitu Electric Vehicle (EV), Plugin Electric Vehicle (PHEV), dan Hybrid. EV merupakan jenis mobil listrik
yang merupakan mobil full menggunakan tenaga listrik dan tidak mempunyai rangkaian mesin bensin ataupun diesel dilamnya, PHEV merupakan mobil listrik yang tenaganya dihasilkan dari baterai sebagai sumber tenaga, namun baterai tersebut kapasitas lebih kecil jika dibandingkan 
dengan EV, akan tetapi mesin PHEV disokong oleh mesin konvensional yang dapat mengisi baterai pada saat mesin bekerja, dan Hybrid adalah gabungan mesin electric dan mesin konvensional, tipe mobil listrik ini dapat menerima sumber daya tenaga dari pengisian baterai listrik ataupun 
pengisian tenaga dengan bahan bakar bensin atau diesel. Dibawah ini merupakan perkembangan ketiga tipe mobil listrik di Indonesia. </p>
'''
st.markdown(paragraf9, unsafe_allow_html= True)

st.plotly_chart(plot_electric, use_container_width=True, height = 500)
paragraf10 = '''<p style = 'font-size : 14px; font-family : Arial;'> Bisa dilihat pada grafik perkembangan mobil listrik di Indonesia dari tahun bisa dibilang perkembangannya cukup pesat, dan jenis mobil electrik yang paling diminati di Indonesia 
adalah Hybrid. Mungkin hal ini dikarenakan jenis mobil ini merupakan kombinasi dari mobil konvensional dan listrik, dan juga dari segi design tentunya untuk saat ini mungkin dimata masyarakat Indonesia tipe hybrid ini masih lebih baik jika dibandingkan dengan jenis mobil listrik lainnya, selain itu 
perihal pengisian tenaga mobil Hybrid untuk saat ini mungkin dinilai lebih efisien karena bisa diisi tenaganya dari bahan bakar bensin atau pun diesel dan juga pengisian tenaga listriknya. Tetapi tidak menutup kemungkinan dimasa yang akan datang dengan tempat pengisian tenaga listrik di Indonesia yang makin berkembang 
penjualan mobil listrik yang lain juga akan ikut berkembang dengan pesat</p> 
'''
st.markdown(paragraf10, unsafe_allow_html= True)

st.markdown("<h1 style = 'text-align : left; color : white; font-size : 20px; font-family : Arial;'> <b>Analisis Penjualan Mobil, dan Motor dengan Indeks Penjualan Rill (IPR)<b></h1>", unsafe_allow_html= True)
paragraf11= ''' <p style = 'font-size: 14px; font-family : Arial;'> Terakhir mari kita coba analisis penjualan mobil dengan Indeks Penjualan Riil (IPR) yang merupakan hasil dari survei yang dibuat oleh Bank Indonesia
yang memberikan informasi tentang penjualan barang eceran di Indonesia, jika indeks naik, maka bisa diasumsikan tingkat konsumsi masyarakat Indonesia naik dan perkembangan ekonomi pada saat itu juga naik, dan coba kita tambahkan data penjualan sepeda motor di Indonesia sebagai data pendukung.</p>
'''
st.markdown(paragraf11, unsafe_allow_html=True)
st.plotly_chart(sales, use_container_width=True)
paragraf12= ''' <p style = 'font-size: 14px; font-family : Arial;'>Nah seteah kita amati grafik diatas ternyata tidak selalu IPR, penjualan mobil dan mobil selaras. Menariknya dari grafik diatas kita mendapatkan informasi bahwa
ternyata setiap tahun pada saat mendekati hari raya idul fitri penjualan mobil di Indonesia sejak 2019 sampai 2020 selalu turun. Pada 2019 penjualan mobil dengan IPR selaras atau sama sama mengalami penurunan. Pada 2020 pada saat mendekati lebaran 
IPR dan penjualan motor naik sedangkan penjualan mobil turun. Pada 2021 penjualan mobil dan motor tidak selaras dengan IPR yang naik. Kemudian pada 2022 mendekati lebaran IPR, penjualan mobil dan motor sama - sama turun. Dari informasi tersebut kita bisa simpulkan
tidak selamanya IPR selaras atau merepresentasi kan penjualan otomotif di Indonesia, dan juga penjualan otomotif motor dan mobil tidak selamanya selaras pula.</p>
'''
st.markdown(paragraf12, unsafe_allow_html=True)
paragraf13= ''' <p style = 'font-size: 14px; font-family : Arial;'>Jika selama mendekati lebaran penjualan mobil turun 
ada faktor, bisa jadi dikarenakan memang minat konsumtif masyarakat pada saat mendekati lebaran turun atau ekonomi di 
indonesia yang turun, hal tersebut sesuai dengan kondisi pada lebaran 2019 dan 2022. Kemudian pada saat lebaran 2020, 2021 
yang dimana tingkat IPR yang naik yang berarti tingkat ekonomi di Indonesia naik dan minat konsumtif masyarakat di Indonesia 
juga dapat diasumsikan naik tidak berbanding lurus dengan sektor penjualan mobil, mungkin masyarakat Indonesia pada saat itu 
lebih memilih untuk membeli kebutuhan lainnya yang berkaitan dengan lebaran dari pada membeli mobil. Untuk mengatasi hal tersebut mungkin dapat dilakukan promosi, 
promo atau diskon menarik mendekati lebaran yang dapat menarik perhatian masyarakat untuk melakukan pembelian mobil.
</p>'''
st.markdown(paragraf13, unsafe_allow_html=True)





