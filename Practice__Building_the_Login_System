import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config(page_title="Course Manager", layout="centered")
json_file = Path("users.json")

if json_file.exists():
    with open(json_file, "r") as file:
        users = json.load(file)
else:
    users = [
        {
            "id": "1",
            "email": "admin@school.edu",
            "full_name": "System Admin",
            "password": "123ssag@43AE",
            "role": "Admin",
            "registered_at": str(datetime.now())
        }
    ]
    with open(json_file, "w") as file:
        json.dump(users, file, indent=4)
st.title("Course Manager")
page = st.sidebar.radio("Choose a page:", ["Register", "Login"])

if page == "Register":
    st.subheader("New Instructor Account")

    with st.container():
        email = st.text_input("Email Address")
        full_name = st.text_input("First and Last Name")
        password = st.text_input("Password", type="password")
        role = st.selectbox("Role", ["Instructor"])

if st.button("Create Account"):
    if email and full_name and password:
        email_exists = any(user["email"] == email for user in users)

        if email_exists:
            st.error("An account with that email already exists.")
        else:
            with st.spinner("Creating your account..."):
                time.sleep(1)
                new_user = {
                    "id": str(uuid.uuid4()),
                    "email": email,
                    "full_name": full_name,
                    "password": password,
                    "role": role,
                    "registered_at": str(datetime.now())
                }

                users.append(new_user)

                with open(json_file, "w") as file:
                    json.dump(users, file, indent=4)

            st.success("Account created successfully!")
    else:
        st.error("Please fill in all fields.")
elif page == "Login":
    st.subheader("Login")

    with st.container():
        login_email = st.text_input("Email")
        login_password = st.text_input("Password", type="password")

if st.button("Log In"):
    with st.spinner("Verifying credentials..."):
        time.sleep(1)

        matched_user = None
        for user in users:
            if user["email"] == login_email and user["password"] == login_password:
                matched_user = user
                break

        if matched_user:
            st.success(
                f"Welcome back, {matched_user['full_name']}! "
                f"Role: {matched_user['role']}, "
                f"Email: {matched_user['email']}"
            )
        else:
            st.error("Invalid email or password.")

    st.subheader("Current User Database")
    st.dataframe(users)
