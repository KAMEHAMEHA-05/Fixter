# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 00:41:59 2024

@author: hp5cd
"""

from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

#client = MongoClient(‘lundbarabar’, 696969) # yaha id password daal
connection_string = "mongodb://localhost:27017"
client = MongoClient(connection_string)
db = client['Fixter']
issues_collection = db['ISSUES']
student_collection = db['STUDENT']
unresolved_collection = db['UNRESOLVED']
log_collection = db['LOG']
student_cred = db['Student Credentials']
staff = db['Staff']
current_time = datetime.now()
def add_issue(regno, category, title, description, path, address, tags, empid):
    issue_data = {
        "Category": category,
        "Title": title,
        "Description": description,
        "Image Path": path,
        "Resident": regno,
        "Address": address,
        "Time": current_time.strftime("%H:%M:%S"),
        "Tags": tags,
        "Status": "Open",
        "Assigned": empid
    }
    result = issues_collection.insert_one(issue_data)
    new_issue_id = str(result.inserted_id)
    student_collection.update_many({}, {'$push': {'Issues': new_issue_id}})
    student = student_cred.find_one({"Reg No": regno})
    student['Issues'].append(issue_data)
    return new_issue_id

def close_issue(issue_id):
    issues_collection.update_one({"_id": ObjectId(issue_id)}, {'$set': {'Status': 'Closed'}})
    issue = issues_collection.find_one({"_id": ObjectId(issue_id)})
    log_collection.insert_one(issue)
    issues_collection.delete_one({"_id": ObjectId(issue_id)})

def add_to_unresolved(issue_id):
    issue = issues_collection.find_one({"_id": ObjectId(issue_id)})
    unresolved_collection.insert_one(issue)

def get_community_issues():
    community_issues = issues_collection.find({"Category": "Community"})
    return list(community_issues)

def get_issue(issue_id):
    issue = issues_collection.find_one({"_id": ObjectId(issue_id)})
    return issue

def get_issue_by_reg(regno):
    issues = student_cred.find_one({"Reg No": regno})
    return issues

def get_issue_by_title(title):
    issue = issues_collection.find_one({"Title": title})
    return issue

def get_all_issues():
    all_issues = issues_collection.find()
    return list(all_issues)

def verify(regno, passwd):
    student = student_cred.find_one({'Reg No': regno, 'Password':passwd})
    if student is None:
        return False
    else:
        return True
    print(student)
def get_phone_numbers_and_ids_by_dept(dept):
    members = staff.find()
    ph1 = []
    id1 = []
    ph2 = []
    id2 = []
    ph3 = []
    id3 = []
    for x in members:
        if x['Dept'] == dept and x['Avg_Rating']>0 and x['Avg_Rating']<2 and x['Status']=='free':
            ph1.append(x['Phone'])
            id1.append(x['Employee_ID'])
        if x['Dept'] == dept and x['Avg_Rating']>2 and x['Avg_Rating']<3.5 and x['Status']=='free':
            ph2.append(x['Phone'])
            id2.append(x['Employee_ID'])
        if x['Dept'] == dept and x['Avg_Rating']>3.5 and x['Avg_Rating']<5 and x['Status']=='free':
            ph3.append(x['Phone'])
            id3.append(x['Employee_ID'])
    return [ph3, ph2, ph1], [id3, id2, id1]

def set_status_to_occupied(eid):
    member = staff.find_one({"Employee_ID" : eid})
    member['Status'] = 'Occupied'
    
def set_status_to_free(eid):
    member = staff.find_one({"Employee_ID" : eid})
    member['Status'] = 'free'
    
def update_rating_and_ledger(eid, rating):
    member = staff.find_one({"Employee_ID" : eid})
    member['Avg_Rating'] = (member['Avg_Rating']*member['Work_Count']+rating)/(member['Work_Count']+1)