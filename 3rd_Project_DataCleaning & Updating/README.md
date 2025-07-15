# 🧹 Employee Data Cleaning & Salary Update Project

This project involves cleaning and updating a messy employee dataset using Python (Pandas and NumPy). It includes identifying and handling null values, removing duplicates, and applying transformations for clean and meaningful data analysis.

---

## 📁 Dataset Overview

- **Original Data Source:** `Employee_Data.csv`
- **Total Rows Before Cleaning:** 600
- **Total Columns:** 3  
  - `EMPLOYEE ID`  
  - `NAME`  
  - `SALARY`

---

## ⚠️ Problems Faced

1. **Missing Values:**
   - `EMPLOYEE ID`: 10 missing entries  
   - `SALARY`: 301 missing entries

2. **Duplicate Entries:**
   - Multiple duplicate `EMPLOYEE ID`s observed across the dataset

3. **Unordered Data:**
   - Rows were not sorted properly

4. **Chained Assignment Warning:**
   - Pandas showed a `FutureWarning` due to chained assignment when filling null salary values

---

## ✅ Solutions Implemented

1. **Filled Null Salaries:**  
   Replaced missing `SALARY` values with the **mean** salary.

2. **Removed Rows with Missing `EMPLOYEE ID`:**
   ```python
   df = df.dropna(subset=["EMPLOYEE ID"])

3. **Removed Duplicate `EMPLOYEE ID` Rows Entirely:**

   ```python
   df = df[df.duplicated(subset="EMPLOYEE ID", keep=False) == False]

4. **Sorted Data by `EMPLOYEE ID`:**

   ```python
   df.sort_values(by="EMPLOYEE ID", inplace=True)

5. **Updated Salary (Increased by 5%):**

   ```python
   df["SALARY"] = df["SALARY"] * 1.05

6. **Saved Final Cleaned File:**
   `Updated_Employee_Data.csv` with clean, updated, and sorted records

7. **Filtered Data into Two Groups Based on Salary:**

   - `Filtered_Salary_0_to_50K.csv`
   - `Filtered_Salary_Above_50K.csv`

## ⏳ Time Taken
   - `Everything is New for thats why its take soo much i think`
   - `I need to do more and more practice so its be easy for me`
   - `Total time:  Approx 6 hours`

**Breakdown:**
   - `Data understanding and visualization: ~45 minutes`
   - `Writing and debugging code: ~2 hours`
   - `Cleaning, testing, and exporting files: ~3 hours`

## 📊 Final Results
| Description	| Count |
|-------------|------|
| Original Rows	| 600 |
| Rows After Removing Nulls & Duplicates | 100 |
| Unique & Clean EMPLOYEE IDs | ✅ Yes |
| Warnings Resolved | ✅ Yes |

## 🚀 Technologies Used
   - `Python 3.13`
   - `Pandas`
   - `NumPy`
   - `Jupyter Notebook / VSCode`
   - `Excel (for verifying cleaned outputs)`

## 📌 Files in This Repo
   - `Employee_Data.csv` – Raw dataset
   - `Employee_DataCleaning.py` – Cleaning script
   - `Updated_Employee_Data.csv` – Cleaned & updated data
   - `Filtered_Salary_0_to_50K.csv` – Salary below ₹50,000
   - `Filtered_Salary_Above_50K.csv` – Salary above ₹50,000
   - `README.md` – Project documentation

## 👨‍💻 Author
## `Mohammed Zaid`
`Created as part of my personal learning journey in data cleaning and Python programming.`
