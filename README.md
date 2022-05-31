# group-creator

The objective of this program is to take a class roster from an Excel spreadsheet, divide the students into workteams of four (or three) and create a PDF with those team assignments. I've designed it specifically to assist me in this task for my job, but it can probably be modified to support closely related tasks.

The file cli.py contains a script to prompt for all the needed information. It then calls the appropriate functions to split the students and create the PDF. The dunder main.py file also calls the main() function in cli.py

As it's currently written, it will find any worksheet in a single Excel file which has a roster, indicated by having a column label "Student Names". The name of that worksheet will be used as the Section No field in the PDF created.

### Requirements:
* Python 3.8 or better
* pandas
* reportlab
* An Excel file with rosters, indicated with "Student Names" as the column header
* Worksheet names of the section number/letter/name for that roster

### To use:
at root of project folder

`% python group-creator`

You will then be prompted for information about the filename, course number, course title, school, instructor name, semester, and unit (I change groups when we start a new unit in class). A PDF will be created using the course number, section number (from the worksheet name) and unit number.

I don't think this will work for class sizes less than 6. But then I probably wouldn't use more than one team.


### Things I still want to do
* Allow for a CSV file to be used as well
* A way to specify the group size
* A better interface

### Things I might want to do
* Allow for a different group size.


Keep up with this project at my blog: https://howardf64.wordpress.com/category/group-creator/


---

#### Motivating thoughts:

In my math classes, I create in-class groups to work together on a variety of learning activities.

My primary work-flow for this would be to shuffle the list in an Excel workbook (by creating a column of random numbers,
then sorting by that column, then dragging students into groups of 4. I would then save that page to a PDF to post in class.

When I had just one math class each semester, this wasn't a problem.

However! At my new job I will have four math classes, creating new teams probably three or four times each semester. So
I wanted to write a program to automate that. This is that program.

The program, when finished will:
* Extract the list of student names from an Excel file
* Randomly place the students into groups of three or four
* Produce a PDF file listing those groups

This should be fun!
