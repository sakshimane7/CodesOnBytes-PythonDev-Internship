import random

# Define a list of 30 questions and answers as tuples.
questions_and_answers = [
    ("Which planet is nearest to Earth?", "Venus"),
    ("Who is the founder of Microsoft?", "Bill Gates"),
    ("Which place is known as tea garden of India?", "Assam"),
    ("What is the capital of France?", "Paris"),
    ("How many continents are there?", "7"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("Total number of oceans in the World is", "5"),
    ("Which one is the biggest island in the World?", "Greenland"),
    ("Which one is the largest tropical rain forest in the world?", "Amazon"),
    ("How many elements are in the periodic table?", "118"),
    ("Plants synthesis protein from", "Amino acids"),
    ("The Indian Air Force celebrated its Golden Jubilee in", "1982"),
    ("The members of the state legislative assemblies are elected for a period of", "5 years"),
    ("OS computer abbreviation usually means?", "Operating System"),
    (".MOV extension refers usually to what kind of file?", "Video file"),
    ("Who developed Python Programming language?", "Guido van Rossum"),
    ("Where is the Railway Staff College located?", "Vadodara"),
    ("The Indian Institute of Science is located at", "Bangalore"),
    ("Which city is known as 'Electronic City of India?", "Bangalore"),
    ("Which city is called 'White City' of Rajasthan?", "Udaipur"),
    ("Who is the father of C language?", "Dennis Ritche"),
    ("Who is the prime minister of india?", "Narendra Modi"),
    ("Who is the president of India?", "Droupadi Murmu"),
    ("1024 Kilobytes is equal to?", "1 MB"),
    ("Brain of computer is?", "CPU"),
    ("Which is the longest river on the earth?", "Nile"),
    ("Smallest state of India is?", "Goa"),
    ("Which is the animal referred as the ship of the desert?", "Camel"),
    ("A figure with 8 sides is called?", "Octagon"),
    ("Which organ purify our blood?", "Kidney"),
    # Add more questions and answers here...
]

# Function to run the quiz.


def run_quiz(num_questions):
    # Shuffle the questions randomly.
    random.shuffle(questions_and_answers)

    # Initialize a variable to keep track of the user's score.
    score = 0

    for i in range(num_questions):
        # Get a random question and its answer.
        question, correct_answer = questions_and_answers[i]

        # Prompt the user with the question.
        print(f"Question {i + 1}: {question}")

        # Get the user's input.
        user_answer = input("Your answer: ")

        # Check if the user's answer is correct.
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}\n")

    # Display the final score.
    print(f"You got {score}/{num_questions} questions correct.")


if __name__ == "__main__":
    # Change this to the number of questions you want in the quiz.
    num_questions = 30
    run_quiz(num_questions)
