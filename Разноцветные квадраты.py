# Импортируем модуль
import turtle



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
a = ""

y = 0
x = 0
colors = []
while a != "exit":
    a = input("Введите цвет: ")
    colors.append(a)
    
del colors[-1]
for c in colors:
    turtle.color(c)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    for _ in range(4):
        turtle.forward(50)
        turtle.right(90)    
    x += 70
    y += 70



print(colors)
# Запуск основного цикла
turtle.mainloop()