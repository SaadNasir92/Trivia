import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
QUESTION_FONT = ('Arial', 20, 'italic')

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # window
        self.win = tk.Tk()
        self.win.title('Quizzler')
        self.win.config(pady=20, padx=20, bg=THEME_COLOR)

        # canvas
        self.canvas = tk.Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Some Question Text',
            font=QUESTION_FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #labels
        self.score_label = tk.Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        #buttons
        true_button_img = tk.PhotoImage(file='images/true.png')
        self.true_button = tk.Button(image=true_button_img, highlightthickness=0, command=self.true_click)
        self.true_button.grid(column=1, row=2)

        false_button_image = tk.PhotoImage(file='images/false.png')
        self.false_button = tk.Button(image=false_button_image, highlightthickness=0, command=self.false_click)
        self.false_button.grid(column=0, row=2)

        self.update_canvas_question()
        self.win.mainloop()

    def update_canvas_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_label.config(text=f'Final Score: {self.quiz.score}/{self.quiz.question_number}')
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def true_click(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_click(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.win.after(1000, self.update_canvas_question)

