# import required modules
import turtle
import time
import random

delay = 0.1
score = 0
highestscore = 0

#snakebodies
bodies=[]

# Creating a window screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
# the width and height can be put as user's choice
s.setup(width=600, height=600)

# head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()

#scoreboard
sb=turtle.Turtle()
sb.speed(0)
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score : 0  |  Highest Score : 0")

# assigning key directions
def moveup():
    if head.direction != "down":
        head.direction = "up"
def movedown():
    if head.direction != "up":
        head.direction = "down"
def moveleft():
    if head.direction != "right":
        head.direction = "left"
def moveright():
    if head.direction != "left":
        head.direction = "right"
def movestop():
    head.direction="stop"   

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


		
s.listen()
s.onkey(moveup, "w")
s.onkey(movedown, "s")
s.onkey(moveleft, "a")
s.onkey(moveright, "d")
s.onkey(movestop, "space")

# Main Gameplay
while True:
    s.update()
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)
        
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        body= turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)
        score += 10
        delay -= 0.001
        if score > highestscore:
            highestscore = score
            sb.clear()
            sb.write("Score : {} High Score : {} ".format(score, highestscore))
    for index in range(len(bodies)-1, 0, -1):
        x = bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x, y)
    if len(bodies)>0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)
    move()
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for body in bodies:
                body.ht()
            bodies.clear()
            score = 0
            delay = 0.1
            sb.clear()
            sb.write("Score : {} Highest Score : {} ".format(score, highestscore), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)

wn.mainloop()
