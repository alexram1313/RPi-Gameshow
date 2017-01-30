import gameshow
import tkinter
import math

_FONT_FAM = 'Ariel'
#_FONT_FAM = 'Trebuchet MS'
_FONT_SIZE= 35
_Q_LBL_RAT= 35/(720*480)
_GAME_BG  = '#003366'
_SCORE_BG  = 'black'
_TEXT_CLR = 'white'

class GameshowWindow:
    

    def __init__(self, controller):
        self._game = gameshow.Gameshow()
        self._controller = controller
        self._init_win_form()
        self._create_info_disp()
        

    def _init_win_form(self)->None:
        self._window = tkinter.Tk()
        self._window.title('GAAAAMESHOW')

        self._window.protocol("WM_DELETE_WINDOW", self._on_close)
        
        self._frm_score = tkinter.Frame(master=self._window,
                background=_SCORE_BG)
        self._frm_score.grid(row=0, column=0,
                sticky=tkinter.W+tkinter.E+tkinter.S+tkinter.N)
        
                             
        self._frm_game = tkinter.Frame(master=self._window,
                background=_GAME_BG)
        self._frm_game.grid(row=1, column=0,
                sticky=tkinter.W+tkinter.E+tkinter.S+tkinter.N)

        self._lbl_question = tkinter.Label(master=self._frm_game,
                                      text = "GAAAAME!",
                                      font=(_FONT_FAM,_FONT_SIZE),
                foreground = _TEXT_CLR,
                background = _GAME_BG,
                                           wraplength=1000) 
        self._lbl_question.grid(row=0, column=0,
                           sticky=tkinter.W+tkinter.E+tkinter.S+tkinter.N)

        self._lbl_answer = tkinter.Label(master=self._frm_game,
                                      text = "Answer Here",
                                      font=(_FONT_FAM,_FONT_SIZE),
                foreground = _TEXT_CLR,
                background = _GAME_BG,) 


        self._frm_game.rowconfigure(0, weight=1)
        self._frm_game.rowconfigure(1, weight=3)
        self._frm_game.columnconfigure(0, weight=1)
        
        
        self._strip_new_game = tkinter.Frame(master=self._window)
        self._strip_new_game.grid(row=2, column=0,
                sticky=tkinter.W+tkinter.E+tkinter.S)
        self._btn_new_game = tkinter.Button(master=self._strip_new_game,
                text='Next Question', command=self._controller.next_question )
        self._btn_new_game.grid(row=0, column=0, padx=5, sticky=tkinter.W)

        self._btn_reveal = tkinter.Button(master=self._strip_new_game,
                text='Reveal Answer?',state=tkinter.DISABLED,
                        command=self._controller.reveal_question)
        self._btn_reveal.grid(row=0, column=1, padx=5, sticky=tkinter.W)
        
        self._btn_right = tkinter.Button(master=self._strip_new_game,
                text='Correct?',state=tkinter.DISABLED,
                        command=self._controller.correct)
        self._btn_right.grid(row=0, column=2, padx=5, sticky=tkinter.W)

        self._btn_reset = tkinter.Button(master=self._strip_new_game,
                text='Reset',command=self._controller.reset)
        self._btn_reset.grid(row=0, column=3, padx=5, sticky=tkinter.E)

        
                
        self._window.rowconfigure(0, weight=10)
        self._window.rowconfigure(1, weight=100)
        self._window.rowconfigure(2, weight=1)
        self._window.columnconfigure(0,weight=1)
        self._window.geometry('500x600')
        self._last_width = self._frm_score.winfo_width()
        self._frm_score.bind('<Configure>', self._frm_score_resized)

    def _create_info_disp(self)->None:
        self._lbl_score = tkinter.Label(master=self._frm_score,
                text=" (0 - 0) ",
                font=(_FONT_FAM,_FONT_SIZE),
                foreground = _TEXT_CLR,
                background = _SCORE_BG) 
        self._lbl_score.grid(row=0, column=1)        
        
        self._frm_score.rowconfigure(0, weight=1)
        self._frm_score.columnconfigure(0,weight=1)
        self._frm_score.columnconfigure(1,weight=9)
        self._frm_score.columnconfigure(2,weight=1)

    def _frm_score_resized(self, event: tkinter.Event)->None:
        self._resize_info_labels()
        
        
    def _resize_info_labels(self)->None:
        score_size=(self._window.winfo_height()*self._window.winfo_width())\
            * _Q_LBL_RAT
            
        if score_size > 50.0:
            score_size = 50
        self._lbl_score['font'] = (_FONT_FAM, int(math.ceil(score_size)))
    def _on_close(self):
        self._controller.close()
        self._window.destroy();

    def run_app(self):
        self._window.mainloop()

    def set_score(self, text):
        self._lbl_score['text'] = text

    def set_question(self, text):
        self._lbl_question['text'] = text
    def set_answer(self, text):
        self._lbl_answer['text'] = text

    def btn_enable(self, btn):
        btn['state'] = 'normal'
    def btn_disable(self, btn):
        btn['state'] = tkinter.DISABLED
    def show_answer(self):
        self._lbl_answer.grid(row=1, column=0,
                           sticky=tkinter.W+tkinter.E+tkinter.S+tkinter.N)
    def hide_answer(self):
        self._lbl_answer.grid_forget()

    def update(self):
        self._window.update()

if __name__ == '__main__':
    app = GameshowWindow(None)
    app.run_app()
