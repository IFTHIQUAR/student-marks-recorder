import pandas as pd
import os
import matplotlib.pyplot as plt

file = 'ifthikar.xlsx'

# Load existing data if file exists, otherwise create new:
if os.path.exists(file):
    existing_df = pd.read_excel(file)
else:
    existing_df = pd.DataFrame(columns=['roll', 'name', 'major', 'allied', 'practical','total','average','Result','Grade'])

while True:
    roll = int(input('Enter your Roll no: '))

    # Check if roll number already exists
    if roll in existing_df['roll'].values:
        print(f"Roll number {roll} already exists. Please enter a different one.")
        continue

    name = input('Enter your name: ')
    major = int(input('Enter Major Marks: '))
    allied = int(input('Enter Allied Marks: '))
    practical = int(input('Enter Practical Marks: '))
    total=sum([major,allied,practical])
    average=round(total / 3, 2)
    #Calculating Grade
    if major<30 or allied<30 or practical<30:
        Grade="No Grade"
    elif average >=90:
        Grade="A"
    elif average >=70:
        Grade="B"
    elif average>=50:
        Grade="C"
    else:
        Grade="D"
    #Calculating Results
    if major>29 and allied>29 and practical>29:
        Result="PASS"
    else:
        Result="FAIL"
    # Append new record to existing DataFrame
    new_data = pd.DataFrame([{
        'roll': roll,
        'name': name,
        'major': major,
        'allied': allied,
        'practical': practical,
        'total':total,
        'average': average,
        'Result':Result,
        'Grade': Grade,


    }])

    existing_df = pd.concat([existing_df, new_data], ignore_index=True)

    more = input('Enter Another Student [yes/no]: ')
    if more.lower() != 'yes':
        break

# Save updated DataFrame to Excel
existing_df.to_excel(file, index=False)
print('Data Saved Successfully')

# Display the final DataFrame
abc = pd.read_excel(file)
print(abc)
plt.bar(abc['name'], abc['total'])
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.title("Total Marks of Students")
plt.show()










