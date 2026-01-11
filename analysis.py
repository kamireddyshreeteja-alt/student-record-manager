import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_NAME = "students.csv"

# Check if CSV exists
if not os.path.exists(FILE_NAME):
    print("No student data found.")
    exit()

# Load CSV into Pandas DataFrame
df = pd.read_csv(FILE_NAME)
df.colums = df.columns.str.strip()

# Convert marks to integers
df["Subject1"] = df["Subject1"].astype(int)
df["Subject2"] = df["Subject2"].astype(int)
df["Subject3"] = df["Subject3"].astype(int)

# Calculate average
df["Average"] = (df["Subject1"] + df["Subject2"] + df["Subject3"]) / 3

# Grade logic
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"

df["Grade"] = df["Average"].apply(grade)

# Display all data
print("\n--- Student Performance ---")
print(df)

# Topper
topper = df.loc[df["Average"].idxmax()]
print("\nTopper:")
print(topper)

# Plot bar graph of student averages
plt.bar(df["Name "], df["Average"], color='skyblue')
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save analyzed data to new CSV
df.to_csv("analyzed_students.csv", index=False)
print("\nAnalyzed data saved to 'analyzed_students.csv'")
