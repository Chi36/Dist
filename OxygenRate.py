# App code to a file named OxygenRate.py 

# Import Python libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Define Function to calculate the oxygen transfer rate
def calculate_do(initial_do, volumetric_mass_transfer_coefficient, saturation_concentration_of_oxygen, time_hours):
    do_values = [initial_do]

    transfer_rate = volumetric_mass_transfer_coefficient * (saturation_concentration_of_oxygen - initial_do)
    consumption_rate = (saturation_concentration_of_oxygen - initial_do) / time_hours

    for _ in range(time_hours):
        do_change = transfer_rate - consumption_rate
        do_values.append(do_values[-1] + do_change)

    return do_values, consumption_rate

# Title for the app
st.title("Oxygen Transfer Rate Calculator")

# Inputs for the Rate app
initial_do = st.number_input("Initial Dissolved Oxygen (mg/L)", min_value=0.0, max_value=20.0, value=8.0)
volumetric_mass_transfer_coefficient = st.number_input("Volumetric Mass Transfer Coefficient", min_value=0.0, value=0.1)
saturation_concentration_of_oxygen = st.number_input("Saturation Concentration of Oxygen (mg/L)", min_value=0.0, max_value=20.0, value=9.0)
time_hours = st.number_input("Time (hours)", min_value=1, max_value=100, value=10)

# Calculate the Dissolved Oxygen (DO) over time and consumption rate
if st.button("Calculate"):
    do_values, consumption_rate = calculate_do(initial_do, volumetric_mass_transfer_coefficient, saturation_concentration_of_oxygen, time_hours)

    st.write(f"Consumption Rate: {consumption_rate} mg/L per hour")

    # Plotting the results using matplotlib
    plt.plot(range(time_hours + 1), do_values)
    plt.xlabel("Time (hours)")
    plt.ylabel("Dissolved Oxygen (mg/L)")
    plt.title("Dissolved Oxygen Over Time")
    st.pyplot(plt)
