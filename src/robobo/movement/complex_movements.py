from robobopy.utils.LED import LED
from robobopy.utils.Color import Color
from robobopy.utils.IR import IR

from constants.sesors_config import DISTANCE_CLOSE, DISTANCE_MEDIUM, DISTANCE_FAR
from robobo.movement.simple_movements import diagonal_movement, move_backward, move_forward, turn_left, turn_right

def without_crashing(fn):

    def wrapper(robot, *args, **kwargs):
        robot.setLedColorTo(LED.All, Color.OFF)

        fn(robot, *args, **kwargs)

        while robot.readIRSensor(IR.FrontC) < DISTANCE_FAR and\
                robot.readIRSensor(IR.FrontRR) < DISTANCE_FAR and\
                    robot.readIRSensor(IR.FrontLL) < DISTANCE_FAR: 
            robot.wait(0.01)

        robot.setLedColorTo(LED.All, Color.GREEN)

        while robot.readIRSensor(IR.FrontC) < DISTANCE_MEDIUM and\
            robot.readIRSensor(IR.FrontRR) < DISTANCE_MEDIUM and\
            robot.readIRSensor(IR.FrontLL) < DISTANCE_MEDIUM: 
            
            robot.wait(0.01)
        
        robot.setLedColorTo(LED.All, Color.MAGENTA)

        while robot.readIRSensor(IR.FrontC) < DISTANCE_CLOSE and\
            robot.readIRSensor(IR.FrontRR) < DISTANCE_CLOSE and\
            robot.readIRSensor(IR.FrontLL) < DISTANCE_CLOSE: 
            
            robot.wait(0.01)

        robot.stopMotors()
        robot.setLedColorTo(LED.All, Color.RED)

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