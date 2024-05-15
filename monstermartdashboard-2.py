#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import os 
import matplotlib.pyplot as plt


# In[ ]:


df1 = pd.read_csv("AKULAKU_FEB.csv")
df2 = pd.read_csv("ALLSEDAYU_FEB.csv")
df3 = pd.read_csv("ARGAPURA2_FEB.csv")
df4 = pd.read_csv("ARWANACITRA_FEB.csv")
df5 = pd.read_csv('ASURANSIJIWAALAMIN_FEB.csv')
df6 = pd.read_csv("AXA4_FEB.csv")
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


# In[ ]:


import streamlit as st
import pandas as pd

def main():
    st.title('Vending Machine Top Sales')

    options = ['AKULAKU_FEB.csv', 'ALLSEDAYU_FEB.csv', 'ARGAPURA2_FEB.csv', 'ARWANACITRA_FEB.csv', 'ASURANSIJIWAALAMIN_FEB.csv', 'AXA4_FEB.csv', 'AXAKUNINGAN1_FEB.csv', 'AXAKUNINGAN2_FEB.csv', 'AXAKUNINGAN3_FEB.csv', 'BAKRIEANDBROTHERLT27_FEB.csv', 'BNIRAWAMANGUN_FEB.csv', 'CBCGALLERY_FEB.csv', 'CLUSTERATHALIA1_FEB.csv', 'CLUSTERATHALIA2_FEB.csv', 'CLUSTERBLUERIVER2_FEB.csv', 'CVJAYAABADI3_FEB.csv', 'DIGNITASACADEMY_FEB.csv', 'GRAHAELNUSA_FEB.csv', 'GRIYAPATRIAGUESTHOUSE_FEB.csv', 'HALIM_FEB.csv', 'HONDAMTHARYONO_FEB.csv', 'HOTEL101_FEB.csv', 'HOTELHERMITAGE_FEB.csv', 'HOTELHILTON_FEB.csv', 'HOTELKEMPINSKI1_FEB.csv', 'HOTELMERCURE_FEB.csv', 'HOTELPARKHYATT_FEB.csv', 'HOTELWYNDHAM_FEB.csv', 'INDOCEMENT_FEB.csv', 'INDOCEMENT2_FEB.csv', 'INDOCEMENT3_FEB.csv', 'INDOCEMENT4_FEB.csv', 'INDOCEMENT5_FEB.csv', 'INDOCEMENT6_FEB.csv', 'INDOCEMENT7_FEB.csv', 'INDOCEMENT8_FEB.csv', 'INDOCEMENT10_FEB.csv', 'JHLSOLITAIRE_FEB.csv', 'KENGSINGTONOFFICETOWER_FEB.csv', 'KLINIKLALITABEKASI_FEB.csv', 'LABSCHOOL1_FEB.csv', 'LABSCHOOL2_FEB.csv', 'LIONVILLAGE1_FEB.csv', 'LIONVILLAGE2_FEB.csv', 'LIPPOTOWERHOLLAND_FEB.csv', 'LIPPOTOWERHOLLAND2_FEB.csv', 'LIPPOTOWERHOLLAND3_FEB.csv', 'MANULIFE1_FEB.csv', 'MANULIFE2_FEB.csv', 'MASJIDALAZHARBEKASI1_FEB.csv', 'MASJIDATTAIBIN_FEB.csv', 'MENARATHAMRIN_FEB.csv', 'MONSTERMART_FEB.csv', 'NEOSOHO_FEB.csv', 'NINERESIDENCE_FEB.csv', 'PADINASOHO_FEB.csv', 'PTBAKER&HUGHES_FEB.csv', 'PTBASF_FEB.csv', 'PTCCIE(INDOCEMENT11)_FEB.csv', 'PTMATRARODAPIRANTI1_FEB.csv', 'PTMATRARODAPIRANTI2_FEB.csv', 'PTMATRARODAPIRANTI3_FEB.csv', 'PTSINERGI_FEB.csv', 'PTTIMERINDO_FEB.csv', 'PTTOACOATING1_FEB.csv', 'PULOMAS1_FEB.csv', 'PULOMAS2_FEB.csv', 'PULOMAS4_FEB.csv', 'REGALSTUDIO_FEB.csv', 'ROYALENFIELDANTASARI_FEB.csv', 'RSCM1_FEB.csv', 'RSCM2_FEB.csv', 'RSCM3_FEB.csv', 'RSCM4_FEB.csv', 'RSDINDA_FEB.csv', 'RSIAPRATIWI_FEB.csv', 'RSJAKARTA2_FEB.csv', 'RSJAKARTA3_FEB.csv', 'RSUIFARMASI_FEB.csv', 'RSUIIGD_FEB.csv', 'RSUILOBBY_FEB.csv', 'RSUILT5_FEB.csv', 'SEKOLAHALAZHARGRANDWISATABEKASI_FEB.csv', 'SAMSUNGKUNINGAN1_FEB.csv', 'SAMSUNGKUNINGAN2_FEB.csv', 'SEKOLAHBSP_FEB.csv', 'SEKOLAHFAJAR_FEB.csv', 'SENTRATIMUR1_FEB.csv', 'SENTRATIMUR2_FEB.csv', 'SMARTHAPPYKIDS_FEB.csv', 'SMKTELKOM_FEB.csv', 'STREGIST1_FEB.csv', 'STREGIST2_FEB.csv', 'UNIPREPBSD1_FEB.csv', 'UNIPREPBSD2_FEB.csv', 'UNIPREPKELAPAGADING_FEB.csv', 'UNIPREPPONDOKINDAH_FEB.csv', 'UNIVBAKRIE1_FEB.csv', 'UNIVBAKRIE2_FEB.csv', 'UNIVBAKRIE3_FEB.csv', 'UNIVERSALLUGAGE1_FEB.csv', 'UNIVERSALLUGAGE2_FEB.csv', 'UNIVERSITASPANCASILA_FEB.csv']
    selected_option = st.selectbox('Select Dataset', options)

    df = pd.read_csv(selected_option)

    df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%Y-%m-%d %I:%M %p')
    df_sorted = df.sort_values(by="Qty Sold", ascending=False)
    top_10 = df_sorted.head(10)
    st.subheader('Top 10 Quantities Sold')

    st.write(top_10)
    st.bar_chart(top_10.set_index('Product')['Qty Sold'])

    st.subheader('Time Series of Sales and Quantity Sold')
    df.set_index('Datetime', inplace=True)
    time_series = df[['Qty Sold', 'Sales']]

    st.line_chart(time_series)

if __name__ == "__main__":
    main()

