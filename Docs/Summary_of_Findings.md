# House Price Dataset – Summary of Findings

## Introduction

This analysis explores factors associated with house sale prices using a housing dataset. Python libraries including Pandas, NumPy, Seaborn, and Matplotlib were used to inspect the data, calculate descriptive statistics, and create visualizations. The analysis focuses on overall quality, neighborhood, and year built.

## Summary statistics

The notebook's descriptive-statistics step uses `housing.describe()` to summarize numerical variables, while `housing.info()` and `housing.isna().sum()` inspect data types and missing values. The notebook's dataset-loading cell references a course dataset that was not included with the uploaded files. Therefore, the dataset-wide summary statistics cannot be independently verified from the supplied notebook and plots alone.

## Key findings

### Sale price by overall quality

The plot shows a clear positive association between overall quality and average sale price. Average prices generally rise as the quality score increases. The highest quality category (10) has the highest plotted average, at roughly $438,000, while quality category 1 is around $50,000.

### Sale price by neighborhood

Average sale prices vary substantially by neighborhood. NoRidge, NridgHt, and StoneBr are among the highest-priced neighborhoods in the chart, with plotted averages around $335,000, $316,000, and $310,000 respectively. MeadowV is among the lowest, at roughly $99,000. These differences suggest that location is associated with property value.

### Sale price by year built

The grouped chart shows a general increase in average sale price across newer construction periods. The 2000+ group has the highest plotted average (roughly $245,000), while the pre-1920 and 1920–1950 groups are around $130,000. This indicates an association between construction period and sale price in this dataset.

## Conclusion

The visualizations suggest that overall quality, neighborhood, and year built are associated with house sale prices. Higher-quality homes, homes in certain neighborhoods, and more recently built homes generally have higher average sale prices in the displayed results. These are descriptive associations and do not establish that any one factor independently causes a higher sale price.

## Figures

- `Results/price_by_quality.png`
- `Results/price_by_neighborhood.png`
- `Results/price_by_year_built.png`
