#define two variables for a student:
#student_name and student_major. The student_major variable will contain a
#code for the student’s major (e.g. ENG).
student_name = 'Bill Nye' #'Mary Jane'

def student_major(code):
    match code:
        case 'BIOL':
            print('Biology, Science Bldg, Room 310')
        case 'CSCI':
            print('Computer Science, Sheppard Hall, Room 314')
        case 'ENG':
            print('English, Kerr Hall, Room 201')
        case 'HIST':
            print('History, Kerr Hall, Room 114')
        case 'MKT':
            print('Marketing, Westly Hall, Room 310')
        case _:
            print('<Unknown>')
print(student_name)
student_major('PHIL')
# made up major code PHIL for philosophy