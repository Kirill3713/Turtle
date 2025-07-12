# Импортируем модули
import random
import turtle



# Настройка
turtle.shape("turtle")
turtle.color("green")
turtle.bgcolor("turquoise")
turtle.speed(0)
turtle.setup(1500, 800)



# Рисуем абстракцию
for _ in range(5):


    a = random.randint(5, 200)
    for _ in range(4):
        turtle.forward(a)
        turtle.right(90)


    b = random.randint(100, 250)
    turtle.forward(b)
    c = random.randint(5, 260)
    turtle.right((c))

    x = random.randint(-700, 700)
    y = random.randint(-400, 400)
    turtle.begin_fill()
    turtle.goto(x + 100, y + 100)
    turtle.goto(x + 100, y - 100)
    turtle.goto(x, y)
    turtle.goto(x - 100, y - 100)
    turtle.goto(x - 100, y + 100)
    turtle.goto(x, y)
    turtle.goto(x + 100, y + 100)
    turtle.end_fill()


    b = random.randint(100, 250)
    turtle.forward(b)
    c = random.randint(5, 260)
    turtle.right((c))

    d = 0
    for _ in range(60):
        turtle.left(1)
        turtle.forward(0.1)
        if d % 10 == 0:
            turtle.left(90)
            turtle.forward(10)
            turtle.right(180)
            turtle.forward(10)


        d += 1


    b = random.randint(100, 250)
    turtle.forward(b)
    c = random.randint(5, 260)
    turtle.right((c))

    e = random.randint(5, 150)
    turtle.circle(e)


    b = random.randint(100, 250)
    turtle.forward(b)
    c = random.randint(5, 260)
    turtle.right((c))

    e = random.randint(5, 150)
    turtle.dot(e)

    b = random.randint(100, 250)
    turtle.forward(b)
    c = random.randint(5, 260)
    turtle.right((c))

    for _ in range(4):
        for _ in range(6):
            turtle.forward(70)
            turtle.left(60)
        turtle.right(90)


    b = random.randint(100, 250)
    turtle.forward(b)
    c = random.randint(5, 260)
    turtle.right((c))

    for _ in range(6):
            turtle.forward(70)
            turtle.left(60)



# Запуск основного цикла
turtle.mainloop()