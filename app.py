import streamlit as st

# 1. ตั้งค่าหน้าจอแบบกว้าง (Wide Layout)
st.set_page_config(page_title="Cost Calculator", layout="wide")

st.title("📊 Cost Calculator: LAOS (NONG KHAI)")
st.divider()

# --- แยกสัดส่วนเป็น 2 ฝั่ง (ฝั่งกรอกข้อมูล 70% | ฝั่งสรุปผล 30%) ---
main_col, summary_col = st.columns([7, 3])

with main_col:
    st.markdown("### 📝 ข้อมูลต้นทุนและค่าใช้จ่าย")
    
    # ส่วนตั้งค่าขนาดบรรจุภัณฑ์ และ % Loss
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        package_size = st.radio("ขนาดบรรจุภัณฑ์ (Package Size):", ["25kg", "50kg"], horizontal=True)
    with sub_col2:
        loss_percentage = st.number_input("% Loss (สูญเสียวัตถุดิบ)", min_value=0.0, max_value=99.9, value=10.0, step=0.1)
    
    st.write("")
    
    # แบ่งเป็น 3 คอลัมน์ย่อยสำหรับกรอกข้อมูลค่าใช้จ่าย
    inp_col1, inp_col2, inp_col3 = st.columns(3)
    
    with inp_col1:
        st.markdown("**🛠 Material**")
        base_material_cost = st.number_input("MATERIAL+CLEAR,TRANSPORT", value=4290.000000, format="%.6f")
        
        # คำนวณ Material รวม Loss
        if loss_percentage < 100:
            calc_mat_cost = base_material_cost / (1 - (loss_percentage / 100))
        else:
            calc_mat_cost = 0.0
        st.caption(f"Mat Cost (+Loss): {calc_mat_cost:,.6f}")

    with inp_col2:
        st.markdown("**⚡ Utilities & Labor**")
        maintenance = st.number_input("MAINTANANCE", value=120.564156, format="%.6f")
        electricity = st.number_input("ELECTRICITY", value=335.395700, format="%.6f")
        water = st.number_input("WATER SECTION", value=0.000000, format="%.6f")
        labour = st.number_input("LABOUR", value=1587.691604, format="%.6f")

    with inp_col3:
        st.markdown("**📦 Others**")
        if package_size == "25kg":
            packaging = st.number_input("PAKAGING (25kg)", value=414.50, format="%.2f")
        else:
            packaging = st.number_input("PAKAGING (50kg)", value=476.00, format="%.2f")
            
        oil = st.number_input("OIL", value=47.376262, format="%.6f")
        brass = st.number_input("BRASS", value=22.035870, format="%.6f")
        imp_exp = st.number_input("IMPORT/EXPORT", value=0.000000, format="%.6f")
        commission = st.number_input("COMISSTION", value=0.000000, format="%.6f")

# --- ส่วนคำนวณผลลัพธ์สุทธิ ---
all_cost_no_material = (
    maintenance + electricity + water + labour + 
    packaging + oil + brass + imp_exp + commission
)
total_cost = calc_mat_cost + all_cost_no_material

# --- ส่วนสรุปผลด้านขวามือ (Summary Box ล็อกพื้นที่ตายตัว ปลอดภัยต่อ f-string) ---
with summary_col:
    st.markdown("### 📋 สรุปราคาสุทธิ")
    
    # 1.
