# -*- coding: utf-8 -*-
"""Capstone Project Gaikindo Automatic .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1afN-QTlPtEnjeSmav8er7sUyFAiDcLKz
"""

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import sqlite3 
from sklearn.preprocessing import MinMaxScaler


# Commented out IPython magic to ensure Python compatibility.
# Ubah lokasi direktori kerja
# Sesuaikan dengan path anda
# %cd /content/drive/My Drive/Capstone Project



car_data = pd.read_excel('Penjualan mobil 2019-2023.xlsx')
motorcycle_data = pd.read_excel('data penjualan motor.xlsx')
data_ipr = pd.read_excel('Data IPR (Index Penjualan Rill).xlsx')

motorcycle_data= motorcycle_data.melt(id_vars = ['TAHUN'], var_name = 'Bulan', value_name = 'Jumlah')
motorcycle_data['Tanggal'] = pd.to_datetime(motorcycle_data['TAHUN'].astype(str) + '-' + motorcycle_data['Bulan'], format = '%Y-%b')
motorcycle_data = motorcycle_data.drop(['Bulan', 'TAHUN'], axis = 1)
motorcycle_data

car_data = car_data.replace('-', np.nan)
car_data = car_data.replace(0, np.nan)
car_data = car_data.replace('4x4', '4X4')
car_data = car_data.replace('PICK UP', 'PICKUP')
car_data = car_data.replace('CRV', 'SUV')
car_data = car_data.replace(['SUV', 'CROSSOVER'], 'SUV/CROSSOVER')
car_data = car_data.replace()
car_data = car_data.replace('AFORDABLE ENERGY SAVING CARS 4X2', 'LCGC')

features_drop = ['TANK\nCAPT', 'GVW\n(Kg)','W HEEL & TYRE SIZE', 'W HEEL BASE', 'DIMENSION\nP x L xT','SEATER', 'DRIVE SYS.', 'Unnamed: 16','DOOR','W HEELS','Unnamed: 34']
for col in features_drop :
  car_data = car_data.drop(col, axis = 1)
car_data

car_data['MAR'].replace('8-', 8, inplace = True)
features = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL','AUG', 'SEP', 'OCT', 'NOV', 'DEC']
for col in features:
  car_data[col].fillna(0, inplace = True)
  car_data[col].astype(int)
car_data

def null_percentage(data):
  total = data.isnull().sum().sort_values(ascending = False)
  total = total[total != 0]
  percent = round(100 * total/len(data),2)
  return pd.concat([total,percent], axis = 1, keys = ['Total Null', 'Percent'])


null_percentage(car_data)

"""## Analisis Top Brand"""

car_data['Total'] = car_data[['JAN', 'FEB', 'MAR','APR', 'MAY', 'JUN','JUL', 'AUG', 'SEP','OCT','NOV','DEC']].sum(axis = 1)
pd.set_option('display.max_columns',90)
car_data

brand_sales = car_data.pivot_table(values = 'Total', index = 'BRAND', aggfunc = 'sum')
brand_sales.sort_values(by='Total', ascending = False, inplace = True)
brand_sales.reset_index(inplace = True)
brand_sales = brand_sales.head(10)

colors = ['#DC0000', '#DC0000', '#DC0000', '#E4DCCF', '#E4DCCF', '#E4DCCF', '#E4DCCF', '#E4DCCF', '#E4DCCF', '#E4DCCF']
plot_10_sales_brand =px.bar(brand_sales, x = 'BRAND', y = 'Total', color = 'BRAND', color_discrete_sequence = colors)
plot_10_sales_brand.update_yaxes(title = 'Sales', title_font = dict(size = 14, color = 'white', family = 'arial'))
plot_10_sales_brand.update_xaxes(title = 'Sumber data : Wholesales Gaikindo')


"""## Analisis Category"""
data_pie = car_data.loc[car_data['CATEGORY'].isin(['MPV','SUV/CROSSOVER', 'LCGC', 'HATCHBACK','DOUBLE CABIN','SEDAN'])]
category_sales = data_pie.pivot_table(values = 'Total', index = 'CATEGORY', aggfunc = 'sum')
category_sales.sort_values(by = 'Total', ascending = False, inplace = True)
category_sales = category_sales.head(5)

