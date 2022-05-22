# make_pdf.py

# This contains code to create a PDF file given a list of student groups

# ARITHS 105-01              Arithmetics                Hogwarts SWW
# HFrancis                  Unit 1 Teams                   Fall 1991


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

from tkinter.tix import TList
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import Table

from make_groups import *

width, height = letter  #keep for later


# # these look like they should be keyword parameters to create_header
# course_no = "ARITH 105"
# section = "01"
# course_title = "Arithmetics"
# school = "Hogwarts SWW"
# instructor = "HFrancis"
# unit_no = "1"
# term = "Fall 1991"
# #pdf_name = "MATH 105-02 Unit 1 Teams.pdf"
# pdf_name = f"{course_no}-{section} Unit {unit_no} Teams.pdf"



def initialize_document(pdf_name):
    c = canvas.Canvas(pdf_name, pagesize=letter)
    return c

def create_header(course_no,
                  section,
                  course_title,
                  school,
                  instructor,
                  unit_no,
                  term
                  ):
    """ This function creates the document and prints course information
    """
    # I don't like that this does the creation, but I don't know
    # how to create the file without repeating arguement
    pdf_name = f"{course_no}-{section} Unit {unit_no} Teams.pdf"
    c = initialize_document(pdf_name)
     
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

def small_tables(groups):
    """This function takes the student groups and returns a
    list of reportlab tables, one for each group
    
    """
    font_size = 14
    table_list = []
    for i, group in enumerate(groups):
        data = [[f"TEAM {i+1}"],
                [groups[i][0]],
                [groups[i][1]],
                [groups[i][2]], 
                [groups[i][3]],
                ]
        table = Table(data)
        table.setStyle([("ALIGN", (0, 0), (-1, 0), "CENTER"),
                        ("FONTSIZE", (0, 0), (-1, -1), font_size),
                        ])
        table_list.append(table)
    return table_list


def plot_tables(c, table_list):
    """Take the list of tables and position them in the PDF document
    
    """
    spaces = "      "
    data = [[table_list[0], spaces, table_list[1]],
            [spaces, spaces, spaces],
            [table_list[2], spaces, table_list[3]],
            [spaces, spaces, spaces],
            [table_list[4], spaces, table_list[5]],
            ]
    full_table = Table(data)
    full_table.wrapOn(c, 0, 0)
    full_table.drawOn(c, 100, 300)
    return c




def main():
    my_canvas = create_header(course_no = "ARITH 105",
                              section = "01",
                              course_title = "Arithmetics",
                              school = "Hogwarts SWW",
                              instructor = "HFrancis",
                              unit_no = "1",
                              term = "Fall 1991"   
                              )

    students = get_students("Sample Roster 24.xlsx")
    groups = make_groups(students)
    table_list = small_tables(groups)
    my_canvas = plot_tables(my_canvas, table_list)

    my_canvas.showPage()
    my_canvas.save()











if __name__ == "__main__":
    main()