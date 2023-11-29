import streamlit as st

st.set_page_config(
    page_title="Welcome To Sales Forecasting  Walmart App",
    page_icon="😃",
    layout="wide"
)

# Add content to your Streamlit app
st.markdown("# 👋 Welcome To Walmart Sales Forecasting App ")

# Display the waving GIF
st.image("https://www.animatedimages.org/data/media/1645/animated-waving-image-0090.gif")

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
st.write('<div class="slide-in-animation">This app is using ARIMA model to forecast  sales of 45 Walmart stores....................</div>', unsafe_allow_html=True)

#add a sidebar to select pages
st.sidebar.success("Select a page above.")