color_pie = ['#0079FF','#00DFA2','#F6FA70','#FF0060','#E55807']
plot_sales_category = px.pie(category_sales, 
                             values = 'Total',
                             names = category_sales.index,
                             color = category_sales.index,
                             color_discrete_sequence=color_pie, 
                             hole = 0.5)
plot_sales_category.update_traces(textposition = 'outside',textfont = dict(color = 'white', size = 13), textinfo = "label+percent", pull = [0.2,0,0,0,0])
plot_sales_category.add_annotation(text = "<b>Sales by Category<b>", showarrow = False,font = dict(size = 14, color = 'white'))
plot_sales_category.update_xaxes(title = 'Sumber data : Wholesales Gaikindo')


"""##Analisis Category Top Brand"""

category_sales = car_data.pivot_table(values = 'Total', index = 'CATEGORY', aggfunc = 'sum')
category_sales.sort_values(by = 'Total', ascending = False, inplace = True)
category_sales = category_sales.head(5)

top_brand_category = car_data.groupby(['BRAND', 'CATEGORY'])['Total'].sum().reset_index()
top_brand_category = top_brand_category.loc[top_brand_category['BRAND'].isin(['TOYOTA','DAIHATSU','HONDA', 'MITSUBISHI MOTORS'])]
top_brand_category = top_brand_category.loc[top_brand_category['CATEGORY'].isin(['MPV','SUV/CROSSOVER', 'LCGC', 'HATCHBACK','DOUBLE CABIN','SEDAN'])]
top_brand_category.sort_values(['BRAND', 'Total','CATEGORY'], ascending = False, inplace = True)

plot_top_brand_category = px.bar(top_brand_category, x = 'BRAND', y = 'Total', color = 'CATEGORY')
plot_top_brand_category.update_yaxes(title = 'Sales', title_font = dict(color = 'white', size = 13, family = 'arial'))
plot_top_brand_category.update_xaxes(title = 'Sumber data : Wholesales Gaikindo')


lineup_brand_category = car_data.groupby(['BRAND', 'CATEGORY'])['TYPE MODEL'].count().reset_index()
lineup_brand_category = lineup_brand_category.loc[lineup_brand_category['BRAND'].isin(['TOYOTA','DAIHATSU','HONDA', 'MITSUBISHI MOTORS'])]
lineup_brand_category = lineup_brand_category.loc[lineup_brand_category['CATEGORY'].isin(['MPV','SUV/CROSSOVER', 'LCGC', 'HATCHBACK','DOUBLE CABIN','SEDAN'])]
lineup_brand_category.sort_values(['BRAND', 'TYPE MODEL','CATEGORY'], ascending = False, inplace = True)

plot_lineup_brand_category = px.bar(lineup_brand_category, x = 'BRAND', y = 'TYPE MODEL', color = 'CATEGORY')
plot_lineup_brand_category.update_yaxes(title = 'Count Model', title_font = dict(size = 13, family = 'arial'))
plot_lineup_brand_category.update_xaxes(title = 'Sumber data : Wholesales Gaikindo')


"""## Analisis Top Car in Top Brand

"""

#sales_top_brand = car_data.groupby(['BRAND', 'CATEGORY', 'TYPE MODEL','TAHUN'])['Total'].sum().reset_index()
#sales_top_brand = sales_top_brand.loc[sales_top_brand['BRAND'].isin(['TOYOTA','DAIHATSU','HONDA', 'MITSUBISHI MOTORS'])]
#sales_top_brand.sort_values('Total', ascending = False)

sales_top_brand = pd.melt(car_data, id_vars = ['BRAND', 'TYPE MODEL', 'TAHUN', 'CATEGORY', 'CC', 'TRANS', 'FUEL',
       'GEAR RATIO', 'PS / HP', 'SPEED', 'CBU / CKD', 'ORIGIN\nCOUNTRY'],
       value_vars = ['JAN','FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV',
       'DEC'], 
       var_name = 'Bulan',
       value_name = 'Sales')
sales_top_brand['Tanggal'] = sales_top_brand['Bulan'] + ' ' + sales_top_brand['TAHUN'].astype(str)
sales_top_brand['Tanggal'] = sales_top_brand['TAHUN'].astype(str) + '-' + sales_top_brand['Bulan']
sales_top_brand.drop(['Bulan'],axis =1, inplace = True)

