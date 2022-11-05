import turtle
import random


def face_base(c,r,x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.forward(r)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def nose(c,r,x,y):
    turtle.penup()
    turtle.forward(r)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def eye(r,c,x,y,x1,y1):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.forward(r)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(r/2)
    turtle.right(90)
    turtle.pendown()
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.circle(r/2)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(r/4)
    turtle.right(90)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(r/4)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def get_hex():
    x = random.randint(0,15)
    if x == 0:
        return "0"
    else:
        return hex(x).lstrip("0x")

def iris_color():
    iris_color_red_a = get_hex()
    iris_color_red_b = get_hex()
    iris_color_green_a = get_hex()
    iris_color_green_b = get_hex()
    iris_color_blue_a = get_hex()
    iris_color_blue_b = get_hex()
    iris_color = "".join(["#",iris_color_red_a,iris_color_red_b,iris_color_green_a,iris_color_green_b,iris_color_blue_a,iris_color_blue_b])
    return iris_color

def mouth(r,x,y):
    turtle.penup()
    turtle.goto(-r*.6+x,-r*.25+y)
    turtle.right(90)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(r*.6,180)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.pendown()


def draw_face(x,y,c):
    turtle.speed(12)
    face_color = "gold"
    face_size = 100
    face_base(face_color,face_size,x,y)

    nose_color = "indianred1"
    nose(nose_color, face_size*.1,x,y)

    eye(face_size/4,c,x,y,face_size*.35+x,face_size*.25+y)
    eye(face_size/4,c,x,y,face_size*-.35+x,face_size*.25+y)

    mouth(face_size,x,y)

def main():
    j = input("# of faces: ")
    j = int(j)
    i = 0
    while i < j:
        draw_face(random.randint(-250,250),random.randint(-250,250),iris_color())
        i = i+1

# Your Mother!
main()