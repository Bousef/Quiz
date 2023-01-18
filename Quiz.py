#a Dictionary that stores the questions and answers
#Have a variable tracking the user score
#Loop through the Dictionary using the key value pairs
#display each question 
#tell them if they are right or wrong
#show final result when quiz is completed

quiz = {
    "question1":{
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer":"Berlin"
    },
    "question3": {
        "question":"What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question":"What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question":"What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "question":"What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7": {
        "question":"What is the capital of Austria?",
        "answer": "Vienna"
    },
}

while True:
    score = 0
    print(quiz["question1"].get('question'))
    user_input1 = input("What would your answer be?: ")

    if user_input1.lower() == 'paris':
        score = score + 1
        print("Great Job! Your score is now: ",score)
        
    else:
        print("Better luck next time Your score is now: ",score)
    
    print(quiz["question2"].get('question'))
    user_input2 = input("What would your answer be?: ")
    if user_input2.lower() == 'berlin':
        score = score + 1
        print("Great Job! Your score is now: ",score)
    else:
        print("Better luck next time Your score is now: ",score)

    print(quiz["question3"].get('question'))
    user_input3 = input("What would your answer be?: ")

    if user_input3.lower() == 'rome':
        score = score + 1
        print("Great Job! Your score is now: ",score)
    else:
        print("Better luck next time Your score is now: ",score)
    
    print(quiz["question4"].get('question'))
    user_input4 = input("What would your answer be?: ")
    if user_input4.lower() == 'madrid':
        score = score + 1
        print("Great Job! Your score is now: ",score)
    else:
        print("Better luck next time Your score is now: ",score)
        
    print(quiz["question5"].get('question'))
    user_input5 = input("What would your answer be?: ")

    
    if user_input5.lower() == 'lisbon':
        score = score + 1
        print("Great Job! Your score is now: ",score)
    else:
        print("Better luck next time Your score is now: ",score)
    
    print(quiz["question6"].get('question'))
    user_input6 = input("What would your answer be?: ")
    if user_input6.lower() == 'bern':
        score = score + 1
        print("Great Job! Your score is now: ",score)
    else:
        print(quiz["question1"].get('question'))
    user_input7 = input("What would your answer be?: ")

    if user_input7.lower() == 'vienna':
        score = score + 1
        print("Great Job! Your score is now: ",score)
    else:
        print("Better luck next time Your score is now: ",score)
    break