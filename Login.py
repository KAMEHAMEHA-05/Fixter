# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 05:54:42 2024

@author: hp5cd
"""
import streamlit as st
import fixtermdb as fmdb

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
st.image('https://i.postimg.cc/9Mnmvm31/fixter-logo-removebg-preview.png', width = 400)
with open(<cred_file_path>, 'r') as cred:
    regno = cred.read()
if not regno:
    st.title("Log In")
    form = st.form('Login')
    regno = form.text_input("Registration Number")
    passwd = form.text_input("Password")
    submit = form.form_submit_button('Log In')
    if submit:
        if fmdb.verify(regno, passwd):
            st.success('Logged In!')
            with open(<cred_file_path>, "w") as file:
                file.write(regno)
        else:
            st.error("Invalid Credentials")
else :
    student = fmdb.get_issue_by_reg(regno)
    st.write('Name : ', student['Name'])
    st.write('Reg No : ', regno)
    logout = st.button('Logout')
    if logout:
        with open(<cred_file_path>, 'w') as cred:
            pass
