import streamlit as st 
import time 
import json 
import uuid 
import datetime 
from pathlib import Path 
st.set_page_config(page_title= "Course Manager",  page_icon="", 
 layout="centered", 
 initial_sidebar_state="collapsed") 
st.title("Course Manager") 
st.divider() 
users = [ 
 { 
 "id" : "1", 
 "email" : "admin@school.edu", 
 "full_name" : "System Admin", 
 "password" : "123ssag@43AE", 
 "role" : "Admin", 
 "registered_at" : "..." 
 }, 
 { 
 "id" : "2", 
 "email" : "teacherassistant@school.edu",  "full_name" : "Teacher Assistant",  "password" : "246ssag@84AE", 
 "role" : "Teacher Assistant", 
 "registered_at" : "..." 
 } 
] 
json_path = Path("users.json") 
if json_path.exists(): 
 with json_path.open("r", encoding="utf-8") as f:  users = json.load(f) 
col1, col2 = st.columns(2)
with col1: 
 st.subheader("Login") 
 email = st.text_input("Email", placeholder="Enter your email", key="email_login")  password = st.text_input("Password", placeholder="Enter your password", type="password", key="password_login") 
 btn_login = st.button("Login", use_container_width=True) 
 if btn_login: 
 user_found = False 
 for user in users: 
 if user["email"] == email and user["password"] == password:  user_found = True 
 time.sleep(5) 
 st.success(f"Welcome, {user['full_name']}! You are logged in as {user['role']}.") 
 break 
 if not user_found: 
 time.sleep(5) 
 st.error("Invalid email or password. Please try again.") 
with col2: 
 st.subheader("Register") 
 full_name = st.text_input("Full Name", placeholder="Enter your full name")  email_reg = st.text_input("Email", placeholder="Enter your email", key="email_register") 
 password_reg = st.text_input("Password", placeholder="Enter your password", type="password", key="password_register") 
 role = st.selectbox("Role", ["Select a role", "Admin", "Teacher Assistant"])  btn_register = st.button("Register", use_container_width=True) 
 if btn_register: 
 if not full_name or not email_reg or not password_reg or role == "Select a role": 
 st.warning("Please fill in all the fields and select a role.")  else: 
 new_user_id = str(uuid.uuid4()) 
 registered_at = datetime.datetime.now().isoformat() 
 new_user = { 
 "id" : new_user_id, 
 "email" : email_reg,
 "full_name" : full_name, 
 "password" : password_reg, 
 "role" : role, 
 "registered_at" : registered_at 
 } 
 users.append(new_user) 
 with json_path.open("w", encoding="utf-8") as f: 
 json.dump(users, f, indent=4) 
 st.success(f"Registration successful! Welcome, {full_name}. You can now log in.")
