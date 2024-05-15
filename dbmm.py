#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import os 
import matplotlib.pyplot as plt


# In[ ]:


df1 = pd.read_csv('AKULAKU_FEB.csv')
df2 = pd.read_csv('ALLSEDAYU_FEB.csv')
df3 = pd.read_csv('ARGAPURA2_FEB.csv')
df4 = pd.read_csv('ARWANACITRA_FEB.csv')
df5 = pd.read_csv('ASURANSIJIWAALAMIN_FEB.csv')
df6 = pd.read_csv('AXA4_FEB.csv')
df7 = pd.read_csv('AXAKUNINGAN1_FEB.csv')
df8 = pd.read_csv('AXAKUNINGAN2_FEB.csv')
df9 = pd.read_csv('AXAKUNINGAN3_FEB.csv')
df10 = pd.read_csv('BAKRIEANDBROTHERLT27_FEB.csv')
df11 = pd.read_csv('BNIRAWAMANGUN_FEB.csv')
df12 = pd.read_csv('CBCGALLERY_FEB.csv')
df13 = pd.read_csv('CLUSTERATHALIA1_FEB.csv')
df14 = pd.read_csv('CLUSTERATHALIA2_FEB.csv')
df15 = pd.read_csv('CLUSTERBLUERIVER2_FEB.csv')
df16 = pd.read_csv('CVJAYAABADI3_FEB.csv')
df17 = pd.read_csv('DIGNITASACADEMY_FEB.csv')
df18 = pd.read_csv('GRAHAELNUSA_FEB.csv')
df19 = pd.read_csv('GRIYAPATRIAGUESTHOUSE_FEB.csv')
df20 = pd.read_csv('HALIM_FEB.csv')
df21 = pd.read_csv('HONDAMTHARYONO_FEB.csv')
df22 = pd.read_csv('HOTEL101_FEB.csv')
df23 = pd.read_csv('HOTELHERMITAGE_FEB.csv')
df24 = pd.read_csv('HOTELHILTON_FEB.csv')
df25 = pd.read_csv('HOTELKEMPINSKI1_FEB.csv')
df26 = pd.read_csv('HOTELMERCURE_FEB.csv')
df27 = pd.read_csv('HOTELPARKHYATT_FEB.csv')
df28 = pd.read_csv('HOTELWYNDHAM_FEB.csv')
df29 = pd.read_csv('INDOCEMENT_FEB.csv')
df30 = pd.read_csv('INDOCEMENT2_FEB.csv')
df31 = pd.read_csv('INDOCEMENT3_FEB.csv')
df32 = pd.read_csv('INDOCEMENT4_FEB.csv')
df33 = pd.read_csv('INDOCEMENT5_FEB.csv')
df34 = pd.read_csv('INDOCEMENT6_FEB.csv')
df35 = pd.read_csv('INDOCEMENT7_FEB.csv')
df36 = pd.read_csv('INDOCEMENT8_FEB.csv')
df37 = pd.read_csv('INDOCEMENT10_FEB.csv')
df38 = pd.read_csv('JHLSOLITAIRE_FEB.csv')
df39 = pd.read_csv('KENGSINGTONOFFICETOWER_FEB.csv')
df40 = pd.read_csv('KLINIKLALITABEKASI_FEB.csv')
df41 = pd.read_csv('LABSCHOOL1_FEB.csv')
df42 = pd.read_csv('LABSCHOOL2_FEB.csv')
df43 = pd.read_csv('LIONVILLAGE1_FEB.csv')
df44 = pd.read_csv('LIONVILLAGE2_FEB.csv')
df45 = pd.read_csv('LIPPOTOWERHOLLAND_FEB.csv')
df46 = pd.read_csv('LIPPOTOWERHOLLAND2_FEB.csv')
df47 = pd.read_csv('LIPPOTOWERHOLLAND3_FEB.csv')
df48 = pd.read_csv('MANULIFE1_FEB.csv')
df49 = pd.read_csv('MANULIFE2_FEB.csv')
df50 = pd.read_csv('MASJIDALAZHARBEKASI1_FEB.csv')
df51 = pd.read_csv('MASJIDATTAIBIN_FEB.csv')
df52 = pd.read_csv('MENARATHAMRIN_FEB.csv')
df53 = pd.read_csv('MONSTERMART_FEB.csv')
df54 = pd.read_csv('NEOSOHO_FEB.csv')
df55 = pd.read_csv('NINERESIDENCE_FEB.csv')
df56 = pd.read_csv('PADINASOHO_FEB.csv')
df57 = pd.read_csv('PTBAKER&HUGHES_FEB.csv')
df58 = pd.read_csv('PTBASF_FEB.csv')
df59 = pd.read_csv('PTCCIE(INDOCEMENT11)_FEB.csv')
df60 = pd.read_csv('PTINDOCEMENT9(GEDUNGGMO)_FEB.csv')
df61 = pd.read_csv('PTMATRARODAPIRANTI1_FEB.csv')
df62 = pd.read_csv('PTMATRARODAPIRANTI2_FEB.csv')
df63 = pd.read_csv('PTMATRARODAPIRANTI3_FEB.csv')
df64 = pd.read_csv('PTSINERGI_FEB.csv')
df65 = pd.read_csv('PTTIMERINDO_FEB.csv')
df66 = pd.read_csv('PTTOACOATING1_FEB.csv')
df67 = pd.read_csv('PULOMAS1_FEB.csv')
df68 = pd.read_csv('PULOMAS2_FEB.csv')
df69 = pd.read_csv('PULOMAS4_FEB.csv')
df70 = pd.read_csv('REGALSTUDIO_FEB.csv')
df71 = pd.read_csv('ROYALENFIELDANTASARI_FEB.csv')
df72 = pd.read_csv('RSCM1_FEB.csv')
df73 = pd.read_csv('RSCM2_FEB.csv')
df74 = pd.read_csv('RSCM3_FEB.csv')
df75 = pd.read_csv('RSCM4_FEB.csv')
df76 = pd.read_csv('RSDINDA_FEB.csv')
df77 = pd.read_csv('RSIAPRATIWI_FEB.csv')
df78 = pd.read_csv('RSJAKARTA2_FEB.csv')
df79 = pd.read_csv('RSJAKARTA3_FEB.csv')
df80 = pd.read_csv('RSUIFARMASI_FEB.csv')
df81 = pd.read_csv('RSUIIGD_FEB.csv')
df82 = pd.read_csv('RSUILOBBY_FEB.csv')
df83 = pd.read_csv('RSUILT5_FEB.csv')
df84 = pd.read_csv('SEKOLAHALAZHARGRANDWISATABEKASI_FEB.csv')
df85 = pd.read_csv('SAMSUNGKUNINGAN1_FEB.csv')
df86 = pd.read_csv('SAMSUNGKUNINGAN2_FEB.csv')
df87 = pd.read_csv('SEKOLAHBSP_FEB.csv')
df88 = pd.read_csv('SENTRATIMUR1_FEB.csv')
df89 = pd.read_csv('SENTRATIMUR2_FEB.csv')
df90 = pd.read_csv('SEKOLAHFAJAR_FEB.csv')
df91 = pd.read_csv('SMARTHAPPYKIDS_FEB.csv')
df92 = pd.read_csv('SMKTELKOM_FEB.csv')
df93 = pd.read_csv('STREGIST1_FEB.csv')
df94 = pd.read_csv('STREGIST2_FEB.csv')
df95 = pd.read_csv('UNIPREPBSD1_FEB.csv')
df96 = pd.read_csv('UNIPREPBSD2_FEB.csv')
df97 = pd.read_csv('UNIPREPKELAPAGADING_FEB.csv')
df98 = pd.read_csv('UNIPREPPONDOKINDAH_FEB.csv')
df99 = pd.read_csv('UNIVBAKRIE1_FEB.csv')
df100 = pd.read_csv('UNIVBAKRIE2_FEB.csv')
df101 = pd.read_csv('UNIVBAKRIE3_FEB.csv')
df102 = pd.read_csv('UNIVERSALLUGAGE1_FEB.csv')
df103 = pd.read_csv('UNIVERSALLUGAGE2_FEB.csv')
df104 = pd.read_csv('UNIVERSITASPANCASILA_FEB.csv')
data = pd.read_csv('dfcombined.csv')


