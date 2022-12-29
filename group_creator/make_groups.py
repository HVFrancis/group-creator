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

def get_rosters(filename):
    """Get the lists of students from each sheet in the name Excel file.

    This function opens an Excel spreadsheet, attempts to find students lists
    from each sheet, and creates a dictionary mapping each sheet name to
    the list of students (randomized) from that list.

    Parameters
    ----------
    filename : str
        The Excel spreadsheet

    Returns
    -------
    dict
        A mapping of sheetnames to the list of students.

    Raises
    ------
    KeyError   
        If a specifc sheet doesn't have a "Student Name" column
        (propogated from get_students)
    """
    rosters = dict()
    xls = pd.ExcelFile(filename)
    for sheet in xls.sheet_names:
        print(f"reading sheet: {sheet}")
        df =  pd.read_excel(filename,sheet_name=sheet)
        try:
            students = get_students(df)
            rosters[sheet] = students
        except KeyError:
            pass  # go to the next sheet
        
    return rosters


def get_students(df):
    """Get a list of students from the provided data frame
    
    This function takes a Pandas dataframe, and tries to find a 
    list of students. It returns that list if found

    Parameters
    ----------
    df : pd.Dataframe
        A single worksheet dataframe

    Returns
    -------
    list
        A list of the students names from the data frame

    Raises
    ------
    KeyError
        Not Caught! If sheet doesn't have a "Student Name" column. 
        (Propogated to get_rosters)
    """
    students = df.loc[:,"Student Name"].tolist()   
    print (students)
    return students




def make_groups(students):
    """Take a list of students and divide them into groups of three or four

    This function takes a list of students, and divides them into groups of 
    three or four. It has not be tested on lists with fewer than 6 students
    (for which this program probably wouldn't be used).

    Parameters
    ----------
    students : list
        A list of student names.

    Returns
    -------
    list
        A list of lists, each individual list a list of 3 or 4 students
    """
    size = len(students)
    random.shuffle(students)
    no_of_groups = (size + 3) // 4
    groups = []
    for i in range (no_of_groups):
        groups.append([])
    for i, student in enumerate(students):
        groups[i % no_of_groups].append(student)  
    for group in groups:
        group.sort()  
    return groups


def make_multiple_groups(rosters):
    """Given a dictionary of rosters, produce a dictionary of student groups

    This function takes a dictionary of rosters, divides each roster into
    groups of 3 or 4, then returns a new dictionary, mapping the worksheet
    name to its collection of groups.

    Parameters
    ----------
    rosters : dict
        A mapping of worksheet name to list of students in that sheet

    Returns
    -------
    dict
        A mapping of worksheet names to a collection of groups.
    """
    all_groups = dict()
    for key in rosters:
        groups = make_groups(rosters[key])
        all_groups[key] = groups
    return all_groups


############
# Functions used during development.

def get_df(filename):
    """Get a Pandas dataframe from an Excel spreadsheet file
    
    """
    # Only used for development purposes. Not needed in final version.
    df = pd.read_excel(filename)
    return df



def test_one_sheet():
    for file in files:
        df = get_df(file)
        students = get_students(df)
        groups = make_groups(students)
        for group in groups:
            print(group)
        print("---")


def test_multiple_sheets():
    rosters = get_rosters("Sample Roster 24.xlsx")
    all_groups = make_multiple_groups(rosters)
    print(all_groups)

if __name__ == "__main__":

    # test_one_sheet()
    test_multiple_sheets()
    