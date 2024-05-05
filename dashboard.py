#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import os 
import matplotlib.pyplot as plt


# In[17]:


df1 = pd.read_csv("https://github.com/jmichikoleo/coding/blob/main/AKULAKU_FEB.csv")
df2 = pd.read_csv("https://github.com/jmichikoleo/coding/blob/main/ALLSEDAYU_FEB.csv")
df3 = pd.read_csv("https://github.com/jmichikoleo/coding/blob/main/ARGAPURA2_FEB.csv")
df4 = pd.read_csv("https://github.com/jmichikoleo/coding/blob/main/ARWANACITRA_FEB.csv")
df5 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/ASURANSIJIWAALAMIN_FEB.csv')
df6 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/AXA4_FEB.csv")
df7 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/AXAKUNINGAN1_FEB.csv')
df8 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/AXAKUNINGAN2_FEB.csv')
df9 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/BAKRIEANDBROTHERLT27_FEB.csv')
df10 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/BNIRAWAMANGUN_FEB.csv')
df11 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/CBCGALLERY_FEB.csv')
df12 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/CLUSTERATHALIA1_FEB.csv')
df13 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/CLUSTERATHALIA2_FEB.csv')
df14 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/CLUSTERBLUERIVER2_FEB.csv')
df15 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/CVJAYAABADI3_FEB.csv')
df16 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/DIGNITASACADEMY_FEB.csv')
df17 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/GRAHAELNUSA_FEB.csv')
df18 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/GRIYAPATRIAGUESTHOUSE_FEB.csv')
df19 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/HALIM_FEB.csv')
df20 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/HONDAMTHARYONO_FEB.csv')
df21 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/HOTEL101_FEB.csv')
df22 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/HOTELHERMITAGE_FEB.csv')
df23 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/HOTELHILTON_FEB.csv')
df24 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/HOTELKEMPINSKI1_FEB.csv')
df25 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/HOTELMERCURE_FEB.csv')
df26 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/HOTELPARKHYATT_FEB.csv')
df27 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/HOTELWYNDHAM_FEB.csv')
df28 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/INDOCEMENT_FEB.csv')
df29 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/INDOCEMENT2_FEB.csv')
df30 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/INDOCEMENT3_FEB.csv')
df31 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/INDOCEMENT4_FEB.csv')
df32 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/INDOCEMENT5_FEB.csv')
df33 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/INDOCEMENT6_FEB.csv')
df34 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/INDOCEMENT7_FEB.csv')
df35 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/INDOCEMENT8_FEB.csv')
df36 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/INDOCEMENT10_FEB.csv')
df37 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/JHLSOLITAIRE_FEB.csv')
df38 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/KENGSINGTONOFFICETOWER_FEB.csv')
df39 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/KLINIKLALITABEKASI_FEB.csv')
df40 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/LABSCHOOL1_FEB.csv')
df41 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/LABSCHOOL2_FEB.csv')
df42 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/LIONVILLAGE1_FEB.csv')
df43 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/LIONVILLAGE2_FEB.csv')
df44 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/LIPPOTOWERHOLLAND_FEB.csv')
df45 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/LIPPOTOWERHOLLAND2_FEB.csv')
df46 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/LIPPOTOWERHOLLAND3_FEB.csv')
df47 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/MANULIFE1_FEB.csv')
df48 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/MANULIFE2_FEB.csv')
df49 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/MASJIDALAZHARBEKASI1_FEB.csv')
df50 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/MASJIDATTAIBIN_FEB.csv')
df51 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/MENARATHAMRIN_FEB.csv')
df52 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/MONSTERMART_FEB.csv')
df53 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/NEOSOHO_FEB.csv')
df54 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/NINERESIDENCE_FEB.csv')
df55 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/PADINASOHO_FEB.csv')
df56 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/PTBAKER&HUGHES_FEB.csv')
df57 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/PTBASF_FEB.csv')
df58 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/PTCCIE(INDOCEMENT11)_FEB.csv')
df59 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/PTMATRARODAPIRANTI1_FEB.csv')
df60 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/PTMATRARODAPIRANTI2_FEB.csv')
df61 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/PTMATRARODAPIRANTI3_FEB.csv')
df62 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/PTSINERGI_FEB.csv')
df63 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/PTTIMERINDO_FEB.csv')
df64 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/PTTOACOATING1_FEB.csv')
df65 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/PULOMAS1_FEB.csv')
df66 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/PULOMAS2_FEB.csv')
df67 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/PULOMAS4_FEB.csv')
df68 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/REGALSTUDIO_FEB.csv')
df69 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/ROYALENFIELDANTASARI_FEB.csv')
df70 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/RSCM1_FEB.csv')
df71 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/RSCM2_FEB.csv')
df72 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/RSCM3_FEB.csv')
df73 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/RSCM4_FEB.csv')
df74 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/RSDINDA_FEB.csv')
df75 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/RSIAPRATIWI_FEB.csv')
df76 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/RSJAKARTA2_FEB.csv')
df77 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/RSJAKARTA3_FEB.csv')
df78 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/RSUIFARMASI_FEB.csv')
df79 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/RSUIIGD_FEB.csv')
df80 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/RSUILOBBY_FEB.csv')
df81 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/RSUILT5_FEB.csv')
df82 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/SAMPOERNAUNIVERSITYLANTAI19_FEB.csv')
df83 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/SAMSUNGKUNINGAN1_FEB.csv')
df84 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/SAMSUNGKUNINGAN2_FEB.csv')
df85 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/SEKOLAHBSP_FEB.csv')
df86 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/SEKOLAHFAJAR_FEB.csv')
df87 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/SMARTHAPPYKIDS_FEB.csv')
df88 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/SMKTELKOM_FEB.csv')
df89 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/STREGIST1_FEB.csv')
df90 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/STREGIST2_FEB.csv')
df91 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/UNIPREPBSD1_FEB.csv')
df92 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/UNIPREPBSD2_FEB.csv')
df93 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/UNIPREPKELAPAGADING_FEB.csv')
df94 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/UNIPREPPONDOKINDAH_FEB.csv')
df95 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/UNIVBAKRIE1_FEB.csv')
df96 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/UNIVBAKRIE2_FEB.csv')
df97 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/UNIVBAKRIE3_FEB.csv')
df98 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/UNIVERSALLUGAGE1_FEB.csv')
df99 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/UNIVERSALLUGAGE2_FEB.csv')
df100 = pd.read_csv('https://github.com/jmichikoleo/coding/blob/main/UNIVERSITASPANCASILA_FEB.csv')


