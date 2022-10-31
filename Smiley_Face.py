import turtle

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


def main(x,y,c):
    turtle.speed(12)
    face_color = "gold"
    face_size = 100
    face_base(face_color,face_size,x,y)

    nose_color = "indianred1"
    nose(nose_color, face_size*.1,x,y)

    iris_color = c
    eye(face_size/4,iris_color,x,y,face_size*.35+x,face_size*.25+y)
    eye(face_size/4,iris_color,x,y,face_size*-.35+x,face_size*.25+y)

    mouth(face_size,x,y)


main(0,0,"firebrick")
main(200,-169,"dimgray")
main(300,30,"dodgerblue3")
input("Awaiting Input: ")
