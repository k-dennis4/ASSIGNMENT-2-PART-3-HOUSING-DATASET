"""Exploratory analysis of house sale prices for Assignment 2, Part 3."""
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "Data" / "HousingDataset.csv"
RESULTS = ROOT / "Results"
RESULTS.mkdir(exist_ok=True)

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATA_PATH}. Place the course CSV at Data/HousingDataset.csv."
    )

housing = pd.read_csv(DATA_PATH)
print("Dataset information:")
housing.info()
print("\nSummary statistics:")
print(housing.describe())
print("\nMissing values:")
print(housing.isna().sum())

print("\nAverage sale price by overall quality:")
print(housing.groupby("OverallQual")["SalePrice"].mean())
sns.barplot(data=housing, x="OverallQual", y="SalePrice", errorbar=("ci", 95))
plt.xlabel("Overall Quality")
plt.ylabel("Sale Price")
plt.title("Sale Price Based on Overall Quality")
plt.tight_layout()
plt.savefig(RESULTS / "price_by_quality.png")
plt.close()

print("\nAverage sale price by neighborhood:")
print(housing.groupby("Neighborhood")["SalePrice"].mean())
order = housing.groupby("Neighborhood")["SalePrice"].mean().index
sns.barplot(data=housing, x="Neighborhood", y="SalePrice", order=order, errorbar=("ci", 95))
plt.xticks(rotation=90)
plt.xlabel("Neighborhood")
plt.ylabel("Sale Price")
plt.title("Sale Price Based on Neighborhood")
plt.tight_layout()
plt.savefig(RESULTS / "price_by_neighborhood.png", bbox_inches="tight")
plt.close()

housing["YearGroup"] = pd.cut(
    housing["YearBuilt"],
    bins=[1870, 1920, 1950, 1980, 2000, 2010],
    labels=["Before 1920", "1920-1950", "1950-1980", "1980-2000", "2000+"],
)
print("\nAverage sale price by year-built group:")
print(housing.groupby("YearGroup", observed=False)["SalePrice"].mean())
sns.barplot(data=housing, x="YearGroup", y="SalePrice", errorbar=("ci", 95))
plt.xlabel("Year Built")
plt.ylabel("Sale Price")
plt.title("Sale Price Based on Year Built")
plt.tight_layout()
plt.savefig(RESULTS / "price_by_year_built.png")
plt.close()
