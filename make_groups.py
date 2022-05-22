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

def get_dataframes(filename):
    """Get a list of all the data frames in the provided spreadsheet

    It returns a dictionary of sheet name : data frame
    """
    dfs = dict()
    xls = pd.ExcelFile(filename)
    for sheet in xls.sheet_names:
        df =  pd.read_excel(filename,sheet_name=sheet)
        try:
            students = get_students(df)
        except KeyError:
            break  # go to the next sheet
        dfs[sheet] = students
    return dfs


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


def make_multiple_groups(dfs):
    """Given a dictionary of dataframes, produce a dictionary of student
    groups

    """
    all_groups = dict()
    for key in dfs:
        groups = make_groups(dfs[key])
        all_groups[key] = groups
    return all_groups


def test_one_sheet():
    for file in files:
        df = get_df(file)
        students = get_students(df)
        groups = make_groups(students)
        for group in groups:
            print(group)
        print("---")


def test_multiple_sheets():
    dfs = get_dataframes("Sample Roster 24.xlsx")
    all_groups = make_multiple_groups(dfs)
    print(all_groups)

if __name__ == "__main__":

    # test_one_sheet()
    test_multiple_sheets()
    