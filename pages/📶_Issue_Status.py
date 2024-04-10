# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 03:50:10 2024

@author: hp5cd
"""

import streamlit as st
import fixtermdb as fmdb
import pandas as pd
from streamlit_star_rating import st_star_rating

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
    #st.image('https://chennai.vit.ac.in/wp-content/uploads/2021/08/vit_logo_colored.png', 200)
    st.image('https://i.postimg.cc/9Mnmvm31/fixter-logo-removebg-preview.png', width = 400)
    with open(r"D:\Ishaan\Bin Arena\Fixter\cred.txt", 'r') as cred:
        regno = cred.read()
    if regno:
        issues = fmdb.get_all_issues()
        lst = []
        for x in issues:
            if x['Resident'] ==regno:
                lst.append(x['Title'])
        if issues:
            ticket = st.selectbox('Select Title', lst)
            issue = fmdb.get_issue_by_title(ticket)
            df = pd.DataFrame(issues)
            df.drop(columns=['_id'], inplace=True)
            st.dataframe(df)
            if issue['Status']=='Open':
                close = st.button('Close Issue')
            if close:
                fmdb.close_issue(issue["_id"])
                #fmdb.set_status_to_free(issue["Assigned"])
                rating = st_star_rating("Rate your helper", maxValue=5, defaultValue=3, key="rating")
                #fmdb.update_rating_and_ledger(issue["Assigned"], rating)
                fmdb.close_issue(issue["_id"])
                
                
        else:
            st.success("No Pending Issues!")
    else:
        st.title("Please log in...")
        st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpng.pngtree.com%2Fpng-clipart%2F20230120%2Fourmid%2Fpngtree-cartoon-lock-png-image_6564340.png&f=1&nofb=1&ipt=c528165d269cff22526d1009b27871cd9b19add3a2f7cbba1f9fdbd918d8b2c1&ipo=images", width = 200)
except:
    pass

