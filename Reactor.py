import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calculate_cstr_volume(flow_rate, rate_constant, initial_concentration, target_conversion):
    """Calculates the CSTR volume."""
    X = target_conversion / 100
    return flow_rate * (X / (rate_constant * initial_concentration * (1 - X)))

def calculate_pfr_volume(flow_rate, rate_constant, initial_concentration, target_conversion):
    """Calculates the PFR volume."""
    X = target_conversion / 100
    return flow_rate / (rate_constant * initial_concentration) * np.log(1 / (1 - X))

def plot_pfr_conversion_profile(flow_rate, rate_constant, initial_concentration, target_conversion):
    """Plots the PFR conversion profile."""
    X = np.linspace(0, target_conversion / 100, 100)
    V = calculate_pfr_volume(flow_rate, rate_constant, initial_concentration, X * 100)
    plt.figure(figsize=(8, 6))
    plt.plot(V, X)
    plt.xlabel("Reactor Volume")
    plt.ylabel("Conversion")
    plt.title("PFR Conversion Profile")
    st.pyplot()

def plot_cstr_conversion_vs_volume(flow_rate, rate_constant, initial_concentration, target_conversion):
    """Plots the CSTR conversion vs. reactor volume."""
    V = np.linspace(0, 100, 100)
    X = V * rate_constant * initial_concentration / flow_rate / (1 + V * rate_constant * initial_concentration / flow_rate)
    plt.figure(figsize=(8, 6))
    plt.plot(V, X)
    plt.xlabel("Reactor Volume")
    plt.ylabel("Conversion")
    plt.title("CSTR Conversion vs. Reactor Volume")
    st.pyplot()

def main():
    st.title("Reactor Volume Calculator")

    # Input parameters
    flow_rate = st.number_input("Flow Rate", value=1.0, min_value=0.0)
    rate_constant = st.number_input("Rate Constant", value=1.0, min_value=0.0)
    initial_concentration = st.number_input("Initial Concentration", value=1.0, min_value=0.0)
    target_conversion = st.number_input("Target Conversion (%)", value=90.0, min_value=0.0, max_value=100.0)

    # Calculate reactor volumes
    cstr_volume = calculate_cstr_volume(flow_rate, rate_constant, initial_concentration, target_conversion)
    pfr_volume = calculate_pfr_volume(flow_rate, rate_constant, initial_concentration, target_conversion)

    st.write("CSTR Volume:", cstr_volume)
    st.write("PFR Volume:", pfr_volume)

    # Compare reactor performance
    if cstr_volume < pfr_volume:
        st.write("CSTR requires a smaller volume to achieve the target conversion.")
    elif cstr_volume > pfr_volume:
        st.write("PFR requires a smaller volume to achieve the target conversion.")
    else:
        st.write("Both CSTR and PFR require the same volume to achieve the target conversion.")

    # Plot conversion profiles
    if st.button("Plot"):
        plot_pfr_conversion_profile(flow_rate, rate_constant, initial_concentration, target_conversion)
        plot_cstr_conversion_vs_volume(flow_rate, rate_constant, initial_concentration, target_conversion)

if __name__ == "__main__":
    main()