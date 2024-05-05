#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import os 
import matplotlib.pyplot as plt


# In[17]:


df1 = pd.read_csv('/Users/jleo/Desktop/monstermart/AKULAKU_FEB.csv')
df2 = pd.read_csv('/Users/jleo/Desktop/monstermart/ALLSEDAYU_FEB.csv')
df3 = pd.read_csv('/Users/jleo/Desktop/monstermart/ARGAPURA2_FEB.csv')
df4 = pd.read_csv('/Users/jleo/Desktop/monstermart/ARWANACITRA_FEB.csv')
df5 = pd.read_csv('/Users/jleo/Desktop/monstermart/ASURANSIJIWAALAMIN_FEB.csv')
df6 = pd.read_csv('/Users/jleo/Desktop/monstermart/AXA4_FEB.csv')
df7 = pd.read_csv('/Users/jleo/Desktop/monstermart/AXAKUNINGAN1_FEB.csv')
df8 = pd.read_csv('/Users/jleo/Desktop/monstermart/AXAKUNINGAN2_FEB.csv')
df9 = pd.read_csv('/Users/jleo/Desktop/monstermart/BAKRIEANDBROTHERLT27_FEB.csv')
df10 = pd.read_csv('/Users/jleo/Desktop/monstermart/BNIRAWAMANGUN_FEB.csv')
df11 = pd.read_csv('/Users/jleo/Desktop/monstermart/CBCGALLERY_FEB.csv')
df12 = pd.read_csv('/Users/jleo/Desktop/monstermart/CLUSTERATHALIA1_FEB.csv')
df13 = pd.read_csv('/Users/jleo/Desktop/monstermart/CLUSTERATHALIA2_FEB.csv')
df14 = pd.read_csv('/Users/jleo/Desktop/monstermart/CLUSTERBLUERIVER2_FEB.csv')
df15 = pd.read_csv('/Users/jleo/Desktop/monstermart/CVJAYAABADI3_FEB.csv')
df16 = pd.read_csv('/Users/jleo/Desktop/monstermart/DIGNITASACADEMY_FEB.csv')
df17 = pd.read_csv('/Users/jleo/Desktop/monstermart/GRAHAELNUSA_FEB.csv')
df18 = pd.read_csv('/Users/jleo/Desktop/monstermart/GRIYAPATRIAGUESTHOUSE_FEB.csv')
df19 = pd.read_csv('/Users/jleo/Desktop/monstermart/HALIM_FEB.csv')
df20 = pd.read_csv('/Users/jleo/Desktop/monstermart/HONDAMTHARYONO_FEB.csv')
df21 = pd.read_csv('/Users/jleo/Desktop/monstermart/HOTEL101_FEB.csv')
df22 = pd.read_csv('/Users/jleo/Desktop/monstermart/HOTELHERMITAGE_FEB.csv')
df23 = pd.read_csv('/Users/jleo/Desktop/monstermart/HOTELHILTON_FEB.csv')
df24 = pd.read_csv('/Users/jleo/Desktop/monstermart/HOTELKEMPINSKI1_FEB.csv')
df25 = pd.read_csv('/Users/jleo/Desktop/monstermart/HOTELMERCURE_FEB.csv')
df26 = pd.read_csv('/Users/jleo/Desktop/monstermart/HOTELPARKHYATT_FEB.csv')
df27 = pd.read_csv('/Users/jleo/Desktop/monstermart/HOTELWYNDHAM_FEB.csv')
df28 = pd.read_csv('/Users/jleo/Desktop/monstermart/INDOCEMENT_FEB.csv')
df29 = pd.read_csv('/Users/jleo/Desktop/monstermart/INDOCEMENT2_FEB.csv')
df30 = pd.read_csv('/Users/jleo/Desktop/monstermart/INDOCEMENT3_FEB.csv')
df31 = pd.read_csv('/Users/jleo/Desktop/monstermart/INDOCEMENT4_FEB.csv')
df32 = pd.read_csv('/Users/jleo/Desktop/monstermart/INDOCEMENT5_FEB.csv')
df33 = pd.read_csv('/Users/jleo/Desktop/monstermart/INDOCEMENT6_FEB.csv')
df34 = pd.read_csv('/Users/jleo/Desktop/monstermart/INDOCEMENT7_FEB.csv')
df35 = pd.read_csv('/Users/jleo/Desktop/monstermart/INDOCEMENT8_FEB.csv')
df36 = pd.read_csv('/Users/jleo/Desktop/monstermart/INDOCEMENT10_FEB.csv')
df37 = pd.read_csv('/Users/jleo/Desktop/monstermart/JHLSOLITAIRE_FEB.csv')
df38 = pd.read_csv('/Users/jleo/Desktop/monstermart/KENGSINGTONOFFICETOWER_FEB.csv')
df39 = pd.read_csv('/Users/jleo/Desktop/monstermart/KLINIKLALITABEKASI_FEB.csv')
df40 = pd.read_csv('/Users/jleo/Desktop/monstermart/LABSCHOOL1_FEB.csv')
df41 = pd.read_csv('/Users/jleo/Desktop/monstermart/LABSCHOOL2_FEB.csv')
df42 = pd.read_csv('/Users/jleo/Desktop/monstermart/LIONVILLAGE1_FEB.csv')
df43 = pd.read_csv('/Users/jleo/Desktop/monstermart/LIONVILLAGE2_FEB.csv')
df44 = pd.read_csv('/Users/jleo/Desktop/monstermart/LIPPOTOWERHOLLAND_FEB.csv')
df45 = pd.read_csv('/Users/jleo/Desktop/monstermart/LIPPOTOWERHOLLAND2_FEB.csv')
df46 = pd.read_csv('/Users/jleo/Desktop/monstermart/LIPPOTOWERHOLLAND3_FEB.csv')
df47 = pd.read_csv('/Users/jleo/Desktop/monstermart/MANULIFE1_FEB.csv')
df48 = pd.read_csv('/Users/jleo/Desktop/monstermart/MANULIFE2_FEB.csv')
df49 = pd.read_csv('/Users/jleo/Desktop/monstermart/MASJIDALAZHARBEKASI1_FEB.csv')
df50 = pd.read_csv('/Users/jleo/Desktop/monstermart/MASJIDATTAIBIN_FEB.csv')
df51 = pd.read_csv('/Users/jleo/Desktop/monstermart/MENARATHAMRIN_FEB.csv')
df52 = pd.read_csv('/Users/jleo/Desktop/monstermart/MONSTERMART_FEB.csv')
df53 = pd.read_csv('/Users/jleo/Desktop/monstermart/NEOSOHO_FEB.csv')
df54 = pd.read_csv('/Users/jleo/Desktop/monstermart/NINERESIDENCE_FEB.csv')
df55 = pd.read_csv('/Users/jleo/Desktop/monstermart/PADINASOHO_FEB.csv')
df56 = pd.read_csv('/Users/jleo/Desktop/monstermart/PTBAKER&HUGHES_FEB.csv')
df57 = pd.read_csv('/Users/jleo/Desktop/monstermart/PTBASF_FEB.csv')
df58 = pd.read_csv('/Users/jleo/Desktop/monstermart/PTCCIE(INDOCEMENT11)_FEB.csv')
df59 = pd.read_csv('/Users/jleo/Desktop/monstermart/PTMATRARODAPIRANTI1_FEB.csv')
df60 = pd.read_csv('/Users/jleo/Desktop/monstermart/PTMATRARODAPIRANTI2_FEB.csv')
df61 = pd.read_csv('/Users/jleo/Desktop/monstermart/PTMATRARODAPIRANTI3_FEB.csv')
df62 = pd.read_csv('/Users/jleo/Desktop/monstermart/PTSINERGI_FEB.csv')
df63 = pd.read_csv('/Users/jleo/Desktop/monstermart/PTTIMERINDO_FEB.csv')
df64 = pd.read_csv('/Users/jleo/Desktop/monstermart/PTTOACOATING1_FEB.csv')
df65 = pd.read_csv('/Users/jleo/Desktop/monstermart/PULOMAS1_FEB.csv')
df66 = pd.read_csv('/Users/jleo/Desktop/monstermart/PULOMAS2_FEB.csv')
df67 = pd.read_csv('/Users/jleo/Desktop/monstermart/PULOMAS4_FEB.csv')
df68 = pd.read_csv('/Users/jleo/Desktop/monstermart/REGALSTUDIO_FEB.csv')
df69 = pd.read_csv('/Users/jleo/Desktop/monstermart/ROYALENFIELDANTASARI_FEB.csv')
df70 = pd.read_csv('/Users/jleo/Desktop/monstermart/RSCM1_FEB.csv')
df71 = pd.read_csv('/Users/jleo/Desktop/monstermart/RSCM2_FEB.csv')
df72 = pd.read_csv('/Users/jleo/Desktop/monstermart/RSCM3_FEB.csv')
df73 = pd.read_csv('/Users/jleo/Desktop/monstermart/RSCM4_FEB.csv')
df74 = pd.read_csv('/Users/jleo/Desktop/monstermart/RSDINDA_FEB.csv')
df75 = pd.read_csv('/Users/jleo/Desktop/monstermart/RSIAPRATIWI_FEB.csv')
df76 = pd.read_csv('/Users/jleo/Desktop/monstermart/RSJAKARTA2_FEB.csv')
df77 = pd.read_csv('/Users/jleo/Desktop/monstermart/RSJAKARTA3_FEB.csv')
df78 = pd.read_csv('/Users/jleo/Desktop/monstermart/RSUIFARMASI_FEB.csv')
df79 = pd.read_csv('/Users/jleo/Desktop/monstermart/RSUIIGD_FEB.csv')
df80 = pd.read_csv('/Users/jleo/Desktop/monstermart/RSUILOBBY_FEB.csv')
df81 = pd.read_csv('/Users/jleo/Desktop/monstermart/RSUILT5_FEB.csv')
df82 = pd.read_csv('/Users/jleo/Desktop/monstermart/SAMPOERNAUNIVERSITYLANTAI19_FEB.csv')
df83 = pd.read_csv('/Users/jleo/Desktop/monstermart/SAMSUNGKUNINGAN1_FEB.csv')
df84 = pd.read_csv('/Users/jleo/Desktop/monstermart/SAMSUNGKUNINGAN2_FEB.csv')
df85 = pd.read_csv('/Users/jleo/Desktop/monstermart/SEKOLAHBSP_FEB.csv')
df86 = pd.read_csv('/Users/jleo/Desktop/monstermart/SEKOLAHFAJAR_FEB.csv')
df87 = pd.read_csv('/Users/jleo/Desktop/monstermart/SMARTHAPPYKIDS_FEB.csv')
df88 = pd.read_csv('/Users/jleo/Desktop/monstermart/SMKTELKOM_FEB.csv')
df89 = pd.read_csv('/Users/jleo/Desktop/monstermart/STREGIST1_FEB.csv')
df90 = pd.read_csv('/Users/jleo/Desktop/monstermart/STREGIST2_FEB.csv')
df91 = pd.read_csv('/Users/jleo/Desktop/monstermart/UNIPREPBSD1_FEB.csv')
df92 = pd.read_csv('/Users/jleo/Desktop/monstermart/UNIPREPBSD2_FEB.csv')
df93 = pd.read_csv('/Users/jleo/Desktop/monstermart/UNIPREPKELAPAGADING_FEB.csv')
df94 = pd.read_csv('/Users/jleo/Desktop/monstermart/UNIPREPPONDOKINDAH_FEB.csv')
df95 = pd.read_csv('/Users/jleo/Desktop/monstermart/UNIVBAKRIE1_FEB.csv')
df96 = pd.read_csv('/Users/jleo/Desktop/monstermart/UNIVBAKRIE2_FEB.csv')
df97 = pd.read_csv('/Users/jleo/Desktop/monstermart/UNIVBAKRIE3_FEB.csv')
df98 = pd.read_csv('/Users/jleo/Desktop/monstermart/UNIVERSALLUGAGE1_FEB.csv')
df99 = pd.read_csv('/Users/jleo/Desktop/monstermart/UNIVERSALLUGAGE2_FEB.csv')
df100 = pd.read_csv('/Users/jleo/Desktop/monstermart/UNIVERSITASPANCASILA_FEB.csv')


# In[26]:


import plotly.express as px

def generate_pie_chart(dataset):
    fig = px.pie(dataset, values='Sales', names='Product', title='Sales Distribution by Product')
    return fig

def main():
    st.title('Vending Machine Sales Dashboard')
    
    for i in range(1, 101):
        dataset_name = f"df{i}"
        dataset = globals()[dataset_name]  
        st.subheader(f'Dataset {i}')
        st.write(dataset.head())  
        pie_chart = generate_pie_chart(dataset)
        st.plotly_chart(pie_chart)  

if __name__ == "__main__":
    main()

