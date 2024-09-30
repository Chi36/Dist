import numpy as np
import matplotlib.pyplot as plt

def calculate_distribution_ratio(solute_concentration_organic, solute_concentration_aqueous):
    """Calculates the distribution ratio (D) based on solute concentrations in both phases."""
    return solute_concentration_organic / solute_concentration_aqueous

def generate_distribution_curve(distribution_ratios, solute_concentrations_aqueous):
    """Generates a distribution curve to visualize the relationship between D and solute concentration."""
    plt.plot(solute_concentrations_aqueous, distribution_ratios)
    plt.xlabel("Solute Concentration in Aqueous Phase")
    plt.ylabel("Distribution Ratio (D)")
    plt.title("Distribution Curve")
    plt.grid(True)
    plt.show()

def plot_tie_line_diagram(solute_concentrations_organic, solute_concentrations_aqueous):
    """Plots a tie-line diagram to show the equilibrium compositions in both phases."""
    plt.scatter(solute_concentrations_aqueous, solute_concentrations_organic)
    plt.xlabel("Solute Concentration in Aqueous Phase")
    plt.ylabel("Solute Concentration in Organic Phase")
    plt.title("Tie-Line Diagram")
    plt.grid(True)
    plt.show()

# Example usage:
solute_concentrations_aqueous = np.linspace(0, 10, 100)
distribution_ratios = [calculate_distribution_ratio(0.5 * concentration, concentration) for concentration in solute_concentrations_aqueous]

# Generate distribution curve
generate_distribution_curve(distribution_ratios, solute_concentrations_aqueous)

# Generate tie-line diagram
plot_tie_line_diagram(0.5 * solute_concentrations_aqueous, solute_concentrations_aqueous)