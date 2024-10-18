import streamlit as st
import time

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit App
def main():
    # Custom CSS for beautiful background and glassmorphism
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        body {
            font-family: 'Poppins', sans-serif;
        }
        .main {
            background: url('https://images.unsplash.com/photo-1496307042754-b4aa456c4a2d?fit=crop&w=1800&q=80');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .stApp {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            backdrop-filter: blur(15px);
            padding: 40px;
            max-width: 500px;
            margin: auto;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        }
        h1 {
            color: white;
            text-shadow: 1px 1px 5px rgba(0,0,0,0.3);
            font-family: 'Poppins', sans-serif;
            text-align: center;
            font-weight: bold;
        }
        h3 {
            color: white;
            font-family: 'Poppins', sans-serif;
            text-align: center;
        }
        .stNumberInput input {
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            color: white;
            border: 2px solid #fff;
            text-align: center;
            font-weight: bold;
        }
        .stButton button {
            background-color: #ff6347;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 20px;
            transition: 0.3s;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        .stButton button:hover {
            background-color: #ff8566;
            transform: scale(1.05);
            box-shadow: 0 8px 30px rgba(0,0,0,0.2);
        }
        .stSuccess {
            background-color: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            color: white;
            font-size: larger;
            text-align: center;
            border-radius: 10px;
            padding: 15px;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # Title and description
    st.title("🌡️ Stylish Temperature Converter 🌡️")
    st.markdown("<h3>Convert between Celsius and Fahrenheit</h3>", unsafe_allow_html=True)
    
    # Input options for conversion type
    st.markdown("<div class='stApp'>", unsafe_allow_html=True)
    
    option = st.radio("Choose conversion:", 
                      ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

    if option == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:", value=0.0, step=0.1)
        if st.button("Convert 🌡️"):
            with st.spinner('Converting...'):
                time.sleep(1)
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.success(f"{celsius}°C is {fahrenheit:.2f}°F")

    elif option == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:", value=32.0, step=0.1)
        if st.button("Convert ❄️"):
            with st.spinner('Converting...'):
                time.sleep(1)
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.success(f"{fahrenheit}°F is {celsius:.2f}°C")

    

# Run the app
if __name__ == "__main__":
    main()
