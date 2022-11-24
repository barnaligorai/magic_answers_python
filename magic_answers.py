import random
import sys

class magic_answers:
    def __init__(self, name):
        self.__name = name
        self.__questions = []
        self.__start_game()

    def __start_game(self):
        print("welcome " + self.__name)
        responses = ["It is certain", "As I see it, yes","As I see it, no", "You may rely on it", "It is decided so", "Without a doubt", "Yes definitely", "Ofcourse not"]
        
        while(True):
            question = input("Ask me a question : ")
            if question == "":
                print("Thank you for playing.")
                sys.exit()

            respondWith = responses[random.randint(0,7)]
            self.__questions.append(question)
            print(respondWith)
    
name = input("Enter your name : ")
game = magic_answers(name)
