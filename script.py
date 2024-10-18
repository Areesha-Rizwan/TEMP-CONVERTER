import streamlit as st

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit App
def main():
    # Custom CSS for styling the background and text
    st.markdown(
        """
        <style>
        .main {
            background-color: #f5f5f5;
            color: #333333;
        }
        h1 {
            color: #ff4d4d;
        }
        .stRadio > div {
            display: flex;
            justify-content: center;
        }
        .stNumberInput input {
            background-color: #e6f7ff;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # Title and description
    st.title("🌡️ Temperature Converter 🌡️")
    st.subheader("Convert temperatures between Celsius and Fahrenheit easily!")
    st.write("Use the options below to select the conversion type and enter the value.")

    # Input options for conversion type
    option = st.radio("Select conversion type:", 
                      ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

    if option == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:", value=0.0, step=0.1)
        if st.button("Convert 🌡️"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.success(f"🌡️ {celsius}°C is {fahrenheit:.2f}°F 🌡️")
    
    elif option == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:", value=32.0, step=0.1)
        if st.button("Convert ❄️"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.success(f"❄️ {fahrenheit}°F is {celsius:.2f}°C ❄️")

    

# Run the app
if __name__ == "__main__":
    main()
