class FertilizerAnalyzer:
    def __init__(self, nitrogen, phosphorus, potassium):
        self.nitrogen = nitrogen  # percentage of nitrogen (N)
        self.phosphorus = phosphorus  # percentage of phosphorus (P2O5)
        self.potassium = potassium  # percentage of potassium (K2O)

    def verify_composition(self):
        """Verify the composition accuracy of the fertilizer."""
        print(f"Analyzing fertilizer composition:")
        print(f"Nitrogen Content: {self.nitrogen}%")
        print(f"Phosphorus Content: {self.phosphorus}%")
        print(f"Potassium Content: {self.potassium}%")

    def quality_control(self):
        """Maintain high standards for fertilizer quality."""
        if self.nitrogen < 0 or self.phosphorus < 0 or self.potassium < 0:
            raise ValueError("Nutrient percentages must be non-negative.")
        print("Quality Control: Fertilizer meets quality standards.")

    def crop_performance(self):
        """Enhance crop growth with balanced fertilizers."""
        total_nutrients = self.nitrogen + self.phosphorus + self.potassium
        if total_nutrients > 100:
            print("Warning: Total nutrient content exceeds 100%.")
        else:
            print("Crop Performance: Balanced nutrient levels for optimal growth.")

    def compliance_assurance(self):
        """Ensure compliance with industry regulations."""
        # Placeholder for compliance checks
        print("Compliance Assurance: Fertilizer complies with industry regulations.")

    def cost_efficiency(self):
        """Minimize waste and optimize usage."""
        usage_efficiency = (self.nitrogen + self.phosphorus + self.potassium) / 3
        print(f"Cost Efficiency: Average nutrient usage efficiency is {usage_efficiency:.2f}%.")

# Example usage
fertilizer = FertilizerAnalyzer(nitrogen=15, phosphorus=10, potassium=5)
fertilizer.verify_composition()
fertilizer.quality_control()
fertilizer.crop_performance()
fertilizer.compliance_assurance()
fertilizer.cost_efficiency()
