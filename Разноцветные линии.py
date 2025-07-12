# Импортируем модуль
import turtle
import random



# Настройка
turtle.shape("turtle")
turtle.color("green")
turtle.bgcolor("turquoise")
turtle.speed(0)
turtle.setup(900, 550)



# Выполняем задание
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
colors = ['green', 'blue', 'light blue', 'light green', 'turquoise', 'indigo', 'azure', 'gray', 'lime', 'aqua', 'purple', 'dark green', 'navy blue', 'yellow', 'red' ]
a = random.choice(colors)
y = 0
for _ in range(15):
    turtle.color(a)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(0, y)
    turtle.pendown()
    a = random.choice(colors)
    y -= 10




# Запуск основного цикла
turtle.mainloop()