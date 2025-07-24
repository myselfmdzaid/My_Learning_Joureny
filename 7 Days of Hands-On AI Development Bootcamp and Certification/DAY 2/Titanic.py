import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('D:/MY PERSONAL/Zaid Learnings/My_Learning_Journey/7 Days of Hands-On AI Development Bootcamp and Certification/DAY 2/TitanicData.csv')
print("First Some Rows From TitanicData\n", data.head(), "\n")
print("Last Some Rows From TitanicData\n", data.tail(), "\n")

print("Information About TitanicData\n", data.info(), "\n")

print("Description of TitanicData\n", data.describe(), "\n")

print("Print Sum of Null\n", data.isnull().sum())

data['Age'].fillna(data["Age"].mean(), inplace=True)

print(data['Survived'].value_counts(normalize=True))

print(data.groupby(['Sex','Pclass'])['Survived'].mean)

plt.plot(data["Age"], data["Survived"])
plt.title('Age of Survived')
plt.xlabel('Age')
plt.ylabel('Survived')
plt.show()

data["Pclass"].value_counts().plot(kind='barh')
plt.title('Pclass Counts')
plt.show()

sns.barplot(x='Sex', y='Survived', data=data)
plt.title('Survived Rate by Sex')
plt.show()

data.to_csv('Updated_TitanicData.csv', index=False)
