import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="ระบบคำนวณต้นทุน (Laos - Nong Khai)", layout="centered")

st.title("📊 ระบบคำนวณต้นทุนวัตถุดิบและค่าใช้จ่าย")
st.subheader("สถิติอ้างอิง: LAOS (NONG KHAI)")
st.write("---")

# ==========================================
# ส่วนที่ 1: การกรอกข้อมูลวัตถุดิบและ % Loss
# ==========================================
st.header("1. ต้นทุนวัตถุดิบ (Material Cost)")

col_mat1, col_mat2 = st.columns(2)

with col_mat1:
    base_material_cost = st.number_input(
        "ราคาวัตถุดิบพื้นฐาน (ต่อหน่วย)", 
        min_value=0.0, 
        value=4766.666667, 
        format="%.6f"
    )

with col_mat2:
    loss_percentage = st.number_input(
        "เปอร์เซ็นต์การสูญเสีย (% Loss)", 
        min_value=0.0, 
        max_value=100.0, 
        value=0.0, 
        step=0.5
    )

# คำนวณต้นทุนวัตถุดิบที่รวมสูญเสียแล้ว
# สูตร: ต้นทุนรวมสูญเสีย = ราคาพื้นฐาน / (1 - (% Loss / 100))
if loss_percentage < 100:
    calculated_material_cost = base_material_cost / (1 - (loss_percentage / 100))
else:
    calculated_material_cost = 0.0

st.info(f"💡 **ต้นทุนวัตถุดิบที่รวมสูญเสียแล้ว:** {calculated_material_cost:,.6f}")

st.write("---")

# ==========================================
# ส่วนที่ 2: ค่าใช้จ่ายอื่น ๆ (Fixed & Variable Costs)
# ==========================================
st.header("2. รายละเอียดค่าใช้จ่ายอื่น ๆ")

# สร้างฟอร์มกรอกข้อมูลค่าใช้จ่ายคงที่ตามรูปภาพ
col1, col2 = st.columns(2)

with col1:
    maintenance = st.number_input("MAINTENANCE", min_value=0.0, value=120.5641558, format="%.7f")
    electricity = st.number_input("ELECTRICITY", min_value=0.0, value=335.3956996, format="%.7f")
    water_section = st.number_input("WATER SECTION", min_value=0.0, value=0.0, format="%.1f")
    labour = st.number_input("LABOUR", min_value=0.0, value=1587.691604, format="%.6f")

with col2:
    oil = st.number_input("OIL", min_value=0.0, value=47.3762619, format="%.7f")
    brass = st.number_input("BRASS", min_value=0.0, value=22.0358699, format="%.7f")
    import_export = st.number_input("IMPORT AND EXPORTS", min_value=0.0, value=0.0, format="%.1f")
    commission = st.number_input("COMMISSION", min_value=0.0, value=0.0, format="%.1f")

st.write("---")

# แยกส่วนบรรจุภัณฑ์ตามขนาดที่เลือก
st.header("3. เลือกขนาดบรรจุภัณฑ์")
package_size = st.radio("ขนาดบรรจุภัณฑ์:", ["25kg", "50kg"], horizontal=True)

if package_size == "25kg":
    packaging = st.number_input("PACKAGING (PALLET, BAG) สำหรับ 25kg", min_value=0.0, value=414.50, format="%.2f")
else:
    packaging = st.number_input("PACKAGING (PALLET, BAG) สำหรับ 50kg", min_value=0.0, value=476.00, format="%.2f")

# ==========================================
# ส่วนที่ 3: คำนวณผลลัพธ์สุทธิ
# ==========================================
st.write("---")
st.header("📋 สรุปผลการคำนวณ")

# คำนวณ All Cost (No Material)
all_cost_no_material = (
    maintenance + electricity + water_section + labour + 
    packaging + oil + brass + import_export + commission
)

# คำนวณต้นทุนรวมทั้งหมด (Material + All Cost)
total_cost = calculated_material_cost + all_cost_no_material

# แสดงผลลัพธ์ในรูปแบบการ์ดที่สวยงาม
res_col1, res_col2 = st.columns(2)

with res_col1:
    st.metric(
        label="ALL COST (NO MATERIAL)", 
        value=f"{all_cost_no_material:,.6f}"
    )

with res_col2:
    st.metric(
        label="🔥 TOTAL COST (รวมวัตถุดิบและสูญเสียแล้ว)", 
        value=f"{total_cost:,.6f}"
    )

# ทำแถบไฮไลท์สีเหลืองเหมือนใน Excel สำหรับต้นทุนรวมสุทธิ
st.markdown(
    f"""
    <div style="background-color: #FFFF00; padding: 15px; border-radius: 5px; text-align: center;">
        <h3 style="color: black; margin: 0;">ต้นทุนรวมสุทธิ ({package_size}): {total_cost:,.6f}</h3>
    </div>
    """, 
    unsafe_style_allowed=True
)