# In[38]:


dfall = [df1, df2, df3, df4, df5, df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36,df37,df38,df39,df40,df41,df42,df43,df44,df45,df46,df47,df48,df49,df50,df51,df52,df53,df54,df55,df56,df57,df58,df59,df60,df61,df62,df63,df64,df65,df66,df67,df68,df69,df70,df71,df72,df73,df74,df75,df76,df77,df78,df79,df80,df81,df82,df83,df84,df85,df86,df87,df88,df89,df90,df91,df92,df93,df94,df95,df96,df97,df98,df99,df100]

combined_df = pd.concat(dfall, ignore_index=True)


# In[30]:


import plotly.express as px

def generate_pie_chart(dataset):
    fig = px.pie(dataset, values='Sales', names='Product', title='Sales Distribution by Product')
    return fig

def main():
    st.title('Vending Machine Top Sales Dashboard')
    
    combined_df = pd.DataFrame()
    for i in range(1, 101):
        dataset_name = f"df{i}"
        dataset = globals()[dataset_name]
        combined_df = pd.concat([combined_df, dataset], ignore_index=True)
        
    st.subheader('Combined Dataset')
    st.write(combined_df.head())
    
    pie_chart = generate_pie_chart(combined_df)
    st.plotly_chart(pie_chart)  

if __name__ == "__main__":
    main()


# In[31]:


df.to_csv('combined_df.csv', index=False)


# In[ ]:




