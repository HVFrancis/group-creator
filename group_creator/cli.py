# cli.py

# A simple interface for the group_craetor app.
# Currently it implements a Q/A session for the necessary 
# parameter values.

import make_groups, make_pdf


def main():
    filename = input("Excel filename: ")
    course_no = input("Course number: ")
    course_title = input("Course title: ")
    school = input("Institution Name: ")
    instructor = input("Instructor Name: ")
    term = input("Semester: ")
    unit_no = input("Unit number: ")

    rosters = make_groups.get_rosters(filename)
    all_groups = make_groups.make_multiple_groups(rosters)
    for key in all_groups:

        my_canvas = make_pdf.create_header(course_no = course_no,
                                  section = key,
                                  course_title = course_title,
                                  school = school,
                                  instructor = instructor,
                                  unit_no = unit_no,
                                  term = term  
                                  )
    
        table_list = make_pdf.small_tables(all_groups[key])
        my_canvas = make_pdf.plot_tables(my_canvas, table_list)

        my_canvas.showPage()
        my_canvas.save()







if __name__ == "__main__":
    main()