# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 02:06:55 2024

@author: hp5cd
"""

import streamlit as st
import fixterai as fai
import fixtersms as fsms
import fixtermdb as fmdb
import pandas as pd

try:
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://i.postimg.cc/Cx35zkdq/Picture1.png");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    #st.image('https://chennai.vit.ac.in/wp-content/uploads/2021/08/vit_logo_colored.png', width = 200)
    st.image('https://i.postimg.cc/9Mnmvm31/fixter-logo-removebg-preview.png', width = 400)
    with open(r"D:\Ishaan\Bin Arena\Fixter\cred.txt", 'r') as cred:
        regno = cred.read()
    if regno:
        st.title("Community Issues")
        issues = fmdb.get_all_issues()
        issues_ = []
        for x in issues:
            if x['Category']=='Community':
                issues_.append(x)
        df = pd.DataFrame(issues_)
        df.drop(columns=['_id', 'Image Path', 'Resident', 'Time', 'Status', 'Assigned', 'Category'], inplace=True)
        st.dataframe(df)
    else:
        st.title("Please log in...")
        st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpng.pngtree.com%2Fpng-clipart%2F20230120%2Fourmid%2Fpngtree-cartoon-lock-png-image_6564340.png&f=1&nofb=1&ipt=c528165d269cff22526d1009b27871cd9b19add3a2f7cbba1f9fdbd918d8b2c1&ipo=images", width = 200)
except:
    pass