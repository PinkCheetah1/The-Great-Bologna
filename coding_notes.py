# To clean up any empty cells, we could use:
# new_student_data = student_data.dropna()
# OR
# student_data.dropna(inplace = True)
# However, we have no blanks to clean up, so we will leave this commented out (:

# Mean = average 
# Median = middle
# Mode = most common 

# We are referencing this by the name we gave the index
# This returns a series, not a dataframe 
# Don't forget to use .loc
# print(df.loc['skittles'])