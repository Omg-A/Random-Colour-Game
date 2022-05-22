from tkinter import *
import random

root = Tk()
root.title("Color Guesser")
root.geometry("400x400")
root.configure(background="gold")

label_title = Label(root, text="Color Guesser", font=("sans serif", 25), bg="gold")
label_title.place(relx=0.5, rely=0.1, anchor=CENTER)

label_name = Label(root, font=("sans serif", 20), bg="gold")
label_name.place(relx=0.5, rely=0.3, anchor=CENTER)

input_color = Entry(root)
input_color.place(relx=0.5, rely=0.5, anchor=CENTER)

label_score = Label(root, text="Score: 0", bg="gold")
label_score.place(relx=0.1, rely=0.05, anchor=CENTER)

class Game:
    def __init__(self):
        self.__score = 0
    
    def updateGame(self):
        self.text = ["Pink", "Green", "Blue", "Yellow", "Red"]
        self.random_text = random.randint(0, 4)
        
        self.color = ["red", "pink", "yellow", "green", "blue"]
        self.random_color = random.randint(0, 4)
        
        label_name["text"] = self.text[self.random_text]
        label_name["fg"] = self.color[self.random_color]
    
    def __updateScore(self, input_value):
        if(input_value == self.color[self.random_color]):
            self.__score = self.__score + random.randint(0, 10)
            label_score["text"] = "Score: " + str(self.__score)
    
    def getUserValue(self, input_value):
        self.__updateScore(input_value)

obj = Game()

def getInput():
    value = input_color.get()
    obj.getUserValue(value)
    obj.updateGame()
    input_color.delete()

game_object = Game()

button = Button(root, text="Start", bg="green1", fg="green4", padx=10, pady=1, font=("Arial", 13, "bold"), command=obj.updateGame)
button.place(relx=0.6, rely=0.7, anchor=CENTER)

button = Button(root, text="Check", bg="red1", fg="red4", padx=10, pady=1, font=("Arial", 13, "bold"), command=getInput())
button.place(relx=0.4, rely=0.7, anchor=CENTER)

root.mainloop()