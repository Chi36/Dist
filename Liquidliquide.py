import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calculate_distribution_ratio(initial_concentration, equilibrium_concentration_organic, equilibrium_concentration_aqueous):
    """Calculates the distribution ratio (D)."""
    return equilibrium_concentration_organic / equilibrium_concentration_aqueous

def plot_distribution_curve(initial_concentrations, equilibrium_concentrations_organic, equilibrium_concentrations_aqueous):
    """Plots the distribution curve."""
    plt.figure(figsize=(8, 6))
    plt.plot(initial_concentrations, equilibrium_concentrations_organic, label="Organic Phase")
    plt.plot(initial_concentrations, equilibrium_concentrations_aqueous, label="Aqueous Phase")
    plt.xlabel("Initial Concentration")
    plt.ylabel("Equilibrium Concentration")
    plt.legend()
    plt.title("Distribution Curve")
    st.pyplot()

def plot_tie_line_diagram(equilibrium_concentrations_organic, equilibrium_concentrations_aqueous):
    """Plots the tie-line diagram."""
    plt.figure(figsize=(8, 6))
    plt.plot(equilibrium_concentrations_aqueous, equilibrium_concentrations_organic)
    plt.xlabel("Equilibrium Concentration (Aqueous)")
    plt.ylabel("Equilibrium Concentration (Organic)")
    plt.title("Tie-Line Diagram")
    st.pyplot()

def main():
    st.title("Liquid-Liquid Extraction Calculator")

    # Input parameters
    initial_concentration = st.number_input("Initial Concentration", value=0.1, min_value=0.0)
    equilibrium_concentration_organic = st.number_input("Equilibrium Concentration (Organic)", value=0.05, min_value=0.0)
    equilibrium_concentration_aqueous = st.number_input("Equilibrium Concentration (Aqueous)", value=0.05, min_value=0.0)

    # Calculate distribution ratio
    distribution_ratio = calculate_distribution_ratio(initial_concentration, equilibrium_concentration_organic, equilibrium_concentration_aqueous)
    st.write("Distribution Ratio (D):", distribution_ratio)

    # Plot distribution curve and tie-line diagram
    if st.button("Plot"):
        # Sample data for demonstration
        initial_concentrations = np.linspace(0.0, 1.0, 100)
        equilibrium_concentrations_organic = initial_concentrations * distribution_ratio / (1 + distribution_ratio)
        equilibrium_concentrations_aqueous = initial_concentrations / (1 + distribution_ratio)

        plot_distribution_curve(initial_concentrations, equilibrium_concentrations_organic, equilibrium_concentrations_aqueous)
        plot_tie_line_diagram(equilibrium_concentrations_organic, equilibrium_concentrations_aqueous)

if __name__ == "__main__":
    main()