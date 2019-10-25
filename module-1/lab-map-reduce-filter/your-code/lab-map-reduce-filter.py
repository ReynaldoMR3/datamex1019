from functools import reduce
from itertools import count

import numpy as np
import pandas as pd
import re

from pandas import DataFrame

"""
Challenge 1 - Mapping
We will use the map function to clean up a words in a book.
In the following cell, we will read a text file containing the book The Prophet by Khalil Gibran.
"""
location = '/Users/apple/desktop/datamex1019/module-1/lab-map-reduce-filter/58585-0.txt'
with open(location, 'r', encoding="utf8") as f:
    prophet = f.read().split(' ')

"""
Let's remove the first 568 words since they contain information about the book but are not part of the book itself.
Do this by removing from prophet elements 0 through 567 of the list 
(you can also do this by keeping elements 568 through the last element).
"""
lst_prophet = list(prophet)
lst_prophet = lst_prophet[568:]

"""""
If you look through the words, you will find that many words have a reference attached to them. 
For example, let's look at words 1 through 10.
"""
print(lst_prophet[1:11])

"""""
The next step is to create a function that will remove references.
We will do this by splitting the string on the { character and keeping only the part before this character. 
Write your function below.
"""


def reference(x):
    '''
    Input: A string
    Output: The string with references removed

    Example:
    Input: 'the{7}'
    Output: 'the'
    '''

    # Your code here:
    return re.split('{', x)[0]


print(reference("the{7}"))

""""
Now that we have our function, use the map() function to apply this function to our book, 
The Prophet. Return the resulting list to a new list called prophet_reference
"""
prophet_reference = list(map(reference, lst_prophet))
print(prophet_reference)

""""
Another thing you may have noticed is that some words contain a line break. 
Let's write a function to split those words. Our function will return the string split on the character \n. 
Write your function in the cell below.
"""

line_break = lambda x: re.sub("\n", " ", x)

"""""
Apply the line_break function to the prophet_reference list. Name the new list prophet_line.
"""""
prophet_line = list(map(line_break, prophet_reference))
print(prophet_line)

""""
Challenge 2 - Filtering
When printing out a few words from the book, 
we see that there are words that we may not want to keep if we choose to analyze the corpus of text. 
Below is a list of words that we would like to get rid of. 
Create a function that will return false if it contains a word from the list of words specified and true otherwise.
"""
'''
Input: A string
Output: true if the word is not in the specified list and false if the word is in the list

Example:
word list = ['and', 'the']
Input: 'and'
Output: False

Input: 'John'
Output: True
'''

word_list = ['and', 'the', 'a', 'an']

prophet_filter = list(filter(lambda x: True if x not in word_list else False, prophet_line))
print(prophet_filter)

"""
Challenge 3 - Reducing
Now that we have significantly cleaned up our text corpus, let's use the reduce() function to put the words back together into one long string separated by spaces.
We will start by writing a function that takes two strings and concatenates them together with a space between the two strings.
"""


def concat_space(a, b):
    '''
    Input:Two strings
    Output: A single string separated by a space

    Example:
    Input: 'John', 'Smith'
    Output: 'John Smith'
    '''

    # Your code here:
    return a + " " + b


print(concat_space("John", "Smith"))
"""""
Use the function above to reduce the text corpus in the list prophet_filter into a single string. 
Assign this new string to the variable prophet_string.
"""""
prophet_string = reduce(concat_space, prophet_filter)
print(prophet_string)
print("")
print("")

"""""
Challenge 4 - Applying Functions to DataFrames
Our next step is to use the apply function to a dataframe and transform all cells.
To do this, we will load a dataset below and then write a function that will perform the transformation.
"""""
# Run this code:

# The dataset below contains information about pollution from PM2.5 particles in Beijing

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00381/PRSA_data_2010.1.1-2014.12.31.csv"
pm25 = pd.read_csv(url)

# Let's look at the data using the head() function.

head = pm25.head()
print(head)
print("")
print("")
print("")


# The next step is to create a function that divides a cell by 24 to produce an hourly figure. Write the function below.
def hourly(x):
    '''
    Input: A numerical value
    Output: The value divided by 24

    Example:
    Input: 48
    Output: 2.0
    '''

    # Your code here:
    return x / 24


# Apply this function to the columns Iws, Is, and Ir. Store this new dataframe in the variable pm25_hourly.
df = DataFrame(pm25)
#new_df= pd.DataFrame(hourly, columns=["Iws","Is","Ir"])
pm25_hourly=pd.DataFrame()
#print ([hourly(e) for e in df.Iws])
pm25_hourly['Iws']=[hourly(e) for e in df.Iws]
pm25_hourly['Is']=[hourly(e) for e in df.Is]
pm25_hourly['Ir']=[hourly(e) for e in df.Ir]
print (pm25_hourly)
print("")
print("")
print("")


"""""
Our last challenge will be to create an aggregate function and apply it to a select group of columns in our dataframe.
Write a function that returns the standard deviation of a column divided by the length of a column minus 1. 
Since we are using pandas, do not use the len() function. One alternative is to use count(). 
Also, use the numpy version of standard deviation.
"""""


def sample_sd(x):
    '''
    Input: A Pandas series of values
    Output: the standard deviation divided by the number of elements in the series

    Example:
    Input: pd.Series([1,2,3,4])
    Output: 0.3726779962
    '''

    # Your code here:
    return (np.std(x)/x.count()-1)

samplesd = pm25_hourly.apply(sample_sd,axis=0)
print(samplesd)