import turtle

def face(a,b):
    turtle.fillcolor(a)
    turtle.begin_fill()
    turtle.circle(b)
    turtle.end_fill()

def main():
    face_color = "gold"
    face_size = 100
    face(face_color,face_size)
    input("Awaiting imput: ")

main()
