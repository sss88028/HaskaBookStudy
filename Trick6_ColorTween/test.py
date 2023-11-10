import turtle
import random

turtle.tracer(0, 0)

# 创建两个Turtle对象
t1 = turtle.Turtle()
t2 = turtle.Turtle()

# 设置两个圆形的属性
radius1 = 50
radius2 = 30

# 设置初始颜色
color1 = "red"
color2 = "blue"

# 绘制第一个圆形
t1.color(color1)
t1.begin_fill()
t1.circle(radius1)
t1.end_fill()

# 移到第二个圆形的位置
t2.penup()
t2.goto(radius1 + 50, 0)
t2.pendown()

# 绘制第二个圆形
t2.color(color2)
t2.begin_fill()
t2.circle(radius2)
t2.end_fill()

# 更新窗口
turtle.update()

# 修改圆形颜色
def change_colors():
    new_color1 = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    new_color2 = "#{:06x}".format(random.randint(0, 0xFFFFFF))

    t1.color(new_color1)
    t1.begin_fill()
    t1.circle(radius1)
    t1.end_fill()

    t2.color(new_color2)
    t2.begin_fill()
    t2.circle(radius2)
    t2.end_fill()

    # 更新窗口
    turtle.update()

# 修改圆形颜色
change_colors()

# 显示窗口
turtle.mainloop()