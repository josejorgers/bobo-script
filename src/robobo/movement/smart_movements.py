from robobopy.utils.IR import IR
from robobo.movement.simple_movements import turn_right, turn_left
from step_logging import inline_log

def distance_based_turn(robot, speed=30, time=0.5, context=None):
    left_distance = robot.readIRSensor(IR.FrontLL)
    right_distance = robot.readIRSensor(IR.FrontRR)

    if left_distance > right_distance:
        inline_log(context, turn_left, robot, speed, time)
        robot.moveWheelsByTime(-speed, speed, time)
        return
    
    inline_log(context, turn_right, robot, speed, time)
    robot.moveWheelsByTime(speed, -speed, time)
    