def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_on_right():
        while wall_on_right():
            if front_is_clear():
                move()
            else:
                turn_left()
    else:
        num = 0
        while not wall_on_right():
            turn_right()
            move()
            num += 1
            if num > 5 and front_is_clear():
                while front_is_clear():
                    move()