data = sales_top_brand
data= data.replace('HYBRI', 'HYBRID')
data= data.replace('ELECTRI', 'ELECTRIC')
data= data.replace('ELECTRIC', 'EV')
data.rename(columns = {'TYPE MODEL' : 'TYPE_MODEL'}, inplace = True)

import re
import pandas as pd

patterns = r'avanza|xenia|sirion|civic|city|86|rush|agya|ayla|cr-v|corolla|jazz|innova|terios|veloz|alphard|br-v|brio rs|brio satya|c+pod|c-hr|calya|corolla cross|century|crow|sigra|gran max|camry|inova|yaris|bz4x|coms|dyna|eclipse|fortuner|pajero|hi-axe|hilux|l300|land cruiser|limo|luxio|mobilio|accord|mirage|minicab|odyssey|outlander|prius|raize|rocky|sienta|sigra|t-120ss|triton|xpander|wr-v|C+POD|delica|hi-ace|hr-v|himax|Vellflre|vios|voxy|supra'


# Membuat kolom baru 'kategori' berdasarkan grup
data['Name'] = data['TYPE_MODEL'].apply(lambda x: re.search(patterns, x, re.IGNORECASE).group(0).lower() if re.search(patterns, x, re.IGNORECASE) else None)

data.loc[data['TYPE_MODEL'] == 'C+POD EV', 'Name'] = 'C+POD EV'


data.replace(['sirion', 'ayla', 'sigra', 'xenia', 'gran max', 'himax', 'terios',
       'rocky', 'luxio', 'jazz', 'brio rs', 'city', 'civic', 'brio satya',
       'mobilio', 'odyssey', 'accord', 'cr-v', 'br-v', 'hr-v', 'wr-v',
       'triton', 'mirage', 'minicab', 'xpander', 'l300', 't-120ss',
       'eclipse', 'outlander', 'pajero', 'delica', 'dyna', 'hilux',
       'yaris', 'bz4x', 'C+POD EV', 'agya', 'calya', 'avanza', 'innova',
       'inova', 'veloz', 'alphard', 'sienta', 'vellflre', 'voxy', '86',
       'camry', 'corolla', 'century', 'crow', 'limo', 'prius', 'supra',
       'vios', 'rush', 'c-hr', 'coms', 'fortuner', 'hi-ace',
       'land cruiser', 'raize'],
        ['Sirion', 'Ayla', 'Sigra', 'Xenia', 'Gran Max', 'Himax', 'Terios',
       'Rocky', 'Luxio', 'Jazz', 'Brio RS', 'Honda City', 'Honda Civic', 'Brio Satya',
       'Mobilio', 'Odyssey', 'Accord', 'CR-V', 'BR-V', 'HR-V', 'WR-V',
       'Triton', 'Mirage', 'Minicab', 'Xpander', 'L300', 'T-120ss',
       'Eclipse', 'Outlander', 'Pajero', 'Delica', 'Dyna', 'Hilux',
       'Yaris', 'Bz4x', 'C+POD EV', 'Agya', 'Calya', 'Avanza', 'Innova',
       'Innova', 'Veloz', 'Alphard', 'Sienta', 'Vellflre', 'Voxy', '86',
       'Camry', 'Corolla', 'Century', 'Crow', 'Limo', 'Prius', 'Supra',
       'Vios', 'Rush', 'CR-V', 'COMS', 'Fortuner', 'Hi-ace',
       'Land Cruiser', 'Raize'], inplace = True)

