import numpy as np
import pandas as pd 

df = pd.read_csv('D:/MY PERSONAL/Zaid Learnings/My_Learning_Joureny/3rd_Project_DataCleaning & Updating/Employee_Data.csv')

print("\n Print DataFrame Information")
print(df.info())

print("\n Print DataFrame Description")
print(df.describe())

print("\n Detect Null and Print Sum of it")
print(df.isnull().sum())

# Fill Null Salary by Mean of it
df.fillna({'SALARY': df['SALARY'].mean()}, inplace=True)

# Removing Null From Employee ID
df.dropna(subset=['EMPLOYEE ID'])

# Removing Duplicates 
df.drop_duplicates(subset=['EMPLOYEE ID'], keep='first', inplace=True)

# Removing Duplicates from Employee ID Colum
df.dropna(subset=['EMPLOYEE ID'], inplace=True)

# Remove all rows that have duplicated EMPLOYEE IDs
df = df[~df['EMPLOYEE ID'].duplicated(keep=False)]

# Sort Data by Employee ID
df.sort_values(by="EMPLOYEE ID", inplace=True)

# Updating Salary
df["SALARY"] = df["SALARY"] * 1.05

# Save DataFrame to CSV
df.to_csv('Updated_Employee_Data.csv', index=False)

# Filter and Save DataFrame : Between 0 to 50,000 
Filte_0_to_50K = df[(df["SALARY"] >= 0) & (df["SALARY"] <= 50000)]
Filte_0_to_50K.to_csv('Filtered_Salary_0_to_50K.csv', index=False)

# Filter and Save DataFrame : Above 50,000
Filte_More_Then_50K = df[(df["SALARY"] > 50000)]
Filte_More_Then_50K.to_csv('Filtered_Salary_Above_50K.csv', index=False)

print("Data Cleaning and Updating Completed and Saved as 'Updated_Employee_Data.csv'")
print("Salary Filtering 0 to 50,000 Completed and Saved as 'Filtered_Salary_0_to_50K.csv'")
print("Salary Filtering Above 50,000 Completed and Saved as 'Filtered_Salary_Above_50K.csv'\n")

print("\n Print Updated DataFrame Information")
print(df.info())

print("\n Print Updated DataFrame Description")
print(df.describe())

print("\n Detect Null and Print Sum of it")
print(df.isnull().sum())
