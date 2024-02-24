THEME_COLOR = "#375362"
from tkinter import Tk
from tkinter import Canvas,messagebox
from tkinter import * 
from quiz_brain import QuizBrain

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.photo1 =  PhotoImage(file = "D34/quizzler-app-start/images/true.png")
        self.photo2 = PhotoImage(file = "D34/quizzler-app-start/images/false.png")
        self.window.title("Quizzler")
        self.window.config(padx = 20 , pady = 20 , bg = THEME_COLOR)
        self.window.geometry("450x550")
        self.canvas = Canvas(width = 300 , height = 250 , bg = "white")
        self.canvas.grid(row =1 , column = 0 , columnspan = 2 , pady = 50 , padx = 50 )

        self.right_button = Button(self.window, image = self.photo1 , command = self.true_pressed)
        self.right_button.grid(row = 2 , column = 0 , pady = 10 , padx = 10)

        self.left_button = Button(self.window, image = self.photo2 , command = self.false_pressed) 
        self.left_button.grid(row =2 , column =1 , pady = 10 , padx = 10)  

        self.score_label = Label(text = f"Score: 0" , bg = THEME_COLOR , fg = "white",  font = "Arial 20 italic")
        self.score_label.grid(row = 0 , column = 1 , pady = 10 , padx = 10)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text  , text = question)
        else:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz.\n Final Score: {self.quiz.score}/{self.quiz.question_number}")  
            self.right_button.config(state = "disabled")
            self.left_button.config(state = "disabled")
            self.window.after(2000, self.play_again)
          

    def play_again(self):
        response = messagebox.askyesno("Quizzler", "Do you want to play again?")
        if response:
            self.quiz.score = 0 
            self.quiz.question_number = 0
            self.right_button.config(state="active")
            self.left_button.config(state="active")
            self.get_next_question()
        else:
            self.window.quit()
            

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def true_pressed(self):    
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def feedback(self,is_right):
        if is_right ==  True:
            self.canvas.config(bg = "green")

        else: 
            self.canvas.config(bg = "red")

        self.window.after(1250, self.get_next_question)
        
        
        
  

        