conn = sqlite3.connect('database_capstone_project')
data.to_sql('data', conn, if_exists = 'replace', index = False)
query_lcgc = '''
        SELECT 
          Name,
          BRAND,
          CATEGORY,
          SUM(Sales) AS Total
        From 
          data
        WHERE CATEGORY = 'LCGC' AND BRAND IN ('TOYOTA','DAIHATSU','HONDA', 'MITSUBISHI MOTORS')
        GROUP BY Name
        ORDER BY Total DESC
        LIMIT 5
'''
query_mpv = '''
        SELECT 
          Name,
          BRAND,
          CATEGORY,
          SUM(Sales) AS Total
        From 
          data
        WHERE CATEGORY = 'MPV'AND BRAND IN ('TOYOTA','DAIHATSU','HONDA', 'MITSUBISHI MOTORS')
        GROUP BY Name
        ORDER BY Total DESC
        LIMIT 5
'''
query_hatcback = '''
        SELECT 
          Name,
          BRAND,
          CATEGORY,
          SUM(Sales) AS Total
        From 
          data
        WHERE CATEGORY = 'HATCHBACK'AND BRAND IN ('TOYOTA','DAIHATSU','HONDA', 'MITSUBISHI MOTORS')
        GROUP BY Name
        ORDER BY Total DESC
        LIMIT 5
'''
query_suv_crossover = '''
        SELECT 
          Name,
          BRAND,
          CATEGORY,
          SUM(Sales) AS Total
        From 
          data
        WHERE CATEGORY = 'SUV/CROSSOVER'AND BRAND IN ('TOYOTA','DAIHATSU','HONDA', 'MITSUBISHI MOTORS')
        GROUP BY Name
        ORDER BY Total DESC
        LIMIT 5
'''
query_sedan = '''
        SELECT 
          Name,
          BRAND,
          CATEGORY,
          SUM(Sales) AS Total
        From 
          data
        WHERE CATEGORY = 'SEDAN' AND BRAND IN ('TOYOTA','DAIHATSU','HONDA', 'MITSUBISHI MOTORS')
        GROUP BY Name
        ORDER BY Total DESC
        LIMIT 5
'''
query_double_cabin = '''
        SELECT 
          Name,
          BRAND,
          CATEGORY,
          SUM(Sales) AS Total
        From 
          data
        WHERE CATEGORY = 'DOUBLE CABIN' AND BRAND IN ('TOYOTA','DAIHATSU','HONDA', 'MITSUBISHI MOTORS')
        GROUP BY Name
        ORDER BY Total DESC
        LIMIT 5
'''
top_car_mpv = pd.read_sql_query(query_mpv,conn)
top_car_double_cabin = pd.read_sql_query(query_double_cabin,conn)
top_car_lcgc = pd.read_sql_query(query_lcgc,conn)
top_car_sedan = pd.read_sql_query(query_sedan,conn)
top_car_hatchback = pd.read_sql_query(query_hatcback,conn)
top_car_suv_crossover = pd.read_sql_query(query_suv_crossover, conn)

top_car_mpv.to_sql('top_car_mpv', conn, if_exists = 'replace', index = False)
top_car_double_cabin.to_sql('top_car_double_cabin', conn, if_exists = 'replace', index = False)
top_car_lcgc.to_sql('top_car_lcgc', conn, if_exists = 'replace', index = False)
top_car_sedan.to_sql('top_car_sedan', conn, if_exists = 'replace', index = False)
top_car_hatchback.to_sql('top_car_hatchback', conn, if_exists = 'replace', index = False)
top_car_suv_crossover.to_sql('top_car_suv_crossover', conn, if_exists = 'replace', index = False)



def plot_top_car_by_category(conn, query):
  data = pd.read_sql_query(query, conn)
  
  fig = px.bar(data, x = 'Total', y = 'Name', color = 'Name')
  fig.update_xaxes(title = 'Sumber data : Wholesales Gaikindo')
  
  return(fig)

plot_top_car_by_category_double_cabin =plot_top_car_by_category(conn,query_double_cabin)
plot_top_car_by_category_lcgc=plot_top_car_by_category(conn, query_lcgc)
plot_top_car_by_category_mpv=plot_top_car_by_category(conn, query_mpv)
plot_top_car_by_category_sedan=plot_top_car_by_category(conn, query_sedan)
plot_top_car_by_category_hatchback=plot_top_car_by_category(conn, query_hatcback)
plot_top_car_by_category_suv_crossover=plot_top_car_by_category(conn, query_suv_crossover)

