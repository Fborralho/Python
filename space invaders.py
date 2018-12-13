import turtle
import math
import random


wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

boarder_pen = turtle.Turtle()
boarder_pen.speed(0)
boarder_pen.color("black")
boarder_pen.penup()
boarder_pen.goto(-300,-300)
boarder_pen.pensize(3)
boarder_pen.pendown()
boarder_pen.forward(600)
boarder_pen.left(90)
boarder_pen.forward(600)
boarder_pen.left(90)
boarder_pen.forward(600)
boarder_pen.left(90)
boarder_pen.forward(600)
boarder_pen.left(90)
boarder_pen.hideturtle()

turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

score = 0
score_pen = turtle.Turtle()
score_pen.color("Green")
score_pen.penup()
score_pen.hideturtle()
score_pen.speed(0)
score_pen.setposition(-290,280)
scorestring = "Score: %s" %score

score_pen.write(scorestring,False,align= "left",font=("Arial",14,"normal"))


player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.left(90)

playerspeed = 15


n_of_enemies = 10
enemies = []

for i in range(n_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.speed(0)
    enemy.penup()
    enemy.shape("invader.gif")
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x, y)

enemyspeed = 5

bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.35,0.35)
bullet.hideturtle()

bulletspeed = 50
bulletstate = "ready"

def firebullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() +10
        bullet.setpos(x,y)
        bullet.showturtle()


def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def isCollision(t1, t2):
    distance = math.sqrt((t1.xcor()-t2.xcor())**2+(t1.ycor()-t2.ycor())**2)
    if distance < 15:
        return True
    else:
        return False




turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(firebullet, "space")



while True:
    for enemy in enemies:

        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1


        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setpos(0, -400)
            x = random.randint(-200,200)
            y = random.randint(100,280)
            enemy.setposition(x,y)
            score += 1
            scorestring = "Score %s" %score
            score_pen.clear()
            score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))

        if isCollision(enemy, player):
            enemy.hideturtle()
            player.hideturtle()
            break
            print("GAME OVER")
            
        if enemy.ycor() <= -250:
            enemy.hideturtle()
            player.hideturtle()
            break
            print("GAME OVER")

        if score == 25:
            break
            print("WINNER WINNER CHICKEN DINNER")

    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"





delay = input("Press Enter to finish")
