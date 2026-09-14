# Assessment Mini-Project — Data Analysis with Python [T2]
**Module 1 - Week 07 | Course: Data Analysis with Python | SCTEC**

## About the Project
Exploratory Data Analysis (EDA) applied to a "Retail" dataset, containing real purchase records (dates, customers, products, and categories) from a supermarket over 4 years (2019–2022). 

The goal is to transform raw data into useful information through data loading, quality checking, cleaning, descriptive statistics, and clustering pattern analysis.

## Repository Structure

Miniprojeto_AndreNicolaiPopadiuk_T2/
├── miniprojeto.py                    # Main analysis script
├── Base Varejo.csv                   # Database required for execution
├── README.md                         # This file (theoretical reflection and insights)
└── README_AndreNicolaiPopadiuk_T2.md # Execution instructions


## How to Run
Please refer to the README_AndreNicolaiPopadiuk_T2.md file for a complete step-by-step guide.

Quick summary (VS Code):

pip install pandas numpy 
python miniprojeto.py


## Technologies Used
*   **csv (native):** Structured CSV reading using DictReader.
*   **datetime (native):** Date conversion and validation.
*   **pandas:** Data manipulation and analysis.
*   **numpy:** Statistical support.

---

## Theoretical Reflection — ETL and Data Quality

### What is ETL?
ETL (Extract, Transform, Load) is a fundamental data engineering process consisting of three stages:
1.  **Extract:** Collecting data from one or more raw sources (CSV files, databases, APIs, etc.).
2.  **Transform:** Cleaning, standardizing, enriching, and restructuring the data to make it reliable and usable.
3.  **Load:** Delivering the transformed data to a final destination (Data Warehouse, dashboard, ML model, etc.).

### Application in this Project
*   **Extract:** We used csv.DictReader (native Python) to read the Base Varejo.csv file with a semicolon separator. Each row is extracted as a dictionary (column: value), ensuring traceability and control before any transformations. Next, we converted it into a pandas DataFrame to facilitate analytical operations.
*   **Transform:** 4 unnamed columns (Unnamed) were dropped as they were artifacts with no analytical value. The DATA (Date) column, originally a string, was converted using datetime.strptime, enabling accurate temporal analysis. #N/D values in PR_CAT and PR_NOME were replaced with 'No Category' and 'No Name' using if/else logic, preserving valid record data. Null values in CL_FHL (children) were imputed with 0, indicating the absence of registered children. Records with invalid DATA were removed, as purchase dates cannot be safely imputed. Duplicate rows were dropped to prevent double counting in analyses. Null or negative values in CO_ID were removed for violating the identifier business rule.
*   **Load:** The clean DataFrame is made available in memory for all subsequent analyses. It can be exported using df.to_csv("varejo_limpo.csv") to feed dashboards or Machine Learning models.

### Data Quality
High-quality data must satisfy five dimensions:
1.  **Completeness:** No null values in critical fields.
2.  **Consistency:** No invalid values (e.g., #N/D).
3.  **Uniqueness:** No duplicate rows.
4.  **Validity:** Adherence to business rules (e.g., positive ID numbers).
5.  **Timeliness:** Dates correctly converted and validated.

The Retail dataset presented issues across all five dimensions, all of which were addressed in Sprint 3 of the script.

---

## Main Insights
*   **Quality:** Approximately 3,650 invalid records (0.44% of the dataset) were identified and handled prior to analysis.
*   **Top-selling category:** FOOD (ALIMENTOS) is the undisputed leader, followed by HYGIENE and CLEANING, a typical pattern for a local neighborhood supermarket.
*   **Gender profile:** Female customers made more purchases than male customers across all categories.
*   **Number of children:** The mode is 0 children, representing by far the demographic that buys the most. Among customers with children, purchase volume remains stable for those with 1, 2, or 3 children (averaging 90k purchases each), dropping sharply only for families with 4 children.
*   **Social segment:** Segment B accounts for the highest purchase volume during the analyzed period.
*   **Suspicious consistency:** The proportions between variables are suspiciously uniform over the 4-year period, suggesting possible artificial data inflation. Validation with the primary data source is highly recommended.

**Author**
André Nicolai Popadiuk — Cohort T2 | SCTEC | 2026