query_line_mpv = '''
        SELECT 
          Name,
          BRAND,
          CATEGORY,
          TAHUN,
          SUM(Sales) as Sales
        FROM 
          data
        WHERE CATEGORY = 'MPV' AND Name IN (SELECT DISTINCT
          Name
        From 
          top_car_mpv)
        GROUP BY 
          Name, TAHUN
'''
query_line_sedan = '''
        SELECT 
          Name,
          BRAND,
          CATEGORY,
          TAHUN,
          SUM(Sales) as Sales
        FROM 
          data
        WHERE CATEGORY = 'SEDAN' AND Name IN  (SELECT DISTINCT
          Name
        From 
          top_car_sedan)
        GROUP BY 
          Name, TAHUN
'''
query_line_suv_crossover = '''
        SELECT 
          Name,
          BRAND,
          CATEGORY,
          TAHUN,
          SUM(Sales) as Sales
        FROM 
          data
        WHERE CATEGORY = 'SUV/CROSSOVER' AND Name IN (SELECT DISTINCT
          Name
        From 
          top_car_suv_crossover)
        GROUP BY 
          Name, TAHUN
'''
query_line_hatchback = '''
        SELECT 
          Name,
          BRAND,
          CATEGORY,
          TAHUN,
          SUM(Sales) as Sales
        FROM 
          data
        WHERE CATEGORY = 'HATCHBACK' AND Name IN (SELECT DISTINCT
          Name
        From 
          top_car_hatchback)
        GROUP BY 
          Name, TAHUN
'''
query_line_double_cabin = '''
        SELECT 
          Name,
          BRAND,
          CATEGORY,
          TAHUN,
          SUM(Sales) as Sales
        FROM 
          data
        WHERE CATEGORY = 'DOUBLE CABIN' AND Name IN (SELECT DISTINCT
          Name
        From 
          top_car_double_cabin)
        GROUP BY 
          Name, TAHUN
'''
query_line_lcgc = '''
        SELECT 
          Name,
          BRAND,
          CATEGORY,
          TAHUN,
          SUM(Sales) as Sales
        FROM 
          data
        WHERE CATEGORY = 'LCGC' AND Name IN (SELECT DISTINCT
          Name
        From 
          top_car_lcgc)
        GROUP BY 
          Name, TAHUN
'''

def line_top_car(query, conn):
  data = pd.read_sql_query(query, conn)
  data['TAHUN'] = data['TAHUN'].astype(str)
  data.sort_values(by=['TAHUN', 'Sales'], ascending=[True, False], inplace=True)
  fig = px.line(data, x = 'TAHUN', y='Sales', color = 'Name', markers = True)
  fig.update_layout(xaxis= {'type': 'category', 'categoryorder' : 'array', 'categoryarray' : data['TAHUN']})
  fig.update_xaxes(title = 'Sumber data : Wholesales Gaikindo')

  return fig

plot_line_top_car_mpv=line_top_car(query_line_mpv,conn)
plot_line_top_car_sedan=line_top_car(query_line_sedan,conn)
plot_line_top_car_lcgc = line_top_car(query_line_lcgc,conn)
plot_line_top_car_suv_crossover = line_top_car(query_line_suv_crossover,conn)
plot_line_top_car_hatchback = line_top_car(query_line_hatchback,conn)
plot_line_top_car_double_cabin = line_top_car(query_line_double_cabin, conn)

"""## Analisist Perkembangan Sales by Category"""

data['Sales'] = data['Sales'].astype(int)
data['Sales'] = data['Sales'].replace(-99, 99)
data['Sales'] = data['Sales'].replace(-85, 85)
data['Sales'] = data['Sales'].replace(-70, 70)
data['Sales'] = data['Sales'].replace(-55, 5)
data['Sales'] = data['Sales'].replace(-41, 41)
data['Sales'] = data['Sales'].replace(-2, 2) 
data['Sales'] = data['Sales'].replace(-1, 1)
data = data.replace(-9,9)

query_category = '''
      SELECT 
        Name,
        BRAND,
        CATEGORY,
        SUM(Sales) AS Sales,
        TAHUN
      FROM
        data
      WHERE CATEGORY IN ('LCGC', 'MPV', 'SUV/CROSSOVER', 'HATCHBACK', 'DOUBLE CABIN', 'SEDAN')
      GROUP BY
        CATEGORY,TAHUN
      ORDER BY 
        Sales DESC, TAHUN ASC
'''
data_category = pd.read_sql_query(query_category, conn)
data_area_category = data_category
data_area_category['TAHUN'] = data_area_category['TAHUN'].astype(str)
data_area_category.sort_values(by=['TAHUN', 'Sales'], ascending=[True, False], inplace=True)


