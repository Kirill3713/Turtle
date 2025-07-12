# Импортируем модули
import random
import turtle



# Настройка
turtle.shape("turtle")
turtle.color("green")
turtle.bgcolor("turquoise")
turtle.speed(7)

# Выполняем задание

for _ in range(3):
    turtle.goto(random.randint(-300, 300), random.randint(-300, 300))



# Запуск основного цикла
turtle.mainloop()