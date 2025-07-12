# Импортируем модуль
import turtle
# Настройка
turtle.shape("turtle")
turtle.color("green")
turtle.bgcolor("turquoise")
turtle.speed(7)
# Перемещение по координатам
turtle.begin_fill()
#            x    y
turtle.goto(100, 100)
turtle.goto(100, -100)
turtle.goto(0, 0)
turtle.goto(-100, -100)
turtle.goto(-100, 100)
turtle.goto(0, 0)
turtle.hideturtle()
turtle.end_fill()
# Запуск основного цикла
turtle.mainloop()