import streamlit as st

st.set_page_config(
    page_title="Welcome To Sales Forecasting  Walmart App",
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
st.write('<div class="slide-in-animation">This app is using ARIMA model to forecast  sales of 45 Walmart stores....................</div>', unsafe_allow_html=True)

#add a sidebar to select pages
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



about = st.container()
with about:
    st.title("Who are we?")

    # Set team image and resize it
    #image = Image.open('Team logo/MicrosoftTeams-image (2).jpg.png')
    #new_size = (1080, 722)
    #resized_image = image.resize(new_size)
    #st.image(resized_image)

    # Add information about the team members (as described in your code)