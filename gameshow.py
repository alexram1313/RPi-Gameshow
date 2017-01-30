
import random
class Gameshow:
    __QUESTIONS=[
            ("What is the 10th most populous city in California?","Anaheim"),
            ("True/False? Bir Tawil is a piece of unclaimed between Egypt and Libya","False"),
            ("Sabritones come from which country?","Mexico"),
        ]
    
    def __init__(self):
        self.__player1 = 0
        self.__player2 = 0
        self.__current = ()

    def get_player1_score(self):
        return self.__player1

    def get_player2_score(self):
        return self.__player2

    def inc_player1_score(self):
        self.__player1 += 1

    def inc_player2_score(self):
        self.__player2 += 1

    def next_question(self):
        while True:
            next_q = random.choice(Gameshow.__QUESTIONS)
            if next_q != self.__current:
                self.__current = next_q
                return self.__current
