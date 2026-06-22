import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเพจ Streamlit
st.set_page_config(
    page_title="Industrial Mineral ERP Blueprint",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# สไตล์ตกแต่งเพิ่มเติม
st.markdown("""
<style>
    .reportview-container .main .block-container{ max-width: 95%; }
    .stAlert p { font-size: 16px; }
    h1, h2, h3 { color: #1E3A8A; }
    .highlight-box { background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 5px solid #1E3A8A; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

# หัวข้อหลัก
st.title("🏭 Detailed ERP System Blueprint for Mineral Processing Plant")
st.caption("Role: Enterprise Resource Planning (ERP Architecture) & Manufacturing IT Consultant")

# ส่วนข้อมูลจำเพาะของโรงงาน (Context)
with st.sidebar:
    st.header("⚙️ Factory Profile")
    st.info("""
    - **ประเภทอุตสาหกรรม:** โรงงานแต่งแร่ (Baryte, Calcite, Talc)
    - **รูปแบบการผลิต:** Hybrid (Make-to-Stock / Make-to-Order)
    - **ขนาดองค์กร:** ~45 คน (SME High-Efficiency)
    - **กระบวนการหลัก:** Crushing, Grinding, Milling, Sizing (Mesh), Packing
    """)
    st.write("---")
    st.markdown("### 📌 สถาปัตยกรรมนี้มุ่งเน้น:")
    st.markdown("- **ความแม่นยำของ Specific Gravity (SG) และ Mesh Size**")
    st.markdown("- **การควบคุมการสึกหรอของเครื่องจักร (Raymond Mill)**")
    st.markdown("- **การตามสอบย้อนกลับ (Lot Traceability)**")

# ส่วนเนื้อหาหลัก แบ่งเป็น 4 Tabs ตามที่กำหนด
tab1, tab2, tab3, tab4 = st.tabs([
    "1. Core Modules & Sub-modules", 
    "2. Data Structure & Database", 
    "3. Workflow & Integration", 
    "4. Dashboards & KPIs"
])

# ==========================================
# TAB 1: CORE MODULES
# ==========================================
with tab1:
    st.header("1. โมดูลหลักและระบบย่อย (Core Modules & Sub-modules)")
    st.write("ฟังก์ชันการทำงานที่เจาะลึกเฉพาะทางอุตสาหกรรมแต่งแร่ (Mineral Processing)")

    with st.expander("📊 1.1 Production Planning & Control (PPC)", expanded=True):
        st.markdown("""
        * **Master Production Schedule (MPS):** วางแผนการผลิตแร่มาตรฐาน (เช่น Calcite 800 Mesh, Baryte SG 4.20) เป็นแบบ *Make-to-Stock (MTS)* โดยคำนวณจาก Forecast และกำหนด Min/Max Stock ส่วนแร่คุณสมบัติพิเศษ (Custom Mesh/Chemical-treated) ให้วางแผนแบบ *Make-to-Order (MTO)*
        * **Material Requirements Planning (MRP):** คำนวณหาปริมาณแร่ดิบ (Run-of-Mine: ROM) ที่ต้องเบิกจากสต็อกหรือสั่งซื้อเพิ่ม โดยต้องคำนวณ **Yield Loss %** (เช่น อัตราสูญเสียในเครื่องบด 3-5% เป็นฝุ่นแร่)
        * **Capacity Planning (Finite Capacity):** คำนวณกำลังการผลิตของเครื่องจักรหลัก เช่น เครื่องบด (Raymond Mill, Ball Mill) และเครื่องคัดขนาด (Classifier) โดยคิดตามอัตราการไหล (Ton/Hour) ตามความแข็งของแร่แต่ละประเภท (Mohs Scale)
        """)

    with st.expander("📦 1.2 Inventory & Warehouse Management (WMS)"):
        st.markdown("""
        * **Lot/Batch Number Tracking:** **(สำคัญมาก)** แร่ที่ผลิตต้องล็อกเบอร์ Lot ตามแหล่งที่มาของสินแร่ดิบ (Mine Source/Pit) และวันเวลาที่ผลิต เพื่อควบคุมค่า Specific Gravity (SG) และความขาว (Whiteness)
        * **การตัดสต็อกแบบ FIFO:** บังคับใช้ระบบ FIFO กับสินค้าสำเร็จรูป (Finished Goods - FG) เพื่อป้องกันแป้งแร่จับตัวเป็นก้อนหากเก็บไว้นานเกินไป (Caking Problem)
        * **Barcode Tracking:** พิมพ์บาร์โค้ดแปะที่ถุง Jumbo Bag (1-2 ตัน) หรือถุงเล็ก (25/50 กก.) ตั้งแต่หน้าเครื่องบรรจุ เพื่อสแกนรับเข้าคลังและสแกนจ่ายออกตอนขึ้นรถขนส่ง
        * **Reorder Point (ROP):** ตั้งระบบแจ้งเตือนเมื่อแร่ก้อน (Crushed Ore) ใน Silo ลดลงถึงจุดวิกฤต
        """)

    with st.expander("🛒 1.3 Procurement & Supplier Management"):
        st.markdown("""
        * **Purchase Requisition (PR) & Purchase Order (PO):** ระบบอนุมัติใบซื้อแร่ดิบ (ROM) และเคมีภัณฑ์ขัดผิวแร่ รองรับการสั่งซื้อตามน้ำหนักชั่งหน้าโรงงาน (Weighbridge Integration)
        * **Vendor Evaluation:** ประเมินคุณภาพผู้จัดส่งสินแร่ดิบ โดยตัดคะแนนหากส่งแร่ที่มีสิ่งเจือปนสูง (เช่น หินปน, ค่า Silica สูงเกินกำหนด) หรือค่าความบริสุทธิ์ไม่ผ่านเกณฑ์
        """)

    with st.expander("🔬 1.4 Quality Control & Assurance (QC/QA)"):
        st.markdown("""
        * **Inbound Quality Control (IQC):** บันทึกผลทดสอบแร่ดิบก่อนดัมพ์ลงลานแร่ (ตรวจสอบค่าความหนาแน่น SG, ความชื้น %, และสารเจือปน)
        * **In-Process Quality Control (IPQC):** สุ่มตรวจทุกๆ 1-2 ชั่วโมงที่หน้าเครื่องบด (ตรวจสอบความละเอียด Mesh Size ด้วยเครื่อง Laser Diffraction และทดสอบ Whiteness)
        * **Finished Quality Control (FQC):** ตรวจสอบขั้นสุดท้ายก่อนปิดปากถุง พร้อมระบบออกใบ **Certificate of Analysis (COA)** แนบไปกับรถส่งสินค้าอัตโนมัติ
        * **Defect Management:** หากแร่ไม่ได้มาตรฐาน (Off-spec) ให้ระบบล็อกสถานะ Blocked ห้ามจ่าย และทำ Workflow สำหรับนำไปบดซ้ำ (Rework) หรือขายเป็นเกรดต่ำ (Off-grade)
        """)

    with st.expander("🛠️ 1.5 Plant Maintenance (PM)"):
        st.markdown("""
        * **Preventive Maintenance (PM):** วางตารางซ่อมบำรุงเชิงป้องกันอัตโนมัติสำหรับชิ้นส่วนที่สึกหรอสูง เช่น ลูกกลิ้งบด (Grinding Roller), แหวนบด (Die Ring) ของ Raymond Mill, และผ้ากรองฝุ่น (Bag Filter) ตามชั่วโมงการทำงาน (Running Hours)
        * **Breakdown Maintenance:** ระบบแจ้งซ่อมด่วนผ่านมือถือสำหรับช่างซ่อมบำรุง พร้อมตัดสต็อกอะไหล่สำรอง (เช่น สายพานลำเลียง, ตลับลูกปืน)
        """)

    with st.expander("💰 1.6 Sales, Distribution & Finance"):
        st.markdown("""
        * **Sales Order & Quotation:** รองรับราคาสินค้าตามปริมาณการสั่งซื้อ (Tier Pricing) และระบุเงื่อนไขการส่งมอบ (Incoterms) เช่น Ex-work, FOB
        * **Actual Costing:** คำนวณต้นทุนจริงราย Batch โดยรวม **ค่าแร่ดิบ + ค่าไฟเครื่องจักร (Energy Cost มหาศาลในโรงบด) + ค่าสึกหรออะไหล่ + ค่าแรง** เทียบกับ Standard Cost เพื่อหา Cost Variance
        """)

# ==========================================
# TAB 2: DATA STRUCTURE
# ==========================================
with tab2:
    st.header("2. โครงสร้างข้อมูลและฐานข้อมูล (Data Structure & Key Entities)")
    
    st.subheader("💡 2.1 Master Data Specifications")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        ### **Item Master**
        * `item_id` (PK)
        * `item_name` (e.g., Calcite Powder 1250 Mesh)
        * `item_type` (ROM / WIP / FG / Spare-Part)
        * `base_uom` (Ton / KG)
        * `target_sg` (Specific Gravity)
        * `target_mesh` (Target Fineness)
        """)
    with col2:
        st.markdown("""
        ### **Multi-level BOM**
        * **Level 0:** Finished Good (e.g., Talc Powder Premium 25kg Bag)
        * **Level 1:** WIP (Talc Powder Unpacked) + Packaging (Jumbo Bag/Paper Bag)
        * **Level 2:** Raw Material (Talc Lump Grade A) + Chemical Additives
        """)
    with col3:
        st.markdown("""
        ### **Routing & Work Center**
        * **WC-01:** Primary Jaw Crusher (หยาบ)
        * **WC-02:** Raymond Mill 01 (บดละเอียด)
        * **WC-03:** Auto-Packing Machine (บรรจุถุง)
        * *บันทึก Standard Rate: เช่น 5 ตัน/ชั่วโมง*
        """)

    st.write("---")
    st.subheader("📊 2.2 Entity Relationship Diagram (Table Schema Relational)")
    
    # แสดงโครงสร้างตารางข้อมูลเพื่อให้นักพัฒนานำไปสร้าง SQL
    st.code("""
TABLE: item_master {
    item_code VARCHAR(30) [PK]
    description VARCHAR(100)
    item_type VARCHAR(10) // ROM, WIP, FG, PKG
    unit_of_measure VARCHAR(10)
    safety_stock DECIMAL(12,2)
}

TABLE: bill_of_materials {
    bom_id VARCHAR(30) [PK]
    parent_item_code VARCHAR(30) [FK -> item_master.item_code]
    component_item_code VARCHAR(30) [FK -> item_master.item_code]
    quantity_required DECIMAL(12,4) // อัตราส่วนผสมแร่และเคมี
    scrap_factor DECIMAL(4,2) // % การสูญเสียในกระบวนการ
}

TABLE: production_order {
    production_order_no VARCHAR(30) [PK]
    sales_order_no VARCHAR(30) [NULLABLE] // Link ถ้าเป็น MTO
    item_code VARCHAR(30) [FK -> item_master.item_code]
    qty_planned DECIMAL(12,2)
    qty_completed DECIMAL(12,2)
    start_date DATETIME
    status VARCHAR(15) // RELEASED, WIP, QC_HOLD, CLOSED
}

TABLE: stock_transaction {
    transaction_id BIGINT [PK]
    production_order_no VARCHAR(30) [FK -> production_order.production_order_no]
    item_code VARCHAR(30) [FK -> item_master.item_code]
    lot_number VARCHAR(50) // รูปแบบ: YYYYMMDD-BATCH-MACHINE
    qty_moved DECIMAL(12,2)
    from_location VARCHAR(20)
    to_location VARCHAR(20)
    timestamp DATETIME
}
    """, language="sql")

# ==========================================
# TAB 3: WORKFLOW & INTEGRATION
# ==========================================
with tab3:
    st.header("3. กระบวนการทำงานและการเชื่อมต่อ (Workflow & Integration)")
    
    st.subheader("🔄 3.1 End-to-End Core Workflow")
    st.markdown("""
    ```
    [ ลูกค้าสั่งซื้อ / Forecast ] 
          │
          ▼
    [ วางแผน MRP / เช็คสต็อกแร่ก้อน & ถุงบรรจุ ]
          │
          ▼
    [ ชั่งน้ำหนักแร่ดิบขาเข้า (Weighbridge) ] ──> บันทึก Lot ตามหน้าเหมือง ──> [ เก็บเข้าลานแร่ ]
          │
          ▼
    [ ปล่อย Production Order ] ──> จ่ายแร่เข้าเครื่องบด (Raymond Mill)
          │
          ▼
    [ IPQC สุ่มตรวจ Mesh Size ทุก 2 ชม. ] ── ถ้า Off-spec ──> [ สั่ง Rework / แยกเกรด ]
          │
          ▼
    [ เข้าเครื่องบรรจุอัตโนมัติ ] ──> สแกนบาร์โค้ดติดถุง (FG Lot Generated)
          │
          ▼
    [ ชั่งน้ำหนักรถขนส่งขาออก ] ──> พิมพ์ใบกำกับภาษี & ใบ COA ──> [ ส่งมอบสินค้า ]
    ```
    """)
    
    st.write("---")
    st.subheader("🔌 3.2 Machine Integration Architecture (IoT/SCADA to ERP)")
    st.markdown("""
    สำหรับโรงงานขนาด 45 คน **ไม่จำเป็นต้องใช้ระบบ MES ขนาดใหญ่** แต่ให้ใช้วิธี **Lightweight IoT Integration** แทน เพื่อประหยัดงบประมาณและได้ประสิทธิภาพสูงสุด:
    """)
    
    st.info("""
    * **Weighbridge Integration:** เชื่อมต่อเครื่องชั่งน้ำหนักรถบรรทุกผ่านพอร์ต Serial (RS232/RS485) หรือ LAN ดึงข้อมูลน้ำหนักแร่ดิบเข้าสู่ใบรับสินค้า (Goods Receipt) ใน ERP โดยตรงเพื่อป้องกันทุจริต
    * **PLC/SCADA Counter Integration:** ดึงข้อมูลจาก PLC ของเครื่องบรรจุถุง (เช่น ปริมาณถุงที่แพ็คเสร็จ) ผ่านโปรโตคอล **OPC UA หรือ MQTT** ยิงตรงเข้าสู่ตาราง `stock_transaction` ใน ERP แบบ Real-time เพื่อตัดยอดผลผลิต
    * **Energy Monitoring Integration:** ติดตั้ง Smart Meter ที่ตู้ไฟของเครื่องบดแร่ ส่งค่าการใช้พลังงาน (kWh) เข้า ERP เพื่อนำไปคำนวณต้นทุน **Actual Energy Cost Per Ton** ได้แม่นยำ
    """)

# ==========================================
# TAB 4: DASHBOARDS & KPIS
# ==========================================
with tab4:
    st.header("4. รายงานและแดชบอร์ดบริหาร (Dashboards & KPIs)")
    st.write("ตัวชี้วัดที่ออกแบบมาสำหรับผู้บริหารและผู้จัดการโรงงานแต่งแร่")

    # จำลองข้อมูลเพื่อสร้างกราฟตัวอย่างใน Streamlit
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Real-time Production Yield vs Loss")
        chart_data = pd.DataFrame({
            'Mineral Type': ['Baryte SG 4.2', 'Calcite 800M', 'Calcite 1250M', 'Talc Premium'],
            'Good Product (Tons)': [120, 85, 60, 40],
            'Dust/Scrap Loss (Tons)': [3, 4, 5, 2]
        }).set_index('Mineral Type')
        st.bar_chart(chart_data)
        st.caption("สูญเสียฝุ่นแร่ (Dust Loss) ต้องไม่เกิน 5% ในกระบวนการบดละเอียด")

    with col2:
        st.subheader("⚡ Overall Equipment Effectiveness (OEE) Tracking")
        oee_data = pd.DataFrame({
            'Machine': ['Crusher 01', 'Raymond Mill 01', 'Raymond Mill 02', 'Packing Line'],
            'OEE %': [88, 72, 65, 90]
        }).set_index('Machine')
        st.bar_chart(oee_data, y="OEE %")
        st.caption("หมายเหตุ: Raymond Mill มักมี OEE ต่ำเนื่องจากต้องหยุดเปลี่ยนอะไหล่สึกหรอบ่อย (Target: >75%)")

    st.write("---")
    st.subheader("📋 รายการรายงานสำคัญระดับบริหาร (Executive Reports)")
    
    st.markdown("""
    1. **Inventory Turnover by Lot Number:** แสดงอายุของแป้งแร่ในคลัง ป้องกันแร่เสื่อมสภาพหรือจับตัวเป็นก้อนแข็ง (Caking)
    2. **Cost Variance Analysis Report:** รายงานเปรียบเทียบต้นทุนที่ตั้งไว้ กับต้นทุนจริง (ค่าไฟฟ้า + ค่าสารเคมี + ค่าแร่ดิบ) เพื่อดูว่าเครื่องจักรบดแร่กินไฟเกินมาตรฐานหรือไม่
    3. **Quality Compliance Rate & COA History:** อัตราการผ่านการตรวจ QC ในครั้งแรก (First Pass Yield) และประวัติการออกใบ COA ย้อนหลังตามเลข Lot ของลูกค้า
    4. **Preventive Maintenance Compliance:** เปรียบเทียบแผน PM เครื่องบด กับการซ่อมบำรุงที่เกิดขึ้นจริง เพื่อลดอัตราการเกิดเครื่องจักรหยุดทำงานฉุกเฉิน (Unplanned Downtime)
    """)

# ส่วนท้ายหน้าเพจ
st.write("---")
st.caption("⚙️ ERP System Blueprint Document - Ready for System Analyst and Software Development Team Spec.")
