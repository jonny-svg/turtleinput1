import turtle
import random

screen = turtle.Screen()

screen.screensize(500,500)
screen.bgcolor('black')





t = turtle.Turtle()
#menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("red")


t.write("background color",font=("arial" ,30 ,"normal"),align="center")
t.penup()
t.goto(0,100)
t.pendown()
t.pencolor("white")




t.penup()
t.goto(0,150)
t.pendown()
t.pencolor("tan")
t.write("1. tan",font=("arial" ,30 ,"normal"),align="center")


t.penup()
t.goto(0,100)
t.pendown()
t.pencolor("azure")
t.write("2. Azure",font=("arial" ,30 ,"normal"),align="center")

t.penup()
t.goto(0,50)
t.pendown()
t.pencolor("Aquamarine")
t.write("3. Aquamarine",font=("arial" ,30 ,"normal"),align="center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("Dark khaki")
t.write("4. Dark khaki",font=("arial" ,30 ,"normal"),align="center")

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor("white")
t.write("chose one",font=("arial" ,30 ,"normal"),align="center")

choose = int(input("choose one: "))
if choose == 1:
    screen.bgcolor('tan')
elif choose == 2:
    screen.bgcolor('azure')
elif choose == 3:
    screen.bgcolor('aquamarine')
elif choose == 4:
    screen.bgcolor('dark khaki')


t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("black")
t.write("Enter your name",font=("arial" ,30 ,"normal"),align="center")

name= input("enter your name: ")
t.clear()





# num1 =int(input("enter a number: "))
# num2 =int(input("enter another number: "))
operator = random.randint (1,4)
if operator ==1:
    symbol = "+"

    num1 = random.randint(-100,100)
    num2 = random.randint(-100,100)
    solution =num1 + num2


elif operator == 2:
    symbol = "-"

    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    solution = num1 - num2



elif operator == 3:
    symbol = "*"

    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10)
    solution = num1 * num2



elif operator == 4:
    symbol = "/"



    num1 = random.randint(-10, 10)
    num2 = random.randint(1, 10)
    sign = random.randint(1,2)
    if sign == 2:
        num2 = -1*num2


    solution = num1 / num2



t.penup()
t.goto(-0,100)
t.pendown()
t.pencolor("red")


t.write(name,font=("arial" ,30 ,"normal"),align="center")


t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor("blue")
t.write(num1,font=("arial" ,30 ,"normal"),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor("green")
t.write(symbol,font=("arial" ,30 ,"normal"),align="center")


t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("purple")
t.write(num2,font=("arial" ,30 ,"normal"),align="center")




t.penup()
t.goto(100,0)
t.pendown()
t.pencolor("black")
t.write("=",font=("arial" ,30 ,"normal"),align="center")
answer = float(input("what is the answer:"))

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor("pink")
t.write(solution,font=("arial" ,30 ,"normal"),align="center")




t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor("pink")
t.write("your answer is: "+str(answer),font=("arial" ,30 ,"normal"),align="center")

if answer == solution:
    screen.bgcolor("dodgerblue")
    t.penup()
    t.goto(0,50)
    t.pendown()
    t.pencolor("pink")
    t.write("correct:",font=("arial" ,30 ,"normal"),align="center")

else:
    screen.bgcolor('darkorange')

    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.pencolor("pink")
    t.write("incorrect:", font=("arial", 30, "normal"), align="center")




turtle.done()
