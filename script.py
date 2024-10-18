import streamlit as st
import time

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit App
def main():
    # Custom CSS for styling the background, text, and layout
    st.markdown(
        """
        <style>
        body {
            background-image: url('https://www.publicdomainpictures.net/pictures/320000/velka/plain-white-background.jpg');
            background-size: cover;
        }
        .stApp {
            background: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            padding: 20px;
        }
        h1 {
            color: #ff6347;
            font-family: 'Arial', sans-serif;
            text-align: center;
            font-weight: bold;
        }
        .stRadio > div {
            display: flex;
            justify-content: center;
            color: #ff6347;
        }
        .stNumberInput input {
            background-color: #eef7fa;
        }
        .stButton button {
            background-color: #ff6347;
            color: white;
            font-weight: bold;
            border-radius: 10px;
        }
        .stButton button:hover {
            background-color: #ff8566;
        }
        .stSuccess {
            background-color: #d4edda;
            font-weight: bold;
            font-size: large;
            text-align: center;
            color: #155724;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # Title and description with updated style
    st.title("🌡️ Enhanced Temperature Converter 🌡️")
    st.markdown("<h3 style='text-align: center;'>Convert between Celsius and Fahrenheit easily!</h3>", unsafe_allow_html=True)
    
    # Input options for conversion type
    option = st.radio("Choose conversion:", 
                      ("Convert Celsius to Fahrenheit", "Convert Fahrenheit to Celsius"))

    # Get temperature input and perform conversion based on the user's choice
    if option == "Convert Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:", value=0.0, step=0.1)
        if st.button("Convert 🌡️"):
            with st.spinner('Converting...'):
                time.sleep(1)
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.success(f"{celsius}°C is {fahrenheit:.2f}°F")

    elif option == "Convert Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:", value=32.0, step=0.1)
        if st.button("Convert ❄️"):
            with st.spinner('Converting...'):
                time.sleep(1)
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.success(f"{fahrenheit}°F is {celsius:.2f}°C")

    

# Run the app
if __name__ == "__main__":
    main()
