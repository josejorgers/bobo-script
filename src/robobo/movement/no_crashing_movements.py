from robobopy.utils.LED import LED
from robobopy.utils.Color import Color

from robobo.movement.simple_movements import diagonal_movement, move_backward, move_forward, turn_left, turn_right
from robobo.emotions import danger_appears
from utils.movements import is_far_from_edge, is_obstacle_close, is_obstacle_far, is_obstacle_medium

def without_crashing(fn):

    def wrapper(robot, *args, **kwargs):
        robot.setLedColorTo(LED.All, Color.OFF)

        fn(robot, *args, **kwargs)

        if 'time' in kwargs.keys():
            return

        while is_obstacle_far(robot) and is_far_from_edge(robot): 
            robot.wait(0.01)

        robot.setLedColorTo(LED.All, Color.GREEN)

        while is_obstacle_medium(robot) and is_far_from_edge(robot): 
            robot.wait(0.01)
        
        robot.setLedColorTo(LED.All, Color.MAGENTA)

        while is_obstacle_close(robot) and is_far_from_edge(robot): 
            robot.wait(0.01)

        robot.stopMotors()
        robot.setLedColorTo(LED.All, Color.RED)

        danger_appears(robot)


    return wrapper


@without_crashing
def no_crash_move_forward(robot, speed, time=None):
    move_forward(robot, speed, time)

@without_crashing
def no_crash_turn_right(robot, speed, time=None):
    turn_right(robot, speed, time)

@without_crashing
def no_crash_turn_left(robot, speed, time=None):
    turn_left(robot, speed, time)

@without_crashing
def no_crash_move_backward(robot, speed, time=None):
    move_backward(robot, speed, time)

@without_crashing
def no_crash_diagonal_movement(robot, speed_left, speed_right, time=None):
    diagonal_movement(robot, speed_left, speed_right, time)