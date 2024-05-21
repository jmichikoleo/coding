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
alldata = pd.read_csv('combined.csv')


# In[ ]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

def main():
    st.title('Vending Machine Top Sales')
    options = {
        'AKULAKU': 'AKULAKU_FEB.csv',
        'ALL SEDAYU': 'ALLSEDAYU_FEB.csv',
        'ARGAPURA2': 'ARGAPURA2_FEB.csv',
        'ARWANA CITRA': 'ARWANACITRA_FEB.csv',
        'ASURANSI JIWA AL AMIN': 'ASURANSIJIWAALAMIN_FEB.csv',
        'AXA 4': 'AXA4_FEB.csv',
        'AXA KUNINGAN1': 'AXAKUNINGAN1_FEB.csv',
        'AXA KUNINGAN2': 'AXAKUNINGAN2_FEB.csv',
        'AXA KUNINGAN3': 'AXAKUNINGAN3_FEB.csv',
        'BAKRIE AND BROTHER LT 27': 'BAKRIEANDBROTHERLT27_FEB.csv',
        'BNI RAWAMANGUN': 'BNIRAWAMANGUN_FEB.csv',
        'CBC GALLERY': 'CBCGALLERY_FEB.csv',
        'CLUSTER ATHALIA 1': 'CLUSTERATHALIA1_FEB.csv',
        'CLUSTER ATHALIA 2': 'CLUSTERATHALIA2_FEB.csv',
        'CLUSTER BLUE RIVER 2': 'CLUSTERBLUERIVER2_FEB.csv',
        'CV JAYA ABADI 3': 'CVJAYAABADI3_FEB.csv',
        'DIGNITAS ACADEMY': 'DIGNITASACADEMY_FEB.csv',
        'GRAHA ELNUSA': 'GRAHAELNUSA_FEB.csv',
        'GRIYA PATRIA GUEST HOUSE': 'GRIYAPATRIAGUESTHOUSE_FEB.csv',
        'HALIM': 'HALIM_FEB.csv',
        'HONDA MT HARYONO': 'HONDAMTHARYONO_FEB.csv',
        'HOTEL 101': 'HOTEL101_FEB.csv',
        'HOTEL HERMITAGE': 'HOTELHERMITAGE_FEB.csv',
        'HOTEL HILTON': 'HOTELHILTON_FEB.csv',
        'HOTEL KEMPINSKI 1': 'HOTELKEMPINSKI1_FEB.csv',
        'HOTEL MERCURE': 'HOTELMERCURE_FEB.csv',
        'HOTEL PARK HYATT': 'HOTELPARKHYATT_FEB.csv',
        'HOTEL WYNDHAM': 'HOTELWYNDHAM_FEB.csv',
        'INDOCEMENT': 'INDOCEMENT_FEB.csv',
        'INDOCEMENT 2': 'INDOCEMENT2_FEB.csv',
        'INDOCEMENT 3': 'INDOCEMENT3_FEB.csv',
        'INDOCEMENT 4': 'INDOCEMENT4_FEB.csv',
        'INDOCEMENT 5': 'INDOCEMENT5_FEB.csv',
        'INDOCEMENT 6': 'INDOCEMENT6_FEB.csv',
        'INDOCEMENT 7': 'INDOCEMENT7_FEB.csv',
        'INDOCEMENT 8': 'INDOCEMENT8_FEB.csv',
        'INDOCEMENT 10': 'INDOCEMENT10_FEB.csv',
        'JHL SOLITAIRE': 'JHLSOLITAIRE_FEB.csv',
        'KENGSINGTON OFFICE TOWER': 'KENGSINGTONOFFICETOWER_FEB.csv',
        'KLINIK LALITA BEKASI': 'KLINIKLALITABEKASI_FEB.csv',
        'LAB SCHOOL 1': 'LABSCHOOL1_FEB.csv',
        'LAB SCHOOL 2': 'LABSCHOOL2_FEB.csv',
        'LION VILLAGE 1': 'LIONVILLAGE1_FEB.csv',
        'LION VILLAGE 2': 'LIONVILLAGE2_FEB.csv',
        'LIPPO TOWER HOLLAND': 'LIPPOTOWERHOLLAND_FEB.csv',
        'LIPPO TOWER HOLLAND 2': 'LIPPOTOWERHOLLAND2_FEB.csv',
        'LIPPO TOWER HOLLAND 3': 'LIPPOTOWERHOLLAND3_FEB.csv',
        'MANULIFE 1': 'MANULIFE1_FEB.csv',
        'MANULIFE 2': 'MANULIFE2_FEB.csv',
        'MASJID AL AZHAR BEKASI': 'MASJIDALAZHARBEKASI1_FEB.csv',
        'MASJID AT TAIBIN': 'MASJIDATTAIBIN_FEB.csv',
        'MENARA THAMRIN': 'MENARATHAMRIN_FEB.csv',
        'MONSTERMART': 'MONSTERMART_FEB.csv',
        'NEOSOHO': 'NEOSOHO_FEB.csv',
        'NINE RESIDENCE': 'NINERESIDENCE_FEB.csv',
        'PADINA SOHO': 'PADINASOHO_FEB.csv',
        'PT BAKER & HUGHES': 'PTBAKER&HUGHES_FEB.csv',
        'PT BASF': 'PTBASF_FEB.csv',
        'PT CCIE (INDOCEMENT11)': 'PTCCIE(INDOCEMENT11)_FEB.csv',
        'PT MATRA RODA PIRANTI 1': 'PTMATRARODAPIRANTI1_FEB.csv',
        'PT MATRA RODA PIRANTI 2': 'PTMATRARODAPIRANTI2_FEB.csv',
        'PT MATRA RODA PIRANTI 3': 'PTMATRARODAPIRANTI3_FEB.csv',
        'PT SINERGI': 'PTSINERGI_FEB.csv',
        'PT TIMERINDO': 'PTTIMERINDO_FEB.csv',
        'PT TOA COATING 1': 'PTTOACOATING1_FEB.csv',
        'PULOMAS 1': 'PULOMAS1_FEB.csv',
        'PULOMAS 2': 'PULOMAS2_FEB.csv',
        'PULOMAS 4': 'PULOMAS4_FEB.csv',
        'REGAL STUDIO': 'REGALSTUDIO_FEB.csv',
        'ROYAL ENFIELD ANTASARI': 'ROYALENFIELDANTASARI_FEB.csv',
        'RSCM 1': 'RSCM1_FEB.csv',
        'RSCM 2': 'RSCM2_FEB.csv',
        'RSCM 3': 'RSCM3_FEB.csv',
        'RSCM 4': 'RSCM4_FEB.csv',
        'RSDINDA': 'RSDINDA_FEB.csv',
        'RSIAPRATIWI': 'RSIAPRATIWI_FEB.csv',
        'RS JAKARTA 2': 'RSJAKARTA2_FEB.csv',
        'RS JAKARTA 3': 'RSJAKARTA3_FEB.csv',
        'RS UI FARMASI': 'RSUIFARMASI_FEB.csv',
        'RS UI IGD': 'RSUIIGD_FEB.csv',
        'RS UI LOBBY': 'RSUILOBBY_FEB.csv',
        'RSUI LT 5': 'RSUILT5_FEB.csv',
        'SEKOLAH AL AZHAR GRAND WISATA BEKASI': 'SEKOLAHALAZHARGRANDWISATABEKASI_FEB.csv',
        'SAMSUNG KUNINGAN 1': 'SAMSUNGKUNINGAN1_FEB.csv',
        'SAMSUNG KUNINGAN 2': 'SAMSUNGKUNINGAN2_FEB.csv',
        'SEKOLAH BSP': 'SEKOLAHBSP_FEB.csv',
        'SEKOLAH FAJAR': 'SEKOLAHFAJAR_FEB.csv',
        'SENTRA TIMUR 1': 'SENTRATIMUR1_FEB.csv',
        'SENTRA TIMUR 2': 'SENTRATIMUR2_FEB.csv',
        'SMART HAPPY KIDS': 'SMARTHAPPYKIDS_FEB.csv',
        'SMK TELKOM': 'SMKTELKOM_FEB.csv',
        'ST REGIST 1': 'STREGIST1_FEB.csv',
        'ST REGIST 2': 'STREGIST2_FEB.csv',
        'UNIPREP BSD 1': 'UNIPREPBSD1_FEB.csv',
        'UNIPREP BSD 2': 'UNIPREPBSD2_FEB.csv',
        'UNIPREP KELAPA GADING': 'UNIPREPKELAPAGADING_FEB.csv',
        'UNIPREP PONDOK INDAH': 'UNIPREPPONDOKINDAH_FEB.csv',
        'UNIV BAKRIE 1': 'UNIVBAKRIE1_FEB.csv',
       'UNIV BAKRIE 2': 'UNIVBAKRIE2_FEB.csv',
        'UNIV BAKRIE 3': 'UNIVBAKRIE3_FEB.csv',
        'UNIVERSAL LUGAGE 1': 'UNIVERSALLUGAGE1_FEB.csv',
        'UNIVERSAL LUGAGE 2': 'UNIVERSALLUGAGE2_FEB.csv',
        'UNIVERSITAS PANCASILA': 'UNIVERSITASPANCASILA_FEB.csv'
        'ALL DATA' : 'combined.csv'
    }
    selected_option = st.selectbox('Select Vending Machine', list(options.keys()))
    months = {'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'}
    selected_month = st.selectbox('Select Month', months)
    year = {'2024'}
    selected_year = st.selectbox('Select Year', year)

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

    st.write(f"{selected_product}")
    fig, ax = plt.subplots(figsize=(10, 6))
    filtered_df.set_index('Transaction').resample('D').size().plot(ax=ax)
    plt.xlabel('Date')
    plt.ylabel('Number of Sales')
    plt.title('Product Sales Time Series')
    plt.grid(True)
    st.pyplot(fig)

    products_list = {
        'Kaki Tiga Larutan Leci 320ml', 'Pocari Sweat 350ml', 'Milo RTD 240ml', 'Tic Tac Ori 90gr',
        'Tic Tac Sapi Panggang 90gr', 'Sukro Oven 38gr', 'Coca Cola Kaleng', 'Sprite Kaleng',
        'Fanta STR Kaleng', 'AW Can 250ml', 'Sedap Mie Goreng 85gr', 'Sedap Mie Kari Spesial 81gr',
        'Sedaap Rawit Bingit', 'Sedaap Korean Spicy', 'Sedaap Soto', 'Milku Cokelat 200ml',
        'Milku Strawberry 200ml', 'Teh Pucuk 350ml', 'Kopiko Lucky Day', 'Im Coco Lychee 350ml',
        'Inaco Mini Jelly', 'Inaco Mini Pudding', '5 Day Chocolate Croissant', 'Cimory Susu UHT 250ml Chocolate',
        'Cimory Susu UHT 250ml Stroberi', 'Cimory Susu UHT 250ml Matcha', 'Cimory Susu UHT 250ml Marie Regal',
        'Cimory Susu UHT 250ml Almond', 'Pokka Leci Tea 450ml', 'Pokka Lemon Tea', 'You C1000 Orange Water 500ml',
        'Monde Serena Snack Gold 30gr', 'Monde Egg Roll Chocolate', 'Monde Egg Roll Cheese', 'Wallens Chocoshoes',
        'Kusuka Ayam Madu', 'Nescafe Black', 'Nescafe Capucino', 'Sunkist Lemon', 'Sunkist Orange Water',
        'Krizzi Chocolate', 'Hydrococo 250ml', 'Lasegar Leci', 'Lasegar Lemon', 'Caffino', 'Aqua', 'Mayasi Paw',
        'Brotatoz Rumput Laut', 'Brotatoz Rendang', 'Brotatoz Korea', 'Pulpy Orange', 'Qtela Tempe Original',
        'PotatoQ Sosis Mexico', 'PotatoQ Rumput Laut', 'Yoritos Ayam Bakar', 'Taro BBQ', 'Teh Sejuk', 'Twistko',
        'Potatokrez Sapi Panggang', 'Potatokrez ayam geprek', 'Spix Mie Goreng', 'Fire Crackers Ayam Bawang',
        'Fire Crackers Sambal Mangga', 'Mayasi Kacang Rasa Sapi Panggang', 'Indosnack Potato Chips'
    }

    selected_products = st.selectbox('Select Product for Restock', products_list)
    
    stock_needed = pd.read_csv('stokneed.csv')
    stock_needed_sorted = stock_needed.sort_values(by='Qty Needed', ascending=False)
    last_10 = stock_needed_sorted.head(10)

    st.subheader('Needs Restock')
    st.write(last_10)

    chart = alt.Chart(last_10).mark_bar().encode(
    x=alt.X('Stock Qty Needed', title='Stock Qty Needed'),
    y=alt.Y('Product', sort='-x', title='Product'),
    color=alt.Color('Product', legend=None)
    ).properties(
    title='Top 10 Products Needing Restock'
    )

    st.altair_chart(chart, use_container_width=True)

if __name__ == "__main__":
    main()

