# House Price Analysis

**Assignment 2 – Part 3**  
A Python-based exploratory data analysis of house sale prices. The project investigates how sale price varies by overall quality, neighborhood, and year built.

## Repository structure

```text
House-Price-Analysis/
├── Src/       # Jupyter Notebook and reusable Python analysis script
├── Data/      # Input dataset (not included; see Data/README.md)
├── Docs/      # Written summary of findings
├── Results/   # Generated visualizations
└── README.md
```

## Analysis questions

1. How does average sale price vary with overall quality (`OverallQual`)?
2. How does average sale price vary by neighborhood (`Neighborhood`)?
3. How does average sale price vary by construction period (`YearBuilt`, grouped into periods)?

## Requirements

- Python 3.9 or later
- pandas
- numpy
- seaborn
- matplotlib
- Jupyter Notebook

Install dependencies:

```bash
pip install pandas numpy seaborn matplotlib jupyter
```

## Dataset setup

The original notebook expects the Ames-style housing dataset in `Data/HousingDataset.csv`. The CSV was not present among the files supplied for this project, so it is intentionally not included. Obtain the dataset from your course materials and place it at that exact path before running the notebook or script. Do not upload a dataset unless you have permission to share it.

## Run the analysis

From the repository root:

```bash
jupyter notebook Src/Dennis_2_3.ipynb
```

Or run the Python script:

```bash
python Src/analysis.py
```

The analysis saves three charts to `Results/`.

## Findings

- Average sale price generally increases with overall quality.
- Average sale prices differ substantially across neighborhoods.
- The grouped chart indicates higher average prices for more recently built homes.

See [`Docs/Summary_of_Findings.md`](Docs/Summary_of_Findings.md) for the written summary and chart interpretations.
