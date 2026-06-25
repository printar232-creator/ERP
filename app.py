import streamlit as st

# 1. ตั้งค่าหน้าจอแบบกว้าง (Wide Layout)
st.set_page_config(page_title="Cost Calculator", layout="wide")

st.title("📊 Cost Calculator: LAOS (NONG KHAI)")
st.divider()

# --- ส่วนที่ 1: ตั้งค่าบรรจุภัณฑ์ และ % Loss ---
col_h1, col_h2 = st.columns([2, 1])
with col_h1:
    package_size = st.radio("ขนาดบรรจุภัณฑ์ (Package Size):", ["25kg", "50kg"], horizontal=True)
with col_h2:
    loss_percentage = st.number_input("% Loss (สูญเสียวัตถุดิบ)", min_value=0.0, max_value=99.9, value=10.0, step=0.1)

st.divider()

# --- ส่วนที่ 2: สร้างฟอร์มรับค่าตัวเลข (แบ่ง 3 คอลัมน์) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🛠 Material Cost")
    base_material_cost = st.number_input("MATERIAL+CLEAR,TRANSPORT", value=4290.000000, format="%.6f")
    
    # คำนวณ Material รวม Loss
    if loss_percentage < 100:
        calc_mat_cost = base_material_cost / (1 - (loss_percentage / 100))
    else:
        calc_mat_cost = 0.0
    st.info(f"Mat Cost (+Loss): {calc_mat_cost:,.6f}")

with col2:
    st.markdown("### ⚡ Utilities & Labor")
    maintenance = st.number_input("MAINTANANCE", value=120.564156, format="%.6f")
    electricity = st.number_input("ELECTRICITY", value=335.395700, format="%.6f")
    water = st.number_input("WATER SECTION", value=0.000000, format="%.6f")
    labour = st.number_input("LABOUR", value=1587.691604, format="%.6f")

with col3:
    st.markdown("### 📦 Others & Packaging")
    if package_size == "25kg":
        packaging = st.number_input("PAKAGING (25kg)", value=414.50, format="%.2f")
    else:
        packaging = st.number_input("PAKAGING (50kg)", value=476.00, format="%.2f")
        
    oil = st.number_input("OIL", value=47.376262, format="%.6f")
    brass = st.number_input("BRASS", value=22.035870, format="%.6f")
    imp_exp = st.number_input("IMPORT/EXPORT", value=0.000000, format="%.6f")
    commission = st.number_input("COMISSTION", value=0.000000, format="%.6f")

# --- ส่วนที่ 3: คำนวณผลลัพธ์สุทธิ ---
all_cost_no_material = (
    maintenance + electricity + water + labour + 
    packaging + oil + brass + imp_exp + commission
)
total_cost = calc_mat_cost + all_cost_no_material

st.divider()

# --- ส่วนที่ 4: แสดงผลลัพธ์สร
