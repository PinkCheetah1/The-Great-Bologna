import pandas as pd

student_data = pd.read_csv('student_data_folder\\student_data.csv')

print(student_data)

print(student_data.info())
# There are no null items in this data
# All data is float64 :D 

# Now lets find things out about our data! 
print()
print("DESCRIBE")
print(student_data.describe())
print()
print("CORRELATION")
print(student_data.corr())

# This loads the file to a json
student_data.to_json('student_data_folder\\student_data.json')

# This SHOULD load the file to an excel file, but doesn't for some reason. 
# student_data.to_excel('student_data_folder\\student_data.xlsx')

# Loads data to file as tab separated 
student_data.to_csv('student_data_folder\\student_data.txt', sep='\t')

# Loads data to modified CSV
student_data.to_csv('student_data_folder\\student_data_modified.csv')