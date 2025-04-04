import pandas as pd
import matplotlib.pyplot as plt
"""
This is MESSY code, but a lot of it is just experimentation. 
Because a lot can be accomplished with very few lines in Pandas, 
it was difficult to write a lot of code without writing a lot of
math, which wasn't what I was trying to learn. 
This is a collection of pretty much all of the things I tried and
all of the things I learned from them. 
"""

student_data = pd.read_csv('student_data_folder\\student_data.csv')

print(student_data.head())
print(student_data.tail())
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

# Now we're going to make plots! 
# Our first plot will be a graph of study time and grade, since those have a high correlation
student_data.plot(kind = 'scatter', x = 'Study Hours', y = 'Grades')
plt.show()

# Now we're going to have a bunch of histograms 
student_data['Study Hours'].plot(kind = 'hist')
plt.show()
# From this we learned that most students study 3-4 hours
student_data['Sleep Hours'].plot(kind = 'hist')
plt.show()
# from this we learn that most students sleep 8-10 hours

# Now let's get fancy and start combining columns. 
print()
student_data['Sleep + Study'] = student_data['Study Hours'] + student_data['Sleep Hours']
print(student_data[['Study Hours', 'Sleep Hours', 'Sleep + Study']])
print()
print()
print(student_data.corr())

student_data.plot(kind = 'scatter', x = 'Sleep + Study', y = 'Grades')
plt.show()
# Didn't find anything interesting from this /:

# I got the following code from ChatGPT, but I understand it. 
student_data['Pass/Fail'] = student_data['Grades'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')
print()
print(student_data.groupby('Pass/Fail')['Study Hours'].mean())
# The average fail student studied for about 3.9h but the average pass student studied
# for about 7.2. That's good to know! 

# Some of the following code also came from ChatGPT, but I understand it
# Try creating the qcut without labels first
percentile_bins = pd.qcut(student_data['Grades'], q=100, duplicates='drop')

# Now figure out how many unique bins we actually got
# This returns the number of bins the program can actually create without having a mental breakdown
num_bins = percentile_bins.cat.categories.size

# Create the correct number of labels
# This gives names to all of the bins that we just made
# Only makes exactly how many labels we need, booyah 
labels = [f'{i}%' for i in range(num_bins)]

# Now that we cut everything up and saw how many pieces we can make, 
# we actually go through and like apply it to the data and stuff
student_data['Grades Percentile'] = pd.qcut(
    student_data['Grades'],
    q=100,
    labels=labels,
    duplicates='drop'
)
print()
print(student_data[['Grades', 'Grades Percentile']].head)

# This loads the file to a json
student_data.to_json('student_data_folder\\student_data.json')

# This SHOULD load the file to an excel file, but doesn't for some reason. 
# student_data.to_excel('student_data_folder\\student_data.xlsx')

# Loads data to file as tab separated 
student_data.to_csv('student_data_folder\\student_data.txt', sep='\t')

# Loads data to modified CSV
student_data.to_csv('student_data_folder\\student_data_modified.csv')

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