# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd

@st.cache
def load_NC_INV():
    df=pd.read_csv("https://raw.githubusercontent.com/SeanRobertSpragueSr/AFH_NC_PRICING_V_0_0_1/main/DT_INV.csv")
    return df


st.title('Current New Car Inventory')

DT_INV=load_NC_INV()
DT_INV=DT_INV[['Stock Number','Days','Year','Model','VIN','Trim',
               'Cylinders','Trans','Color','Color Code','MSRP','Invoice','E-Price',
               'Color DS']]



Models=list(DT_INV.Model.unique())
Models.insert(0,'All_Models')


Years=list(DT_INV.Year.unique())
Years.insert(0,'All_Years')

Trims=list(DT_INV.Trim.unique())
Trims.insert(0,'All_Trims')



year=st.sidebar.selectbox('Year',Years)
model=st.sidebar.selectbox('Models',Models)
trim=st.sidebar.selectbox('Trims',Trims)



if year=="All_Years":
    DDT_INV=DT_INV
else:
    DDT_INV=DT_INV[DT_INV['Year']==year]

if model=="All_Models":
    DDT_INV=DDT_INV
else:
    DDT_INV=DDT_INV[DDT_INV['Model']==model]
    
if trim =='All_Trims':
    DDT_INV=DDT_INV
else:
    DDT_INV=DDT_INV[DDT_INV['Trim']==trim]
    
    
Colors=list(DDT_INV.Color.unique())
Colors.insert(0,'All_Colors')
color=st.sidebar.selectbox('EXT_Colors',Colors)

if color=='All_Colors':
    DDT_INV=DDT_INV
else:
    DDT_INV=DDT_INV[DDT_INV['Color']==color]

    
st.table(DDT_INV.iloc[:,:])
