import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บหน้าตาแอปพลิเคชัน
st.set_page_config(page_title="AMR Cost Calculator", layout="centered")

st.title("📊 ระบบคำนวณและแสดงต้นทุนสินค้า (Cost Breakdown)")
st.write("เลือกข้อมูลเพื่อแสดงต้นทุนย่อยและต้นทุนรวมของผลิตภัณฑ์")

# 1. ฟังก์ชันโหลดข้อมูล (แนะนำให้เปลี่ยน URL เป็นลิงก์ Raw ของ GitHub คุณเอง)
@st.cache_data
def load_data():
    # ตัวอย่างการใส่ค่า Mockup ข้อมูลตามโครงสร้างไฟล์ของคุณ 
    # หากใช้งานจริงให้เปิดใช้งานบรรทัดด้านล่างนี้แล้วใส่ URL ไฟล์จริงบน GitHub:
    # url = "https://raw.githubusercontent.com/username/repo/main/cost_data.csv"
    # return pd.read_csv(url)
    
    mock_data = {
        'product_type': ['M5', 'M5', 'M7', 'M10', 'A45', 'B45', 'C5', 'D45'],
        'packaging': ['25kg', '50kg', '25kg', '25kg', '25kg', '50kg', '25kg', 'big bag'],
        'source': ['CHINA', 'LAOS', 'CHINA', 'LAOS', 'CHINA', 'LAOS', 'CHINA', 'LAOS'],
        'ค่าวัตถุดิบ (Raw Material)': [7718, 6400, 8200, 6400, 7718, 4700, 4290, 3400],
        'ค่าไฟโรงงาน (Electricity)': [804.95, 431.81, 804.95, 431.81, 631.29, 431.81, 804.95, 631.29],
        'ค่าซ่อมบำรุง (Maintenance)': [145.78, 302.86, 145.78, 302.86, 145.78, 302.86, 145.78, 145.78],
        'ค่าแรงฝ่ายผลิต (Labor)': [1587.69, 1850.46, 1587.69, 1850.46, 1587.69, 1850.46, 1587.69, 1587.69],
        'ค่าบรรจุภัณฑ์และพาเลท (Bag/Pallet)': [479.47, 550.00, 479.47, 479.47, 1202.44, 600.00, 479.47, 160.00]
    }
    df = pd.DataFrame(mock_data)
    return df

df = load_data()

# 2. ส่วนของตัวเลือก Filter (Drop-
