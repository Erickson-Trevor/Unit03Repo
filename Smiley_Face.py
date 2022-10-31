import turtle

def face_base(a,b):
    turtle.penup()
    turtle.forward(b)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor(a)
    turtle.begin_fill()
    turtle.circle(b)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.pendown()

def nose(a,b):
    turtle.penup()
    turtle.forward(b)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor(a)
    turtle.begin_fill()
    turtle.circle(b)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    turtle.pendown()


def main():
    face_color = "gold"
    face_size = 100
    face_base(face_color,face_size)
    nose_color = "indianred1"
    nose(nose_color, face_size*.1)
    input("Awaiting imput: ")

main()
