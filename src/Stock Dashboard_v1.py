# Removed the erroneous "StockDashboard_v1" line and fixed import statements
import streamlit as st
import plotly.express as pl
import pandas as pd
import numpy as np
import yfinance as yf

# Title Mansa Capital Stock Dashboard
st.title('Mansa Capital Stock Dashboard'),

# Create sample stock data
stock_data = pd.DataFrame({
    'Data':pd.date_range(start='2023-01-01', periods=100),
        'Price':np.random.randn(100),
        'company':['Mansa Capital']*100  
    })
    
