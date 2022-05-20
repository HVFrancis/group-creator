# make_pdf.py

# This contains code to create a PDF file given a list of student groups

# MATH 105-01        Fundamentals of Mathematics           Xavier Univ.
# HFrancis                  Unit 1 Teams                   Fall 2022


#           Team 1                             Team 2
#          name                               name
#          name                               name
#          name                               name
#          name                               name

#           Team 3                             Team 4
#          name                               name
#          name                               name
#          name                               name
#          name                               name

#           Team 5                             Team 6
#          name                               name
#          name                               name
#          name                               name
#          name                               name

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch

from make_groups import *

width, height = letter  #keep for later

course_no = "MATH 105"
section = "02"
course_title = "Fundamentals of Mathematics"
school = "Xavier Univ."
instructor = "HFrancis"
unit_no = "1"
term = "Fall 2022"
pdf_name = "MATH 105-02 Unit 1 Teams.pdf"
#pdf_name = f"{course_no}-{section} Unit {unit_no} Teams.pdf"



def initialize_document():
    c = canvas.Canvas(pdf_name, pagesize=letter)
    return c

def create_header(c):
    width, height = letter
    first_row = height - inch
    second_row = height - (inch + 15)
    c.drawString(inch, first_row, f"{course_no}-{section}")
    c.drawCentredString(width/2, first_row, f"{course_title}")
    c.drawRightString(width-inch, first_row, f"{school}")
    c.drawString(inch, second_row, f"{instructor}")
    c.drawCentredString(width/2, second_row, f"Unit {unit_no} Teams")
    c.drawRightString(width-inch, second_row, f"{term}")
    return c


def main():
    my_canvas = initialize_document()
    my_canvas = create_header(my_canvas)

    students = get_students("Sample Roster 24.xlsx")
    groups = make_groups(students)


    my_canvas.showPage()
    my_canvas.save()











if __name__ == "__main__":
    main()