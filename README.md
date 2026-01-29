# UNDER CONSTRUCTION
yeah i should have written that in earlier commits

# 2026_01_Toy_Store_E-Commerce
This is a Exploratory Data Analysis portfolio project.

## Goal
Demonstrate my skills at performing exploratory data analysis (data profiling, data cleaning, univariate/bivariate analysis, feature engineering) to provide descriptive statistics from the raw data (thus demonstrating a simple ETL process) and present them in a simple dashboard (thus demonstrating data visualization).

## About the data
Maven Fuzzy Factory is a synthetic dataset created by Maven Analytics.
It contains fictitious e-commerce data simulating 3 years of sales.
Maven Analytics provides this data under a Public Domain license, I do not own or have any special rights over it nor have I created it.

The original dataset can be accessed at:
https://mavenanalytics.io/data-playground/toy-store-e-commerce-database

Alternatively, it has been uploaded to Kaggle:
https://www.kaggle.com/datasets/siddharth0935/toy-store-e-commerce-database/data

## Business relevancy
Although the data is fictitious, it simulated actual e-commerce traffic. 
Such a business would probably be interested in knowing about:
* Most popular products
* Least popular products
* Conversion rate
* Average order value

## Requirements
This project uses, among other Python modules, pandas & jupyter notebooks.
A full requiremenst list can be found in `/requirements.txt` 

## Components
* Dashboard: a simple dashboard is in `/main.py`
* Dataset: all 6 tables of the original database are located in `/data/raw/`
* Clean data: products of exploratory data analysis are located in `/data/clean/`
* Jupyter notebooks: to keep them out of the base directory, but still in a directory where (to the best of my abilities) they can read the data, the notebooks are in `/data/`.
* Ancilliary components: Additional python scripts are located in `/utils/`

