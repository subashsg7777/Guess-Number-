from tkinter import *
import random 
dashboard = Tk()
dashboard.geometry("500x300")
dashboard.title("Guess The Number (Mark 2)")
#dashboard.bg("yellow")
question = Label(dashboard,text = "Guess the number b/w 1 and 15")
text_box = Text(dashboard,height=1,width=20)
rand_num = random.randint(1,15)
def checking():
	#print("the number is being checking by the compiler Please wait if this has been shown more than a 5 sec the restart the Game!")
	value=text_box.get(1.0, "end-1c")
	parsed_value = int(value)
	if(parsed_value == rand_num):
		result = Label(dashboard,text="You Got The Right Answer! Bro!")
		result.grid()
	elif(parsed_value > rand_num):
		result = Label(dashboard,text="To Judged Little High please Guess again!")
		result.grid()
	elif(parsed_value < rand_num):
		result = Label(dashboard,text="You Judged Little Low please Guess again!")
		result.grid()
def reload():
	rand_num = random.randint(1,15)
	print(rand_num)
button = Button(dashboard,text ="Check!",command = checking,height = 5,width = 40,bg = "red")
reload_button = Button(dashboard,text ="Reload Game!",command = reload,bg = "red")
reload_button.grid(row = 10,column = 8)
# here we pack all the things 
question.grid()
text_box.grid()
button.grid()
dashboard.mainloop()

''' inp = inputtxt.get(1.0, "end-1c") '''