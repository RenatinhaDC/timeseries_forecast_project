import streamlit as st
import panda as pd

from prophet import Prophet

#Importing the data

walmart_cleaned = pd.read_csv("walmart_cleaned.csv")

#Creating the function

def forecast(walmart_cleaned):
    # Creating a Prophet model
    m = Prophet()

    # Fitting the model to the data
    m.fit(walmart_cleaned)

    # Making future predictions
    future = m.make_future_dataframe(periods=365)
    forecast = m.predict(future)

    #Return the forecast DataFrame
    return forecast


#Streamlit app

def main():
  # Set Streamlit app title and description
  st.title('Time Series Forecasting App')
  st.write('My Forecast Data.')

  forecast_data = forecast(walmart_cleaned)

  # Display the forecast output
  st.dataframe(forecast_data)
if __name__ == '__main__':
main()

streamlit run forecast_app.py


