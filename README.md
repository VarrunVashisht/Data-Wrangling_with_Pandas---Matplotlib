# Finding Duplicates in Survey Data

## Data Wrangling with Pandas & Matplotlib

---

## 📌 Project Overview

This project focuses on **identifying, analyzing, visualizing, and removing duplicate records** from a real-world dataset using Python.
The dataset is derived from the **Stack Overflow Developer Survey** and intentionally contains duplicate entries to simulate real data quality challenges.

Handling duplicates is a **critical data wrangling step** that ensures data accuracy and reliable analysis.

---

## 🎯 Objectives

The goals of this project are to:

* Identify duplicate rows in a dataset
* Analyze the characteristics of duplicate entries
* Visualize duplicate distributions across categories
* Remove duplicates strategically using business logic
* Document and verify the duplicate removal process

---

## 🧰 Tools & Libraries Used

* **Python 3**
* **Pandas** – data manipulation and analysis
* **Matplotlib** – data visualization

---

## 📂 Dataset Information

* **Source:** Stack Overflow Developer Survey (subset)
* **Format:** CSV
* **Special Note:**
  The dataset intentionally includes duplicate rows for learning and analysis purposes.

### Dataset URL

```
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/VYPrOu0Vs3I0hKLLjiPGrA/survey-data-with-duplicate.csv
```

---

## 🔍 Project Workflow

### 1. Load the Dataset

* The dataset is loaded directly from a URL into a Pandas DataFrame.
* Initial rows are displayed to understand the data structure.

---

### 2. Identify Duplicate Rows

* Duplicate rows are detected using `pandas.DataFrame.duplicated()`.
* The total number of duplicate records is counted.
* Sample duplicate rows are displayed for inspection.

---

### 3. Analyze Duplicate Characteristics

* Duplicate entries are analyzed using selected columns:

  * `MainBranch`
  * `Employment`
  * `RemoteWork`
* This helps identify patterns and repeated respondent characteristics.

---

### 4. Visualize Duplicate Distribution

* Bar charts show duplicate distribution by **Country**
* Pie charts show duplicate distribution by **Employment**

Visualizations help identify whether duplicates are random or concentrated in specific groups.

---

### 5. Strategic Duplicate Removal

* Duplicates are removed using a **subset of columns** instead of entire rows.
* This approach preserves meaningful variation while maintaining data integrity.

Example criteria used:

```python
['MainBranch', 'Employment', 'RemoteWork']
```

---

### 6. Verification & Documentation

* Dataset size is compared before and after duplicate removal.
* The duplicate handling process is clearly documented.
* Decisions are justified based on data analysis principles.

---

## 📊 Key Learnings

* Duplicate data can significantly impact analysis results
* Duplicate removal should be **strategic**, not automatic
* Visualization helps understand the nature of duplicates
* Clean data is the foundation of trustworthy insights
* documentation-finding-duplicate.csv file attached for refernce.

---

## 🚀 Why This Project Matters

This project demonstrates **real-world data wrangling skills** used by data analysts in professional environments, including:

* Data quality assessment
* Analytical decision-making
* Transparent documentation
* Reproducible data workflows

These skills are essential for **exploratory data analysis, dashboards, and business reporting**.

---


## 👤 Author

**Varrun Vashisht**
Aspiring Data Analyst
Python | Pandas | Data Wrangling

---

## 📄 License

This project is for educational purposes and uses publicly available survey data.
