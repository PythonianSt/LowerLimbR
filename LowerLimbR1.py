import streamlit as st

st.set_page_config(
    page_title="Lower Limb",
    page_icon="🩺",
    layout="centered"
)

st.title("Lower Limb")
st.caption("Doctor Quick Reminder • Rule-based • No AI")

st.warning(
    "Concise clinical reminder only. Use clinical judgment and local referral guidelines."
)

tab1, tab2 = st.tabs(["🚩 Red Flags", "🧠 Differential Diagnoses"])

with tab1:
    st.subheader("Red Flags")

    st.markdown("""
### Trauma
- Suspected fracture or dislocation
- Unable to bear weight
- Open wound or severe crush injury
- Neurovascular compromise

### Vascular
- Cold, pale, pulseless limb
- Acute severe calf pain or swelling
- Suspected DVT
- Severe pain out of proportion

### Infection
- Rapidly spreading redness or swelling
- Fever with severe limb pain
- Abscess or necrotic skin
- Diabetic foot infection

### Neurologic
- New foot drop
- Progressive weakness or numbness
- Saddle anesthesia or bladder/bowel symptoms

### Others
- Persistent night pain
- Unexplained weight loss
- Enlarging mass
""")

with tab2:
    st.subheader("Differential Diagnoses")

    st.markdown("""
### Hip / Thigh
- Muscle strain
- Hip osteoarthritis
- Trochanteric pain syndrome
- Femoral fracture
- Meralgia paresthetica

### Knee
- Knee sprain
- Meniscus injury
- Ligament injury
- Patellofemoral pain
- Osteoarthritis
- Bursitis

### Leg / Calf
- Muscle strain
- Shin splints
- DVT
- Cellulitis
- Chronic venous disease

### Ankle / Foot
- Ankle sprain
- Plantar fasciitis
- Achilles tendinopathy
- Gout
- Stress fracture
- Diabetic foot problem

### Nerve / Referred Pain
- Lumbar radiculopathy
- Sciatica
- Peripheral neuropathy
- Myofascial pain syndrome
""")

st.divider()

st.caption(
    "KU KPS Pain Consult • Doctor QR • No AI • No data collection"
)
