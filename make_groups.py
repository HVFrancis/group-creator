# make_groups.py
# 
# file contains functions to take student names from an
# Excel spreadsheet, and divide the students into groups
# of three or four.
# The final result should be a list of lists

import pandas as pd
import openpyxl, xlrd
import random 

files = ["Sample Roster 24.xlsx",
            "Sample Roster 21.xlsx",
            "Sample Roster 16.xlsx"]

## Ideally, I want to start with a file, and have it return a list of
## dataframes, then generate a dictionary (str -> list of lists),
## with the section number being the key.

# def get_dataframes(filename):
#     """Get a list of all the data frames in the provided spreadsheet

#     """
#     book = pd.read_excel(filename)
#     dfs = []
#     for sheets in book.items()

def get_students(df):
    """Get a randomized list of students from the provided data frame
    
    """
    students = df.loc[:,"Student Name"].tolist()
    random.shuffle(students)
    return students

def get_df(filename):
    df = pd.read_excel(filename)
    return df



def make_groups(students):
    """Take a list of students and divide them into groups of three or four



    """
    size = len(students)
    no_of_groups = (size + 3) // 4
    groups = []
    for i in range (no_of_groups):
        groups.append([])
    for i, student in enumerate(students):
        groups[i % no_of_groups].append(student)  
    for group in groups:
        group.sort()  
    return groups

def test_one_sheet():
    for file in files:
        df = get_df(file)
        students = get_students(df)
        groups = make_groups(students)
        for group in groups:
            print(group)
        print("---")


if __name__ == "__main__":

    test_one_sheet()

