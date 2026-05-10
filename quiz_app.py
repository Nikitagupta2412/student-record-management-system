score = 0
print("start quiz")
questions=[
    {"question":"capital of india?",
     "options":["a)delhi","b)jaipur","c)mumbai","d)hyderabad"],
     "answer":"a"
    },
    {"question":"what is the full form of AI?",
     "options":["a)apple intelligence","b)artificial intelligence","c)aromatic interference","d)abnormal intelligence"],
     "answer":"b"
    },
    {"question":"which is a keyword in python?",
     "options":["a)hello","b)command","c)for","d)follow"],
     "answer":"c"
    }
    ]

for i in questions:

    print(i["question"])

    for option in i["options"]:
        print(option)

    answer = input("Enter your answer: ")

    if answer == i["answer"]:
        score += 10
        print("Correct answer")
        print("Current score =", score)

    else:
        print("Wrong answer")

print("\nFinal Score =", score)
