def main():

    import turtle               # allows us to use the turtles library
    wn = turtle.Screen()        # creates a graphics window
    michael = turtle.Turtle()
    michael.color("purple")
    michael.speed(0)
    
    sides = 0

    michael.up()
    michael.left(180)
    michael.forward(350)
    michael.right(90)
    michael.forward(150)
    michael.down()

    # M
    michael.forward(200)
    michael.right(160)
    michael.forward(200)
    michael.left(140)
    michael.forward(200)
    michael.right(160)
    michael.forward(200)

    michael.left(90)
    michael.forward(20)

    # i
    michael.left(90)
    michael.forward(100)
    michael.up()
    michael.forward(15)
    michael.down()
    michael.pensize(10)
    michael.forward(10)
    michael.up()
    michael.right(90)
    michael.forward(20)

    # c
    michael.right(90)
    michael.forward(25)
    michael.left(90)
    michael.forward(50)
    michael.down()
    michael.pensize(1)
    michael.left(180)
    for i in range(0,10):
        michael.forward(17)
        michael.left(20)

    michael.right(20)
    michael.up()
    michael.forward(20)

    # h
    michael.right(90)
    michael.forward(5)
    michael.left(180)
    michael.down()
    michael.forward(200)
    michael.left(180)
    michael.forward(105)
    michael.left(90)
    for i in range(0,7):
        michael.forward(5)
    for i in range(0,7):
        michael.right(13)
        michael.forward(10)
    michael.left(2)
    michael.forward(47)
        
    michael.up()
    michael.left(90)
    michael.forward(65)
    michael.down()
    michael.left(180)
    michael.left(180)

    # a
    michael.up()
    for i in range(0,16):
        michael.forward(3)
        michael.left(3.5)
    michael.down()
    michael.left(178)
    for i in range(0,16):
        michael.forward(3)
        michael.right(3.5)
    for i in range(0,60):
        michael.forward(3)
        michael.right(3.5)
    michael.right(45)
    michael.forward(95)

    michael.up()
    michael.left(77)
    michael.left(90)
    michael.forward(40)
    michael.right(90)

    # e
    michael.right(15) 
    michael.up()
    michael.forward(10)
    michael.left(90)
    michael.forward(10)
    michael.down()
    michael.right(75)
    michael.forward(95)
    michael.left(90)
    for i in range(32):
        michael.forward(8)
        michael.left(10)
        
    michael.up()
    michael.right(15)
    michael.forward(40)
    michael.left(54)
    michael.left(180)
    michael.forward(25)
    michael.left(180)
    michael.down()
    
    # l
    michael.forward(200)
    michael.up()
    michael.left(180)
    michael.forward(200)
    michael.down()
    michael.forward(15)
    michael.up()
    michael.forward(160)
    michael.right(90)
    michael.forward(450)
    michael.down()
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # L
    michael.right(90)
    michael.forward(200)
    michael.left(180)
    michael.forward(200)
    michael.left(90)
    michael.forward(120)

    # y
    michael.left(120)
    michael.forward(90)
    michael.right(180)
    michael.forward(90)
    michael.left(180)
    michael.right(60)
    michael.forward(90)
    michael.right(180)
    michael.forward(200)

    michael.up()
    michael.left(180)
    michael.forward(110)
    michael.right(60)
    michael.forward(45)
    michael.left(90)
    michael.forward(6)
    michael.right(90)
    michael.forward(30)
    michael.down()

    # o
    michael.circle(35)

    michael.up()
    michael.forward(47)
    michael.left(89)
    michael.down()

    # n
    michael.forward(70)

    michael.right(180)
    michael.forward(5)
    michael.left(110)

    for i in range(6):
        michael.forward(9)
        michael.right(10)
    for i in range(10):
        michael.right(5)
        michael.forward(1)
    michael.forward(51)

    michael.up()
    michael.forward(50)
    michael.right(90)
    michael.forward(480)
    michael.right(89)
    michael.down()
    michael.right(90)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # G
    michael.forward(120)
    michael.left(180)
    michael.forward(120)
    michael.left(90)
    michael.forward(200)
    michael.left(90)
    michael.forward(120)
    michael.up()
    michael.left(90)
    michael.forward(100)
    michael.left(90)
    michael.forward(40)
    michael.left(180)
    michael.down()
    michael.forward(80)
    michael.right(90)
    michael.forward(100)

    michael.left(90)
    michael.up()
    michael.forward(65)
    michael.down()
    
    # a
    michael.up()
    for i in range(16):
        michael.forward(3)
        michael.left(3.5)
    michael.down()
    michael.left(178)
    for i in range(0,16):
        michael.forward(3)
        michael.right(3.5)
    for i in range(0,60):
        michael.forward(3)
        michael.right(3.5)
    michael.right(45)
    michael.forward(95)

    michael.up()
    michael.left(77)
    michael.forward(15)
    michael.left(90)
    michael.down()

    # r
    michael.forward(100)
    michael.right(90)
    for i in range(50):
        michael.forward(1.5)
        michael.right(1.5)

    michael.up()
    michael.forward(65)
    michael.left(76)
    michael.forward(50)
    michael.left(89)

    # d
    michael.forward(215)
    michael.left(180)
    michael.down()
    michael.forward(215)
    michael.right(90)
    for i in range(53):
        michael.forward(3.2)
        michael.right(3.5)

    michael.up()
    michael.forward(25)
    michael.right(84)
    michael.forward(105)
    michael.left(180)
    michael.down()

    # i
    michael.forward(100)
    michael.up()
    michael.forward(15)
    michael.down()
    michael.pensize(10)
    michael.forward(10)
    michael.up()
    michael.pensize(1)
    michael.right(90)
    
    michael.forward(20)
    michael.right(90)
    michael.forward(125)
    michael.right(180)
    michael.down()

    # n
    michael.forward(100)
    michael.right(180)
    michael.forward(5)
    michael.left(110)

    for i in range(6):
        michael.forward(9)
        michael.right(10)
    for i in range(10):
        michael.right(5)
        michael.forward(1)
    michael.forward(82)

    michael.up()
    michael.left(90)
    michael.forward(10)
    michael.left(90)
    michael.forward(40)
    michael.right(90)
    michael.down()

    # e
    michael.right(15) 
    michael.up()
    michael.forward(5)
    michael.left(90)
    michael.forward(10)
    michael.down()
    michael.right(75)
    michael.forward(95)
    michael.left(90)
    for i in range(38):
        michael.forward(6.7)
        michael.left(8)

    michael.up()
    michael.right(33)
    michael.forward(45)
    michael.right(91)
    michael.forward(7)
    michael.left(180)
    michael.down()
    
    # r
    michael.forward(95)
    michael.right(90)
    for i in range(50):
        michael.forward(1.5)
        michael.right(1.5)

    michael.up()
    michael.forward(65)
    michael.left(76)
    michael.forward(50)
    michael.left(89)

    michael.color("blue")
    # underline
    michael.left(180)
    michael.forward(45)
    michael.right(90.5)
    michael.down()
    michael.pensize(15)
    michael.forward(840)

    michael.up()
    michael.forward(2)
    michael.down()

    # leftline
    michael.right(90)
    michael.pensize(10)
    michael.forward(700)

    # topline
    michael.right(90)
    michael.forward(845)
    
    #rightline
    michael.right(90)
    michael.forward(702)

    michael.ht()
    wn.exitonclick()
    
main()
