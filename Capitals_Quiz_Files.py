import random
import os.path

capitals_dic = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}
# Create directory for the quiz and answer files
current_directory = os.getcwd()
quiz_file_directory = os.path.join(current_directory, "quiz_folder")
if not os.path.isdir(quiz_file_directory):
    os.mkdir("quiz_folder")
os.chdir(quiz_file_directory)

# Generate 35 quiz files with the questions in random order
for quizNum in range(35):
    # Create quiz and answer key files
    quizFile = open(f"capitalQuiz_{quizNum+1}.txt", 'w')
    answerFile = open(f"capitalQuizAnswers_{quizNum+1}.txt", 'w')

    # Write the header for the quiz

    quizFile.write('Name:\nDate:\n\n\n')
    quizFile.write(f'States Capital Quiz #{quizNum+1}\n\n')
    states = list(capitals_dic)
    random.shuffle(states)

    # loop through 50 states and create the questions and 4 answers
    # one correct answer with three wrong answers

    for questionNumber in range(50):
        correctAnswer = capitals_dic[states[questionNumber]]
        wrongAnswers = list(capitals_dic.values())  # create list of all of the answer values
        del wrongAnswers[wrongAnswers.index(correctAnswer)]  # only wrong answers are left in the list
        wrongAnswers = random.sample(wrongAnswers, 3)  # reduces list to only 3
        answerOptions = wrongAnswers + [correctAnswer]  # new list of only 4 options
        random.shuffle(answerOptions)  # randomize the order of the answers

        # Write to file
        quizFile.write(f"{questionNumber}) What is the capital of {states[questionNumber]}?\n")
        for i in range(4):
            quizFile.write(f"\t{'ABCD'[i]}) {answerOptions[i]}\n")
        quizFile.write('\n')

        # Write to answer file
        answerFile.write(f"{questionNumber}) {'ABCD'[answerOptions.index(correctAnswer)]}\n")

    # Close files
    quizFile.close()
    answerFile.close()
