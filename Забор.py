# Импортируем модуль
import turtle



# Настройка
turtle.shape("turtle")
turtle.color("green")
turtle.bgcolor("turquoise")
turtle.speed(0)



# Рисуем забор
turtle.left(180)
turtle.forward(250)
turtle.right(180)
x = 0
for _ in range(5):

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(45)
    turtle.right(90)
    turtle.forward(45)
    turtle.right(45)
    turtle.forward(100)
    turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(50)



# Рисуем цветок
for _ in range(90):
    turtle.left(1)
    turtle.forward(0.1)
    if x % 10 == 0:
        turtle.left(90)
        turtle.forward(10)
        turtle.right(180)
        turtle.forward(10)


    x += 1
turtle.right(180)
turtle.forward(50)



turtle.right(90)
turtle.forward(330)
turtle.left(180)



# Запуск основного цикла
turtle.mainloop()