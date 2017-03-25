from gameshow import Gameshow
from test_window import GameshowWindow
from buzzermatch import BuzzerMatch

BTN1 = 11
LED1 = 12
BTN2 = 40
LED2 = 36

class GameshowController:
    def __init__(self, team1="Team 1", team2="Team 2"):
        self._game = Gameshow()
        self._team1 = team1
        self._team2 = team2
        self._view = GameshowWindow(self)
        self._buzzer = BuzzerMatch(BuzzerMatch.GPIO_BOARD, BTN1, LED1, BTN2, LED2)
        self.set_score_view()
        self._view.run_app()
    def start_buzzer(self):
        #GPIO
        pass
    def team1_correct(self):
        self._game.inc_player1_score()
        return self._game.get_player1_score()
    def team2_correct(self):
        self._game.inc_player2_score()
        return self._game.get_player2_score()
    def get_score(self):
        return (self._game.get_player1_score(), self._game.get_player2_score())
    def set_score_view(self, team_sel = -1):
        #print(team_sel)
        if team_sel == 0:
            self._view.set_score(">"+self._team1+ "< "+str(self.get_score()) +" " +self._team2)
        elif team_sel == 1:
            self._view.set_score(self._team1+ " "+ str(self.get_score()) +">" +self._team2+"<")
        else:
            self._view.set_score(self._team1+ " "+ str(self.get_score()) +" " +self._team2)

    def next_question(self):
        self._view.hide_answer()
        self._view.btn_disable(self._view._btn_right)
        question = self._game.next_question()
        self._view.set_question(question[0])
        self._view.set_answer(question[1])
        self._view.update()
        self._player = self._buzzer.play()
        if self._player != None:
            self.set_score_view(self._player)
        self._view.btn_enable(self._view._btn_reveal)

    def reveal_question(self):
        self._view.show_answer()
        if self._player != None:
            self._view.btn_enable(self._view._btn_right)

    def correct(self):
        self._view.btn_disable(self._view._btn_right)
        self.team1_correct() if not self._player else self.team2_correct()
        self.set_score_view()

    def reset(self):
        self._player = None
        self._buzzer.reset()
        self._view.hide_answer()
        self._view.btn_disable(self._view._btn_right)


    def close(self):
        self._buzzer.cleanup()
        
        

if __name__ == "__main__":
    controller = GameshowController()
