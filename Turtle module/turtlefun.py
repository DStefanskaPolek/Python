import turtle
import math

# creating turtle object named Franklin
franklin = turtle.Turtle()
print(franklin)


# t - turtle
# length - distance to move
# moving turtle without leaving a mark
def move_t(t, length):
    t.pu()
    t.fd(length)
    t.pd()


# t - turtle
# r - length of triangle's arm
# t_a - triangle's angle
# printing an arm of length r and rotating the turtle by the internal angle
def print_arm(t, r, t_a):
    t.fd(r)
    t.lt(180.0 - t_a)


# t - turtle
# t_b - length of triangle's base
# t_a - triangle's angle
# printing a base of length t_b and rotating the turtle by the internal angle
def print_base(t, t_b, t_a):
    t.fd(t_b)
    t.lt(180.0 - t_a)


# t - turtle
# r - length of triangle's arm
# t_a - triangle's angle
# t_b - length of triangle's base
# printing an arm, a base and an arm again,
# then rotating the turtle by the internal angle to prepare for next triangle
def print_triangle(t, r, t_a, t_b):
    print_arm(t, r, t_a)
    print_base(t, t_b, t_a)
    print_arm(t, r, t_a)
    t.lt(t_a)


# t - turtle
# n - number of "slices of pie"
# r - length of triangle's arm
# calculating all the triangles' angles:
#  - internal_angle is vertex angle,
#  - triangle_angle is base angle,
# calculating triangles' bases,
# rotating turtle by the half of the vertex angle so the shapes would be symmetrical,
# printing a pie with n slices (triangles)
# rotating turtle again to the middle, to print another shape
def print_pie(t, n, r):
    internal_angle = 360.0 / n
    triangle_angle = (180.0 - internal_angle) / 2
    triangle_base = 2 * ((math.sin(math.radians(internal_angle / 2))) * r)
    t.lt(internal_angle / 2)
    for i in range(n):
        print_triangle(t, r, triangle_angle, triangle_base)
    t.rt(internal_angle / 2)


# moving turtle far to the left to print first pie of 3 slices with 40 pixels arms
move_t(franklin, -400)
print_pie(franklin, 3, 40)

# moving turtle and printing second pie of 4 slices with 60 pixels arms
move_t(franklin, 100)
print_pie(franklin, 4, 60)

# moving turtle and printing third pie of 6 slices with 80 pixels arms
move_t(franklin, 150)
print_pie(franklin, 6, 80)

# moving turtle and printing fourth pie of 8 slices with 100 pixels arms
move_t(franklin, 200)
print_pie(franklin, 8, 100)

# moving turtle and printing fifth pie of 20 slices with 120 pixels arms
move_t(franklin, 250)
print_pie(franklin, 20, 120)

franklin.hideturtle()
turtle.mainloop()
