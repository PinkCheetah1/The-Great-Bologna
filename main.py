import pandas as pd

student_data = pd.read_csv('student_data_folder\\student_data.csv')

print(student_data)

print(student_data.info())
# There are no null items in this data
# All data is float64 :D 

# To clean up any empty cells, we could use:
# new_student_data = student_data.dropna()
# OR
# student_data.dropna(inplace = True)
# However, we have no blanks to clean up, so we will leave this commented out (:


# making some data, this is just a series I think? 
# randomData = {
#     "pink" : [1, 2, 3, 4, 5],
#     "purple" : [6, 7, 8, 9, 10],
#     "orange" : [11, 12, 13, 14, 15],
#     "magenta" : [16, 17, 18, 19, 20]
# }

# Now we're turning the series into a dataframe
# We're naming the rows instead of having an index. I can access these by the name now rather than the index
# df = pd.DataFrame(randomData, index = ['skittles', 'm&ms', 'tortillas', 'candycorn', 'flowers'])
# print(df)

# We are referencing this by the name we gave the index
# This returns a series, not a dataframe 
# Don't forget to use .loc
# print(df.loc['skittles'])