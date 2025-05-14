import streamlit as st
import hashlib
import os
from datetime import datetime
from fpdf import FPDF
from openpyxl import Workbook
import json

# Path to store the user data
USER_FILE = "user_data.txt"

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check if the user exists and if the password is correct
def authenticate_user(username, password):
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            users = file.readlines()
            for user in users:
                stored_username, stored_password_hash = user.strip().split(",")
                if stored_username == username and stored_password_hash == hash_password(password):
                    return True
    return False

# Function to register a new user
def register_user(username, password):
    with open(USER_FILE, "a") as file:
        file.write(f"{username},{hash_password(password)}\n")
    st.success("User registered successfully!")

# User interface to choose between login and register
def user_authentication():
    st.title("User Authentication")

    choice = st.radio("Select action", ("Login", "Register"))

    if choice == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if authenticate_user(username, password):
                st.session_state['user'] = username
                st.success(f"Welcome {username}!")
                return True
            else:
                st.error("Invalid username or password")
                return False

    elif choice == "Register":
        st.subheader("Register New Account")
        username = st.text_input("Choose a username")
        password = st.text_input("Choose a password", type="password")
        confirm_password = st.text_input("Confirm password", type="password")

        if password != confirm_password:
            st.error("Passwords do not match")
        elif st.button("Register"):
            if os.path.exists(USER_FILE):
                with open(USER_FILE, "r") as file:
                    users = file.readlines()
                    for user in users:
                        stored_username, _ = user.strip().split(",")
                        if stored_username == username:
                            st.error("Username already exists")
                            return
            register_user(username, password)
            st.success("You have registered successfully! Please login.")
            return False

    return False

# Main Audit Tool Functionality
def audit_tool():
    # Load questions
    with open("questions.json", "r") as f:
        questions = json.load(f)

    st.title("🛡️ ISO 27001 Internal Audit Tool")
    auditor = st.text_input("👤 Enter Auditor Name")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Answer collection
    responses = {}
    score_summary = {}
    total_score = 0
    total_max = 0

    for domain, qs in questions.items():
        st.subheader(domain)
        domain_score = 0
        for q in qs:
            answer = st.selectbox(f"{q}", ["Select", "Yes", "No", "Partial"], key=q)
            if answer == "Yes":
                domain_score += 2
            elif answer == "Partial":
                domain_score += 1
        max_score = len(qs) * 2
        score_summary[domain] = {"score": domain_score, "max": max_score}
        total_score += domain_score
        total_max += max_score

    # Status calculator
    def get_status(score, max_score):
        pct = (score / max_score) * 100
        if pct == 100:
            return "Compliant"
        elif pct >= 50:
            return "Needs Improvement"
        return "Non-Compliant"

    # Save PDF
    def save_pdf(score_summary, auditor, timestamp):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, "ISO 27001 Audit Report", ln=True, align="C")
        pdf.ln(10)
        pdf.cell(200, 10, f"Auditor: {auditor}", ln=True)
        pdf.cell(200, 10, f"Date: {timestamp}", ln=True)
        pdf.ln(10)

        for domain, data in score_summary.items():
            status = get_status(data["score"], data["max"])
            pdf.cell(200, 10, f"{domain}: {data['score']} / {data['max']} | Status: {status}", ln=True)

        pdf.ln(10)
        overall_status = get_status(total_score, total_max)
        pdf.cell(200, 10, f"Total Score: {total_score} / {total_max}", ln=True)
        pdf.cell(200, 10, f"Overall Status: {overall_status}", ln=True)

        path = f"audit_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf.output(path)
        return path

    # Save Excel
    def save_excel(score_summary, auditor, timestamp):
        wb = Workbook()
        ws = wb.active
        ws.append(["Auditor", auditor])
        ws.append(["Date", timestamp])
        ws.append(["Domain", "Score", "Max Score"])
        for domain, data in score_summary.items():
            ws.append([domain, data["score"], data["max"]])
        ws.append(["Total", total_score, total_max])
        path = f"audit_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        wb.save(path)
        return path

    # Download buttons
    if st.button("Generate Reports"):
        if auditor.strip() == "":
            st.warning("Please enter an auditor name.")
        else:
            pdf_path = save_pdf(score_summary, auditor, timestamp)
            xlsx_path = save_excel(score_summary, auditor, timestamp)
            st.success("Reports generated!")
            st.download_button("📄 Download PDF Report", open(pdf_path, "rb"), file_name=pdf_path)
            st.download_button("📊 Download Excel Report", open(xlsx_path, "rb"), file_name=xlsx_path)


# Check if the user is authenticated
if 'user' not in st.session_state:
    if user_authentication():
        st.session_state['authenticated'] = True
        audit_tool()  # Run the main audit tool
else:
    audit_tool()  # If user is already authenticated, show the main audit tool
