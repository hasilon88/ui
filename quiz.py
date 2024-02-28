import json, random, os

def readJson(path = "questions.json"):
    with open(path, encoding='utf-8') as fh:
        data = json.load(fh)
    
    return data
    
def run_quiz(questions):
    score = 0
    for question in questions:
        randomNum = random.randint(0,len(questions)-1)
        
        print("\n" + questions[randomNum]["question"])
        print(len(questions[randomNum]["question"]) * "-")
        for key, value in questions[randomNum]["options"].items():
            print(f"\n{key}: {value}")
        user_answer = input("\nVotre réponse: ").upper()
        if user_answer == questions[randomNum]["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("\nIncorrect.\nLa bonne réponse est:", questions[randomNum]["answer"])        
        
        questions.pop(randomNum)
        input("\nPesez sur ENTER pour la prochaine question.")
        os.system("cls")
        
    print(f"Votre score est de {score}/{len(questions)}.")

run_quiz(readJson())