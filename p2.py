import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv(r"C:\Users\SAMPATH\Desktop\test (1)prodidy task 1.csv")

# Display initial information
print("Initial missing values:\n", data.isnull().sum())
print("Initial number of duplicates:", data.duplicated().sum())

# Step 1: Handle Missing Values
# 1.1 Drop rows where "Embarked" has missing values
data.dropna(subset=["Embarked"], inplace=True)

# 1.2 Replace missing values in the "Cabin" column with "unknown"
data["Cabin"] = data["Cabin"].fillna("unknown")

# 1.3 Replace missing values in the "Age" column with the mean age
data["Age"] = data["Age"].fillna(data["Age"].mean())

# Step 2: Clean "Fare" Column
import numpy as np

# Assuming 'Fare' column might contain some non-numeric characters
data['Fare'] = data['Fare'].replace(to_replace=r'[^\d.]', value='', regex=True)

# Convert the cleaned 'Fare' column to a numeric type
data['Fare'] = pd.to_numeric(data['Fare'], errors='coerce')

# Check the result to ensure the cleaning process worked as expected
print(data['Fare'].head())


# Step 3: Clean "Ticket" Column
# 3.1 Remove any duplicates in "Ticket" column if necessary
data["Ticket"] = data["Ticket"].str.replace('.', '').str.strip()

# Step 4: Handle Duplicates
# 4.1 Drop duplicate rows if any
data.drop_duplicates(inplace=True)


# Step 6: Verify Cleaning
print("Final missing values:\n", data.isnull().sum())
print("Final number of duplicates:", data.duplicated().sum()) 



# Step 7: Display Cleaned Data Info
print(data.info())
print(data.describe())

# Optional: Display a sample of the cleaned data
print(data.head(10))

#Age distribution
plt.figure(figsize=(6, 3))
sns.histplot(data["Age"], bins=20, kde=True, kde_kws={'bw_adjust': 0.8})
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.grid(True)
plt.show()

#Boxplot of Age by pclass shows the distribution of passengers across different passeneger classes
plt.figure(figsize=(8, 4))
sns.boxplot(x="Pclass", y="Age", data=data)
plt.title("Age Distribution by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Age")
plt.show()

# Distribution of passengers by Embarked
embarked_counts = data['Embarked'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(embarked_counts, labels=embarked_counts.index, autopct='%1.1f%%', colors=sns.color_palette("coolwarm", len(embarked_counts)))
plt.title("Distribution of Passengers by Embarkation Point")
plt.show()
