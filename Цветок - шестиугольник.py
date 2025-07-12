# Импортируем модуль
import turtle



# Настройка
turtle.shape("turtle")
turtle.color("green")
turtle.bgcolor("turquoise")
turtle.speed(5)
turtle.setup(900, 550)



# Рисуем цветок
for _ in range(4):
    for __ in range(6):
        turtle.forward(70)
        turtle.left(60)
    turtle.right(90)



# Запуск основного цикла
turtle.mainloop()