import plotly.express as px

category_area = px.area(data_category, x='TAHUN', y="Sales", color="CATEGORY")
#category_area.update_layout(xaxis= {'type': 'category'})
category_area.update_layout(xaxis={'type': 'category', 'categoryorder': 'array', 'categoryarray': data_area_category['TAHUN']})
category_area.update_xaxes(title = 'Sumber data : Wholesales Gaikindo')
category_area.update_yaxes(title = 'Sales')


"""#Analisis Speed CC """

data['SPEED'] = data['SPEED'].fillna(0)
data['SPEED'] = data['SPEED'].astype(float)

data['SPEED'].unique()
data['SPEED'] = data['SPEED'].replace('240.', 240)
data['SPEED'] = data['SPEED'].replace('240.', 240)
data['SPEED'] = data['SPEED'].replace('240.', 240)
data['SPEED'] = data['SPEED'].replace('240.', 240)
data['SPEED'] = data['SPEED'].replace('240.', 240)
data_speed = [ 0. , 240. , 250. ,   6. ,   8. ,  10. , 225. , 140. , 155. ,
         4. ,   5. , 177. , 193. , 180. , 200. ,   7. , 170. , 222. ,
       230. , 116. , 100. , 112. , 104.6, 126. , 115. , 105. , 119. ,
       110. , 120. ,  60. ,  12. , 165. , 125. ,  70. ,  50. , 160. ,
       124. , 103. ,  97. ,  90. ,  95. , 107. , 102. ,  94. , 113. ,
       104. , 109. ,  98. ,  96. ,  80. ,  93. ,  76. , 106. ,  87. ,
        86. ,  88. ,  99. ,  75. ,  83. ,  89. ,  85. ,   9. ,  66. ,
       226. ,  84. , 241. , 118. ]

data_speed_replace = [ 0, 240, 250,   100,   100 ,  100 , 225, 140, 155,
         40,   50, 177, 193, 180, 200,   70, 170, 222,
       230, 116, 100, 112, 104, 126, 115, 105, 119,
       110, 120,  60,  12, 165, 125,  70,  50, 160,
       124, 103,  97,  90,  95, 107, 102,  94, 113,
       104, 109,  98,  96,  80,  93,  76, 106,  87,
        86,  88,  99,  75,  83,  89,  85,   90,  66,
       226,  84, 241, 118]
mapping = dict(zip(data_speed, data_speed_replace))
data['SPEED'] = data['SPEED'].replace(mapping)

scatter_speed_cc = px.scatter(data, x="SPEED", y="CC", animation_frame="Tanggal",
          color="CATEGORY", size = 'Sales', size_max = 55, range_x = [50,250], range_y= [0,10000],
           log_x=True,)
scatter_speed_cc.update_xaxes(title = 'Sumber data : Wholesales Gaikindo')


#fig["layout"].pop("updatemenus") # optional, drop animation buttons


"""## Analisis Perkembangan Mobil Listrik"""

data= data.replace('HYBRI', 'HYBRID')
data= data.replace('ELECTRI', 'ELECTRIC')
data= data.replace('ELECTRI', 'EV')


data['FUEL'].unique()

query_electric = '''
        SELECT
          SUM(Sales) as Sales,
          FUEL,
          TAHUN
        FROM 
          data
        WHERE 
          FUEL IN ('HYBRID', 'EV', 'PHEV')
        GROUP BY
          FUEL, TAHUN
      ORDER BY TAHUN ASC

'''
car_electric = pd.read_sql_query(query_electric, conn)
car_electric['TAHUN'] = car_electric['TAHUN'].astype(str)
car_electric.sort_values(['TAHUN', 'Sales'], ascending = [True, False], inplace = True)


import plotly.express as px

plot_electric = px.area(car_electric, x="TAHUN", y="Sales", color="FUEL", markers = True)
plot_electric.update_layout(xaxis={'type': 'category', 'categoryorder': 'array', 'categoryarray': car_electric['TAHUN']})
plot_electric.update_xaxes(title = 'Sumber data : Wholesales Gaikindo')



"""#Analisis Sales Car, Motorcycle, IPR"""

data_sales_car = data.dropna().groupby('Tanggal')['Sales'].sum().reset_index(name = 'Sales')
data_sales_car.sort_values('Tanggal', ascending =True, inplace = True)

