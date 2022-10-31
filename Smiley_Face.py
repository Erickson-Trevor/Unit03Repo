import turtle

def face_base(c,r):
    turtle.penup()
    turtle.forward(r)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.pendown()

def nose(c,r):
    turtle.penup()
    turtle.forward(r)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.pendown()

def eye(r,c,x,y):
    turtle.penup()
    turtle.goto(x,y)
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
    turtle.home()
    turtle.pendown()

def mouth(r):
    turtle.penup()
    turtle.goto(-r*.6,-r*.25)
    turtle.right(90)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(r*.6,180)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.pendown()


def main():
    turtle.speed(6)
    face_color = "gold"
    face_size = 100
    face_base(face_color,face_size)

    nose_color = "indianred1"
    nose(nose_color, face_size*.1)

    iris_color = "dodgerblue3"
    eye(face_size/4,iris_color,face_size*.35,face_size*.25)
    eye(face_size/4,iris_color,face_size*-.35,face_size*.25)

    mouth(face_size)

    input("Awaiting imput: ")

main()
