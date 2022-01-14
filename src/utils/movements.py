from robobo.movement.simple_movements import *
from constants.sensors_config import DISTANCE_CLOSE, DISTANCE_MEDIUM, DISTANCE_FAR, EDGE_DISTANCE
from robobopy.utils.IR import IR

DIRECTIONS = {
    'forward': move_forward,
    'right': turn_right,
    'left': turn_left,
    'backward': move_backward,
    'custom': diagonal_movement
}

def is_obstacle_far(robot):
    return robot.readIRSensor(IR.FrontC) < DISTANCE_FAR and\
                robot.readIRSensor(IR.FrontRR) < DISTANCE_FAR and\
                    robot.readIRSensor(IR.FrontLL) < DISTANCE_FAR

def is_obstacle_medium(robot):
    return robot.readIRSensor(IR.FrontC) < DISTANCE_MEDIUM and\
            robot.readIRSensor(IR.FrontRR) < DISTANCE_MEDIUM and\
            robot.readIRSensor(IR.FrontLL) < DISTANCE_MEDIUM

def is_obstacle_close(robot):
    return robot.readIRSensor(IR.FrontC) > DISTANCE_CLOSE or\
            robot.readIRSensor(IR.FrontRR) > DISTANCE_CLOSE or\
            robot.readIRSensor(IR.FrontLL) > DISTANCE_CLOSE

def is_far_from_edge(robot):
    return robot.readIRSensor(IR.FrontL) > EDGE_DISTANCE or\
            robot.readIRSensor(IR.FrontR) > EDGE_DISTANCE or\
            robot.readIRSensor(IR.BackL) > EDGE_DISTANCE or\
            robot.readIRSensor(IR.BackR) > EDGE_DISTANCE