data_sales_car.sort_values('Tanggal', ascending =True, inplace = True)
data_sales_car['Tanggal'] = pd.to_datetime(data_sales_car['Tanggal'], format = '%Y-%b')
motorcycle_data.sort_values('Tanggal', ascending = True, inplace = True)
data_ipr.sort_values('date', ascending = True, inplace = True)
data_ipr = data_ipr.rename(columns = {'Indeks Penjualan Riil (IPR)': 'Indeks_Penjualan_Riil'})

data_sales_car.to_sql('data_sales_car', conn, if_exists = 'replace', index = False)
motorcycle_data.to_sql('motorcycle_data', conn, if_exists = 'replace', index = False)
data_ipr.to_sql('data_ipr', conn, if_exists = 'replace', index = False)

query_sales = '''
      SELECT
        di.date AS Tanggal,
        di.Indeks_Penjualan_Riil, 
        dc.Sales AS Sales_Car,
        dm.Jumlah AS Sales_Motorcycle
      FROM
        data_ipr AS di
      LEFT JOIN 
        data_sales_car AS dc
      ON 
        di.date = dc.Tanggal
      LEFT JOIN 
        motorcycle_data AS dm
      ON 
        di.date = dm.Tanggal
      ORDER BY Tanggal ASC

'''
data_sales = pd.read_sql_query(query_sales, conn)
data_sales

numerical_features = ['Sales_Car', 'Sales_Motorcycle', 'Indeks_Penjualan_Riil']


for col in numerical_features:
  scaler = MinMaxScaler()
  data_sales[col] = scaler.fit_transform(data_sales[[col]])

data_sales

import plotly.express as px
import plotly.graph_objects as go

sales = go.Figure()
sales.add_trace(go.Scatter(go.Scatter(x=data_sales['Tanggal'], y=data_sales['Sales_Car'],
                    mode='lines+markers',
                    name='Car Sales')))
sales.add_trace(go.Scatter(x=data_sales['Tanggal'], y=data_sales['Sales_Motorcycle'],
                    mode='lines+markers',
                    name='Motorcycle Sales'))
sales.add_trace(go.Scatter(go.Scatter(x=data_sales['Tanggal'], y=data_sales['Indeks_Penjualan_Riil'],
                    mode='lines+markers',
                    name='Indeks Penjualan Riil (IPR)')))
sales.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='white',
        linewidth=2
    ),
    yaxis=dict(
        title_text='Nilai',
        titlefont=dict(
            family='Rockwell',
            size=26,
            color='white',
        ),
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='white',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Rockwell',
            size=26,
            color='white',
        ),
    ),
    showlegend=True,
    template = 'plotly_white'

)

annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.07, y=0.4,
                              xanchor='left', yanchor='bottom',
                              text='Mei - Juni 2019 Penjualan mobil <br>dan IPR sama - sama turun',
                              font=dict(family='Rockwell',
                                        size=12,
                                        color='white'),
                              showarrow=False))

annotations.append(dict(xref='paper', yref='paper', x=0.1, y=0.1,
                              xanchor='left', yanchor='bottom',
                              text='April - Mei 2020 Penjualan motor <br>dan IPR naik, sedangkan mobil menurun',
                              font=dict(family='Rockwell',
                                        size=12,
                                        color='white'),
                              showarrow=False))

annotations.append(dict(xref='paper', yref='paper', x=0.4, y=0.85,
                              xanchor='left', yanchor='bottom',
                              text='April - Mei 2021 Penjualan motor <br>dan mobil turun, sedangkan IPR naik',
                              font=dict(family='Rockwell',
                                        size=12,
                                        color='white'),
                              showarrow=False))

annotations.append(dict(xref='paper', yref='paper', x=0.65, y=0.85,
                              xanchor='left', yanchor='bottom',
                              text='April - Mei 2022 Penjualan motor, <br>mobil, dan IPR sama-sama turun',
                              font=dict(family='Rockwell',
                                        size=12,
                                        color='white'),
                              showarrow=False))

sales.update_layout(annotations=annotations)
sales.update_xaxes(title = 'Sumber data : Wholesales Gaikindo, Databooks, Asosiasi Industri Sepeda Motor Indonesia')