# In[ ]:


combined = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36,df37,df38,df39,df40,df41,df42,df43,df44,df45,df46,df47,df48,df49,df50,df51,df52,df53,df54,df55,df56,df57,df58,df59,df60,df61,df62,df63,df64,df65,df66,df67,df68,df69,df70,df71,df72,df73,df74,df75,df76,df77,df78,df79,df80,df81,df82,df83,df84,df85,df86,df87,df88,df89,df90,df91,df92,df93,df94,df95,df96,df97,df98,df99,df100,df101,df102,df103,df104], ignore_index=True)


# In[ ]:


combined.to_csv('combined.csv', index=False)


# In[ ]:


selected_option = st.selectbox('Select Vending Machine', list(options.keys()))

   df = pd.read_csv(options[selected_option])
   df_sorted = df.sort_values(by="Qty Sold", ascending=False)
   top_10 = df_sorted.head(10)
   st.subheader('Top 10 Quantities Sold')
   st.write(top_10)

   st.title('Product Sales Time Series')

   df_combined = pd.read_csv('dfcombined.csv')  
   df_combined['Transaction'] = pd.to_datetime(df_combined['Transaction'])
   products = df_combined['Product'].unique()
   selected_product = st.selectbox('Select Product', products)
   filtered_df = df_combined[df_combined['Product'] == selected_product]

   st.write(f"### Sales Time Series for {selected_product}")
   fig, ax = plt.subplots(figsize=(10, 6))
   filtered_df.set_index('Transaction').resample('D').size().plot(ax=ax) 
   plt.xlabel('Date')
   plt.ylabel('Number of Sales')
   plt.title('Product Sales Time Series')
   plt.grid(True)
   st.pyplot(fig)

   products_list = {'Kaki Tiga Larutan Leci 320ml','Pocari Sweat 350ml','Milo RTD 240ml','Tic Tac Ori 90gr','Tic Tac Sapi Panggang 90gr','Sukro Oven 38gr','Coca Cola Kaleng','Sprite Kaleng','Fanta STR Kaleng','AW Can 250ml','Sedap Mie Goreng 85gr','Sedap Mie Kari Spesial 81gr','Sedaap Rawit Bingit','Sedaap Korean Spicy','Sedaap Soto','Milku Cokelat 200ml','Milku Strawberry 200ml','Teh Pucuk 350ml','Kopiko Lucky Day','Im Coco Lychee 350ml','Inaco Mini Jelly','Inaco Mini Pudding','5 Day Chocolate Croissant','Cimory Susu UHT 250ml Chocolate','Cimory Susu UHT 250ml Stroberi','Cimory Susu UHT 250ml Matcha','Cimory Susu UHT 250ml Marie Regal','Cimory Susu UHT 250ml Almond','Pokka Leci Tea 450ml','Pokka Lemon Tea','You C1000 Orange Water 500ml','Monde Serena Snack Gold 30gr','Monde Egg Roll Chocolate','Monde Egg Roll Cheese','Wallens Chocoshoes','Kusuka Ayam Madu','Nescafe Black','Nescafe Capucino','Sunkist Lemon','Sunkist Orange Water','Krizzi Chocolate','Hydrococo 250ml','Lasegar Leci','Lasegar Lemon','Caffino','Aqua','Mayasi Paw','Brotatoz Rumput Laut','Brotatoz Rendang','Brotatoz Korea','Pulpy Orange','Qtela Tempe Original','PotatoQ Sosis Mexico','PotatoQ Rumput Laut','Yoritos Ayam Bakar','Taro BBQ','Teh Sejuk','Twistko','Potatokrez Sapi Panggang','Potatokrez ayam geprek','Spix Mie Goreng','Fire Crackers Ayam Bawang','Fire Crackers Sambal Mangga','Mayasi Kacang Rasa Sapi Panggang','Indosnack Potato Chips'}

   selected_products = st.selectbox('Select Product for Restock', products_list)

   stock_needed = pd.read_csv('stockneededfeb.csv') 
   stock_needed_sorted = stock_needed.sort_values(by='Stock Qty Needed', ascending=False)
   last_10 = stock_needed_sorted.head(10)
   st.subheader('Needs Restock')
   st.write(last_10)

if __name__ == "__main__":
   main()

