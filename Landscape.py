import turtle

Ross = turtle.Turtle()
Rachel = turtle.Turtle()
Chandler = turtle.Turtle()
Monica = turtle.Turtle()
Phoebe = turtle.Turtle()

Ross.shape("turtle")
Rachel.shape("turtle")
Chandler.shape("turtle")
Monica.shape("turtle")
Phoebe.shape("turtle")

Monica.fillcolor("light blue")
Monica.begin_fill()
Monica.forward(800)
Monica.backward(1800)
Monica.left(90)
Monica.forward(800)
Monica.right(90)
Monica.forward(1800)
Monica.right(90)
Monica.forward(800)
Monica.end_fill()

Ross.fillcolor("green")
Ross.begin_fill()
Ross.color("green")
Ross.forward(800)
Ross.backward(1800)
Ross.right(90)
Ross.forward(800)
Ross.left(90)
Ross.forward(1800)
Ross.left(90)
Ross.forward(800)
Ross.end_fill()

Rachel.fillcolor("pink")
Rachel.begin_fill()
Rachel.color("pink")

def square(turtle,side):
    for i in range(4):
        Rachel.right(90)
        Rachel.forward(100)

Rachel.right(180)


square(turtle, 75)
Rachel.right(90)
Rachel.forward(100)
Rachel.end_fill()

Rachel.fillcolor("purple")
Rachel.begin_fill()
Rachel.right(35)
Rachel.forward(100)
Rachel.right(117)
Rachel.forward(98)
Rachel.end_fill()
