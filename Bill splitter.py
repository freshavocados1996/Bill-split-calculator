import streamlit as st

# 1. Page Setup
st.set_page_config(page_title="Bill Splitter", page_icon="🧾")
st.title("Bill Splitter")

# 2. Reset Function
def reset_values():
    st.session_state["bill"] = 0.0
    st.session_state["tip"] = 15
    st.session_state["tax"] = 0.0
    st.session_state["people"] = 1

# 3. Input Layout (Using columns for a compact UI)
col1, col2 = st.columns(2)

with col1:
    bill = st.number_input("Bill Amount ($)", min_value=0.0, step=0.01, key="bill")
    tax_perc = st.number_input("Tax Percentage (%)", min_value=0.0, step=0.1, key="tax")

with col2:
    tip_perc = st.slider("Tip Percentage (%)", 0, 100, 15, key="tip")
    people = st.number_input("Number of People", min_value=1, step=1, key="people")

# 4. Action Buttons
btn_col1, btn_col2 = st.columns([1, 4])
with btn_col1:
    calculate = st.button("Calculate", type="primary")
with btn_col2:
    st.button("Reset All", on_click=reset_values)

# 5. Calculation Logic
if calculate:
    tax_amount = bill * (tax_perc / 100)
    tip_amount = bill * (tip_perc / 100)
    total = bill + tax_amount + tip_amount
    split = total / people

    st.divider()
    
    # Summary Table for professional look
    st.write(f"**Base Bill:** ${bill:.2f}")
    st.write(f"**Tax ({tax_perc}%):** ${tax_amount:.2f}")
    st.write(f"**Tip ({tip_perc}%):** ${tip_amount:.2f}")
    st.subheader(f"Grand Total: ${total:.2f}")
    st.success(f"### Each Person Pays: **${split:.2f}**")