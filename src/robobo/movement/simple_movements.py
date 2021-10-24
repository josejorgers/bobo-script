def move_forward(robot, speed, time=None):
    if time is None:
        robot.moveWheels(speed, speed)
    else:
        robot.moveWheelsByTime(speed, speed, time)

def turn_right(robot, speed, time=None):
    if time is None:
        robot.moveWheels(-speed, speed)
    else:
        robot.moveWheelsByTime(-speed, speed, time)

def turn_left(robot, speed, time=None):
    if time is None:
        robot.moveWheels(speed, -speed)
    else:
        robot.moveWheelsByTime(speed, -speed, time)

def move_backward(robot, speed, time=None):
    if time is None:
        robot.moveWheels(-speed, -speed)
    else:
        robot.moveWheelsByTime(-speed, -speed, time)

def diagonal_movement(robot, speed_left, speed_right, time=None):
    if time is None:
        robot.moveWheels(speed_left, speed_right)
    else:
        robot.moveWheelsByTime(speed_left, speed_right, time)

def stop(robot):
    robot.stopMotors()