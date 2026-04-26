import turtle
import time
import random


class Pasaulis:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Gyvaciuks")
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=500)
        self.screen.tracer(0)

    def update(self):
        self.screen.update()


class Galva(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.goto(0, 0)
        self.direction = "stop"
        self.gali_keistijudesi = True

    def go_up(self):
        if self.direction != "down" and self.gali_keistijudesi:
            self.direction = "up"
            self.gali_keistijudesi = False

    def go_down(self):
        if self.direction != "up" and self.gali_keistijudesi:
            self.direction = "down"
            self.gali_keistijudesi = False

    def go_right(self):
        if self.direction != "left" and self.gali_keistijudesi:
            self.direction = "right"
            self.gali_keistijudesi = False

    def go_left(self):
        if self.direction != "right" and self.gali_keistijudesi:
            self.direction = "left"
            self.gali_keistijudesi = False

    def judejimas(self):

        if self.direction == "up":
            self.sety(self.ycor() + 20)
        if self.direction == "down":
            self.sety(self.ycor() - 20)
        if self.direction == "right":
            self.setx(self.xcor() + 20)
        if self.direction == "left":
            self.setx(self.xcor() - 20)


class Maistas(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(0, 100)

    def vieta(self, gyvate):
        while True:
            x = random.randrange(-280, 280, 20)
            y = random.randrange(-180, 180, 20)

            laisva = True
            if abs(x - gyvate.galva.xcor()) < 20 and abs(y - gyvate.galva.ycor()) < 20:
                laisva = False

            for segmentas in gyvate.uodega:
                if abs(x - segmentas.xcor()) < 20 and abs(y - segmentas.ycor()) < 20:
                    laisva = False
                    break
            if laisva:
                self.goto(x, y)
                break


class Kunas:
    def __init__(self, galva):
        self.galva = galva
        self.uodega = []

    def augimas(self):
        naujas_segmentas = turtle.Turtle()
        naujas_segmentas.speed(0)
        naujas_segmentas.shape("square")
        naujas_segmentas.color("lightgreen")
        naujas_segmentas.penup()

        if len(self.uodega) > 0:
            paskutinis_x = self.uodega[-1].xcor()
            paskutinis_y = self.uodega[-1].ycor()
        else:
            paskutinis_x = self.galva.xcor()
            paskutinis_y = self.galva.ycor()

        naujas_segmentas.goto(paskutinis_x, paskutinis_y)

        self.uodega.append(naujas_segmentas)

    def uodegos_judejimas(self):
        for i in range(len(self.uodega) - 1, 0, -1):
            x = self.uodega[i - 1].xcor()
            y = self.uodega[i - 1].ycor()
            self.uodega[i].goto(x, y)

        if len(self.uodega) > 0:
            self.uodega[0].goto(self.galva.xcor(), self.galva.ycor())

    def isnyk(self):
        for dalis in self.uodega:
            dalis.goto(1000, 1000)
            dalis.hideturtle()
        self.uodega.clear()
        self.galva.goto(0, 0)
        self.galva.direction = "stop"

class Rezultatas(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        try:
            with open("rekordas.txt", "r") as failas:
                self.high_score = int(failas.read())
        except:
            self.high_score = 0

        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 210)
        self.rasyti()

    def rasyti(self):
        self.clear()
        self.goto(0, 210)
        self.write(f"Taskai: {self.score} Rekordas: {self.high_score}",
                   align="center", font=("Courier", 16, "normal" ))

    def prideti_taska(self):
        self.score +=1
        self.rasyti()

    def rodyti_mirti(self):
        self.goto(0, 60)
        self.color("red")
        self.write(f"WOMP WOMP\nscore: {self.score}",
                   align="center", font=("Courier", 24, "normal" ))

        turtle.Screen().update()

        if self.score > self.high_score:
            self.high_score = self.score

        with open("rekordas.txt", "w") as failas:
            failas.write(str(self.high_score))

        time.sleep(2)

        self.score = 0
        self.clear()
        self.color("white")
        self.goto(0, 210)
        self.rasyti()

        turtle.Screen().update()

if __name__ == "__main__":
    game = Pasaulis()
    head = Galva()
    maistas = Maistas()
    gyvaciukas = Kunas(head)
    rezultatas = Rezultatas()

    rem = turtle.Turtle()
    rem.hideturtle()
    rem.penup()
    rem.color("yellow")
    for x in range(-300, 301, 10):
        rem.goto(x, 190)
        rem.write("|", align="center")
        rem.goto(x, -210)
        rem.write("|", align="center")
    for y in range(-210, 201, 20):
        rem.goto(-300, y)
        rem.write("|", align="center")
        rem.goto(300, y)
        rem.write("|", align="center")

    game.screen.listen()
    game.screen.onkey(head.go_up, "Up")
    game.screen.onkey(head.go_down, "Down")
    game.screen.onkey(head.go_right, "Right")
    game.screen.onkey(head.go_left, "Left")

    while True:
        game.update()
        gyvaciukas.uodegos_judejimas()
        head.judejimas()
        head.gali_keistijudesi = True

        time.sleep(0.2)

        if head.xcor() > 290 or head.xcor() < -290:
            rezultatas.rodyti_mirti()
            gyvaciukas.isnyk()

        if head.ycor() > 190 or head.ycor() < -190:
            rezultatas.rodyti_mirti()
            gyvaciukas.isnyk()

        if head.distance(maistas) < 20:
            maistas.vieta(gyvaciukas)
            gyvaciukas.augimas()
            rezultatas.prideti_taska()

        for segmentas in gyvaciukas.uodega[1:]:
            if head.distance(segmentas) < 20:
                rezultatas.rodyti_mirti()
                gyvaciukas.isnyk()


