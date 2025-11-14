import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("covid_data.csv")

# Display basic info
print(data.head())
print(data.describe())

# Data Cleaning
data = data.dropna()

# Visualization
plt.figure(figsize=(12,6))
plt.plot(data["Country/Region"], data["New cases"], label="New Cases", color='blue')
plt.title("COVID-19 New Cases by Country")
plt.xlabel("Country/Region")
plt.ylabel("New Cases")
plt.xticks(rotation=90)  # Helps read country names on x-axis
plt.legend()
plt.tight_layout()       # Adjusts layout to prevent overlap
plt.show()