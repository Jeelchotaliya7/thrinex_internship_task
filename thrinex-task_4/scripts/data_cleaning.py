import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(
    BASE_DIR,
    "..",
    "cleaned_data",
    "cleaned_superstore.csv"
)

reports_folder = os.path.join(
    BASE_DIR,
    "..",
    "reports"
)

visuals_folder = os.path.join(
    BASE_DIR,
    "..",
    "visuals"
)

os.makedirs(reports_folder, exist_ok=True)
os.makedirs(visuals_folder, exist_ok=True)

df = pd.read_csv(input_file)

# Summary report
summary = df.describe()

summary.to_excel(
    os.path.join(
        reports_folder,
        "summary_report.xlsx"
    )
)

# Sales by Category
sales = df.groupby(
    'Category'
)['Sales'].sum()

plt.figure(figsize=(8,5))

sales.plot(kind='bar')

plt.title("Sales by Category")

plt.tight_layout()

plt.savefig(
    os.path.join(
        visuals_folder,
        "category_sales.png"
    )
)

plt.close()

# Profit by Region
profit = df.groupby(
    'Region'
)['Profit'].sum()

plt.figure(figsize=(8,5))

profit.plot(kind='pie')

plt.ylabel("")

plt.tight_layout()

plt.savefig(
    os.path.join(
        visuals_folder,
        "profit_region.png"
    )
)

plt.close()

print("Reports Generated Successfully")