import pandas as pd

###Dictionary for student answers to be converted into a DF later on
TESTS_DICT = {}
###Dictionary for student grades to be Converted into a DF later on
TESTS_GRADE_DICT = {}
grade_percentage = ["Percentage Grade:"]
grade_index = pd.Index(grade_percentage)

###Number of questions used to prompt the for loop to fill out the list of student answers
NUM_QUESTIONS = int(input("How many questions are on the test?: "))
questions_num_list = [] ##list appended through a for loop to create the Questions # for our Panda DF
for i in range(NUM_QUESTIONS): ##aforementioned for loop
    questions_num_list.append("Question#" + str(i + 1)) ##appending afforementioned for loop
questions_index = pd.Index(questions_num_list) ##setting the fully appended list to function as a Pandas column/index for our comprehensive DF

####Number of tests used to give the below while loop an exit
NUM_OF_TESTS = int(input('How many tests are you grading?: '))

###List to be appended for a teacher answer key
TEACHER_LIST = []

while len(TEACHER_LIST) < len(range(NUM_QUESTIONS)):
    next_teacher_answer = input("What is the next answer in your teacher key?: ")
    TEACHER_LIST.append(next_teacher_answer)

while NUM_OF_TESTS > len(TESTS_DICT):
    student_answers = [] ##Empty list appended throughout the loop
    student_name = input("What is the student's name?: ") ##storing the new key for our dictionary in 'student_name'
    student_correct_answers = 0 ## Number of correct answers to be used to determined student grade
    for answer_t in TEACHER_LIST: ##looping through the answers in TEACHER_LIST in order to input the values for 'student_name' key
        student_answer = input("What answer did your student choose?: ")##Each of the student's answers are stored in 'each_answer' variable
        student_answers.append(student_answer)##'each_answer' variable is the appended to student_answers list from earlier
        if student_answer == answer_t: ##if the student_answer value is equal to the value of answer_t in the TEACHERS_LIST... 
            student_correct_answers += 1 ##increment correct number of student answer by 1
    if len(student_answers) == len(range(NUM_QUESTIONS)): ##if the length of the student_answers list is equal to the length of the range of number of questions on thes test...
        TESTS_DICT[student_name] = student_answers###add the student's name as a key, and their answers list as the value. Repeat until program is completed
        student_grade = (student_correct_answers / NUM_QUESTIONS) * 100
        TESTS_GRADE_DICT[student_name] = [student_grade]

TESTS_DF = pd.DataFrame(TESTS_DICT)##Converting TESTS_DICT to a DataFrame
TESTS_DF = TESTS_DF.set_index(questions_index) ##Setting index of the DataFrame to equal the Question#

TESTS_GRADE_DF = pd.DataFrame(TESTS_GRADE_DICT)##Converting TESTS_GRADE_DICT to a DataFrame
TESTS_GRADE_DF = TESTS_GRADE_DF.set_index(grade_index)##Setting index of the DataFrame to a single row that reads "Percentage Grade:"

print(TESTS_GRADE_DF)
print(TESTS_DF)
print(student_correct_answers)

###TOMORROW, WORK ON WRITING CODE TO LIMIT THE KIND OF INPUT A TEACHER CAN CHOOSE