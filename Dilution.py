import streamlit as st
import numpy as np

def calculate_dilution(initial_concentration, final_concentration, initial_volume):
    """Calculates the final volume required for dilution."""
    return (initial_concentration * initial_volume) / final_concentration

def main():
    st.title("Dilution Calculator")

    # Input parameters
    initial_concentration = st.number_input("Initial Concentration (wt%)", value=10.0, min_value=0.0)
    final_concentration = st.number_input("Final Concentration (wt%)", value=5.0, min_value=0.0)
    initial_volume = st.number_input("Initial Volume (mL)", value=100.0, min_value=0.0)

    # Calculate final volume
    final_volume = calculate_dilution(initial_concentration, final_concentration, initial_volume)

    st.write("Final Volume:", final_volume, "mL")

if __name__ == "__main__":
    main()