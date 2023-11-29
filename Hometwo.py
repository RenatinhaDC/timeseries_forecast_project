

import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from pmdarima import auto_arima
import sys
print(sys.version)

# Load the ARIMA model and other necessary objects
arima_model = joblib.load('arima_model.joblib')
train_size = joblib.load('train_size.joblib')
train_data = joblib.load('train_data.joblib')

def forecast_sales(ts_data, num_periods):
    # Split your time series data into training and validation sets
    train_size = int(len(ts_data) * 0.75)
    train_data, validation_data = ts_data[:train_size], ts_data[train_size:]

    # Forecast the specified number of periods
    forecast_periods = num_periods * 4  
    forecast = arima_model.predict(n_periods=forecast_periods)

    # Measure accuracy on the validation data
    mae = mean_absolute_error(validation_data, forecast)
    mse = mean_squared_error(validation_data, forecast)
    rmse = np.sqrt(mse)
    percentage_error = np.mean(np.abs((validation_data - forecast) / validation_data)) * 100

    st.write(f'Mean Absolute Error: {mae}')
    st.write(f'Mean Squared Error: {mse}')
    st.write(f'Root Mean Squared Error: {rmse}')
    st.write(f'Percentage Error: {percentage_error}%')

    # Visualize actual vs. forecast with training and validation data
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(train_data.index, train_data, label='Training Data', linewidth=2)
    ax.plot(validation_data.index, validation_data, label='Actual Validation Data', linestyle='--', linewidth=2)
    ax.plot(pd.date_range(start=validation_data.index[-1], periods=num_periods + 1, freq='W')[1:], forecast,
            label='Forecasted Data', linestyle='--', linewidth=2) 
    ax.set_xlabel('Date')
    ax.set_ylabel('Your Y-axis label')
    ax.legend()
    ax.grid(True)

    # Show the plot using Streamlit
    st.pyplot(fig)

# Streamlit app
st.set_page_config(
    page_title="Welcome To Sales Forecasting Walmart App",
    page_icon="😃",
    layout="wide"
)

# Add content to your Streamlit app
st.markdown("# 👋 Welcome To Walmart Sales Forecasting App ")

# Display the waving GIF
st.image("https://www.animatedimages.org/img-animated-cat-image-0516-58883.htm")

# Add CSS for animation
st.write("""
    <style>
        @keyframes slide-in {
            0% {
                transform: translateX(-100%);
            }
            100% {
                transform: translateX(0);
            }
        }
        .slide-in-animation {
            animation: slide-in 1.5s ease-in-out;
        }
    </style>
""", unsafe_allow_html=True)

# Text with animation
st.write('<div class="slide-in-animation">This app is using ARIMA model to forecast sales of 45 Walmart stores....................</div>', unsafe_allow_html=True)

# Add a sidebar to select pages
st.sidebar.success("Select a page above.")

subheader_container = st.container()

subheader_content = """
<div class="slide-in-animation">
<h3>What should you expect:</h3>
<ul>
  <li>Forecast Sales of 45 Walmart Stores</li>
  <li>View the dataset and interact with a visual showing sales across stores</li>
  <li>Get to know more about the team</li>
</ul>
</div>
"""

subheader_container.markdown(subheader_content, unsafe_allow_html=True)

# Add CSS for animation
st.write("""
<style>
    @keyframes slide-in {
        0% {
            transform: translateX(-100%);
        }
        100% {
            transform: translateX(0);
        }
    }
    .slide-in-animation {
        animation: slide-in 1.5s ease;
    }
</style>
""", unsafe_allow_html=True)

# Display the forecast input and button
forecast_container = st.container()
with forecast_container:
    st.title("Sales Forecasting")

    # User input for the number of forecasted periods
    num_periods = st.slider("Number of Forecasted Periods", min_value=1, max_value=12, value=6)

    # Button to trigger the forecast
    if st.button("Generate Forecast"):
        forecast_sales(train_data, num_periods)

about = st.container()
with about:
    st.title("Who are we?")
