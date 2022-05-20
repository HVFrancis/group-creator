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



# def get_dataframes(filename):
#     """Get a list of all the data frames in the provided spreadsheet

#     """
#     book = pd.read_excel(filename)
#     dfs = []
#     for sheets in book.items()

def get_students(filename):
    """Get a randomized list of students from the provided spreadsheet
    
    """
    df = pd.read_excel(filename)
    students = df.loc[:,"Student Name"].tolist()
    random.shuffle(students)
    return students


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



if __name__ == "__main__":

    for file in files:
        students = get_students(file)
        groups = make_groups(students)
        for group in groups:
            print(group)
        print("---")


