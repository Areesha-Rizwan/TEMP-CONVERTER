import streamlit as st

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit App
def main():
    st.title("Temperature Converter")

    # Input options for conversion type
    option = st.radio("Select conversion type:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

    if option == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:", value=0.0)
        if st.button("Convert"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.success(f"{celsius}°C is {fahrenheit:.2f}°F")
    
    elif option == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:", value=32.0)
        if st.button("Convert"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.success(f"{fahrenheit}°F is {celsius:.2f}°C")

# Run the app
if __name__ == "__main__":
    main()
