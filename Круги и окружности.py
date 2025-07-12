# Импортируем модуль
import turtle



# Настройка
turtle.shape("turtle")
turtle.color("green")
turtle.bgcolor("turquoise")
turtle.speed(0)
turtle.setup(900, 550)



# Рисуем круг и окружность
turtle.dot(100)
turtle.forward(200)
turtle.circle(100)
# Рисуем гипнотические круги
a = 5
turtle.goto(0, 0)
turtle.clear()
for _ in range(360):
    turtle.circle(a)
    a += 5
    turtle.left(5)



# Запуск основного цикла
turtle.mainloop()