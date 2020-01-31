
"""
Created on Sun Aug 25 21:02:56 2019

@author: Robin Devasagayam Sebastian
"""


from fuzzywuzzy import process

with open("D:/Data/Projects/Fuzzy String Matching/cities.csv", "r") as f:
    cities=f.read().split("\n") 

def get_matches(query, choice, limit=3):
    result=process.extract(query, choice, limit=limit)
    return result

print("Please enter any city name")
n= (str(input()))

print("The matches of the names of the cities are: ", get_matches(n, cities))
