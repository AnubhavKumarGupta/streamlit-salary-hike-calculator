import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Salary Hike Calculator",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .calculator-container {
        background: rgba(255, 255, 255, 0.95);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
        margin: 20px 0;
    }
    
    .title {
        text-align: center;
        color: #000000;
        font-size: 3em;
        font-weight: 700;
        margin-bottom: 10px;
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2em;
        margin-bottom: 30px;
        font-weight: 400;
    }
    
    .result-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin: 30px 0;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .result-label {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.2em;
        font-weight: 500;
        margin-bottom: 10px;
    }
    
    .result-value {
        color: white;
        font-size: 3.5em;
        font-weight: 700;
        margin: 10px 0;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    
    .positive {
        color: #4ade80;
    }
    
    .negative {
        color: #f87171;
    }
    
    .info-card {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        border-left: 4px solid #667eea;
    }
    
    .info-row {
        display: flex;
        justify-content: space-between;
        margin: 10px 0;
        font-size: 1.1em;
    }
    
    .info-label {
        color: #666;
        font-weight: 500;
    }
    
    .info-value {
        color: #333;
        font-weight: 600;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 15px 40px;
        font-size: 1.1em;
        font-weight: 600;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.6);
    }
    
    .stNumberInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 12px;
        font-size: 1.1em;
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    .footer {
        text-align: center;
        color: white;
        margin-top: 40px;
        padding: 20px;
        font-size: 0.9em;
        opacity: 0.8;
    }
    
    .emoji {
        font-size: 1.5em;
        margin-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">💰 Salary Hike Calculator</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Calculate your salary increment percentage</p>', unsafe_allow_html=True)

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Old Salary")
    old_salary = st.number_input(
        "Enter your current salary",
        min_value=0.0,
        value=50000.0,
        step=1000.0,
        format="%.2f",
        key="old_salary",
        label_visibility="collapsed"
    )

with col2:
    st.markdown("### 📈 New Salary")
    new_salary = st.number_input(
        "Enter your new salary",
        min_value=0.0,
        value=60000.0,
        step=1000.0,
        format="%.2f",
        key="new_salary",
        label_visibility="collapsed"
    )

# Add some space
st.markdown("<br>", unsafe_allow_html=True)

# Calculate button
if st.button("🎯 Calculate Hike", use_container_width=True):
    if old_salary <= 0:
        st.error("⚠️ Old salary must be greater than 0!")
    elif new_salary < 0:
        st.error("⚠️ New salary cannot be negative!")
    else:
        # Calculate hike
        hike_amount = new_salary - old_salary
        hike_percentage = (hike_amount / old_salary) * 100
        
        # Determine if it's a hike or cut
        is_positive = hike_percentage >= 0
        emoji = "📈" if is_positive else "📉"
        color_class = "positive" if is_positive else "negative"
        
        # Display results
        st.markdown(f"""
            <div class="result-card">
                <div class="result-label">{emoji} Your Salary {'Hike' if is_positive else 'Change'} Percentage</div>
                <div class="result-value {color_class}">{hike_percentage:+.2f}%</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Additional information
        st.markdown(f"""
            <div class="info-card">
                <div class="info-row">
                    <span class="info-label">💵 Old Salary:</span>
                    <span class="info-value">₹{old_salary:,.2f}</span>
                </div>
                <div class="info-row">
                    <span class="info-label">💰 New Salary:</span>
                    <span class="info-value">₹{new_salary:,.2f}</span>
                </div>
                <div class="info-row">
                    <span class="info-label">{'➕' if is_positive else '➖'} Difference:</span>
                    <span class="info-value {color_class}">₹{hike_amount:+,.2f}</span>
                </div>
                <div class="info-row">
                    <span class="info-label">📊 Hike Percentage:</span>
                    <span class="info-value {color_class}">{hike_percentage:+.2f}%</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Motivational message
        if hike_percentage > 20:
            st.success("🎉 Excellent! That's a fantastic hike!")
        elif hike_percentage > 10:
            st.success("👍 Great! That's a good increment!")
        elif hike_percentage > 0:
            st.info("✨ That's a positive change!")
        elif hike_percentage == 0:
            st.warning("⏸️ No change in salary")
        else:
            st.warning("⚠️ This is a salary reduction")

# Quick calculate on input change
else:
    if old_salary > 0 and new_salary >= 0:
        hike_percentage = ((new_salary - old_salary) / old_salary) * 100
        st.markdown(f"""
            <div style="text-align: center; padding: 20px; color: white; font-size: 1.2em;">
                <span style="opacity: 0.8;">Quick Preview: </span>
                <span style="font-weight: 700; font-size: 1.4em;">{hike_percentage:+.2f}%</span>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        Made with ❤️ using Streamlit<br>
        Track your career growth • Plan your future
    </div>
""", unsafe_allow_html=True)
