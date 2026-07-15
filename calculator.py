import streamlit as st

# Page configuration for a beautiful layout
st.set_page_config(page_title="Neo-Blue Calculator", page_icon="🧮", layout="centered")

# Custom CSS for Premium Animations
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f0f4f8 0%, #dbeafe 100%);
    }
    div.stButton > button {
        width: 100%;
        height: 60px;
        font-size: 20px !important;
        font-weight: 600;
        background-color: #ffffff;
        color: #1e293b;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    }
    div.stButton > button:hover {
        transform: translateY(-3px);
        background-color: #2563eb !important;
        color: white !important;
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3);
    }
    div.stButton > button:active {
        transform: scale(0.95);
    }
    .display-box {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 24px;
        text-align: right;
        font-size: 36px;
        font-weight: 300;
        color: #1e293b;
        margin-bottom: 24px;
        border: 2px solid #3b82f6;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧮 Neo-Blue Calculator")

# State Management for Calculator
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Display
st.markdown(f'<div class="display-box">{st.session_state.expression if st.session_state.expression else "0"}</div>', unsafe_allow_html=True)

# Grid Layout
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("C"):
        st.session_state.expression = ""
        st.rerun()
with col2:
    if st.button("⌫"):
        st.session_state.expression = st.session_state.expression[:-1]
        st.rerun()
with col3:
    if st.button("%"):
        st.session_state.expression += "%"
        st.rerun()
with col4:
    if st.button("÷"):
        st.session_state.expression += "/"
        st.rerun()

# Numbers and Operators Rows
rows = [
    ('7', '8', '9', '*'),
    ('4', '5', '6', '-'),
    ('1', '2', '3', '+'),
    ('0', '.', '=', None)
]

for row in rows:
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button(row[0]): st.session_state.expression += row[0]; st.rerun()
    with c2:
        if st.button(row[1]): st.session_state.expression += row[1]; st.rerun()
    with c3:
        if row[2] == "=":
            if st.button("="):
                try:
                    # Calculate percentage dynamically
                    expr = st.session_state.expression.replace('%', '/100')
                    st.session_state.expression = str(eval(expr))
                except:
                    st.session_state.expression = "Error"
                st.rerun()
        else:
            if st.button(row[2]): st.session_state.expression += row[2]; st.rerun()
    with c4:
        if row[3]:
            if st.button(row[3]): st.session_state.expression += row[3]; st.rerun()
