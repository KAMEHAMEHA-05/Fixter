# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:18:38 2024

@author: hp5cd
"""

import streamlit as st
import fixterai as fai
import fixtersms as fsms
import fixtermdb as fmdb
from random import choice

#try:      
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
    queue = []
    st.title("Report an Issue")
    form = st.form(key='SACS PRACTICAL')
    title = form.text_input("Title")
    category = form.selectbox("Category of Issue", ["Community", "Indivisual"])
    description = form.text_area("Description", max_chars=500)
    address = form.text_area("Address", max_chars=200)
    
    # Image upload
    #uploaded_file = form.file_uploader("Upload Image(s)", accept_multiple_files=True)
    submit = form.form_submit_button('Submit')
    lst = []
    for x,z in zip((1,1.5,2),(0,1,2)):
        for y in range(int(2700/x)):
            lst.append(z)
    if submit:
        tags, dept = fai.issue_tag(description)
        staff, _ = fmdb.get_phone_numbers_and_ids_by_dept(dept)
        #issue_id = fmdb.add_issue(regno, category, title, description, 'None', address, tags)
        if staff==[]:
        # SETS PRIORITY IN THE QUEUE
            issue_id = fmdb.add_issue(regno, category, title, description, 'None', address, tags)
            for ind, x in senumerate(queue):
                if fai.priority(tags, x['Tags']):
                    queue.insert(ind, issue_id)
            st.write('Your issue has been queued!')
        else:       
             staff, empid = fmdb.get_phone_numbers_and_ids_by_dept(dept)
             staff_mem = []
             while staff_mem == []:
                 rate = choice(lst)
                 staff_mem = staff[0][0]
                 mem_empid = empid[0][0]
             fsms.main(staff_mem, address, title, description)
             fmdb.set_status_to_occupied(mem_empid)
             issue_id = fmdb.add_issue(regno, category, title, description, 'None', address, tags, empid)
             st.success('Your issue has been assigned!')
else:
    st.title("Please log in...")
    st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpng.pngtree.com%2Fpng-clipart%2F20230120%2Fourmid%2Fpngtree-cartoon-lock-png-image_6564340.png&f=1&nofb=1&ipt=c528165d269cff22526d1009b27871cd9b19add3a2f7cbba1f9fdbd918d8b2c1&ipo=images", width = 200)
#except : pass




        
    
    
    
    

