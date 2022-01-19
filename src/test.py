from robobo.movement.simple_movements import turn_left
from constants.motion_config import TURN_90_DEGREES
from constants.connections import LOCAL
from robobopy.Robobo import Robobo

robot = Robobo(LOCAL)
robot.connect()


turn_left(robot, TURN_90_DEGREES[0], TURN_90_DEGREES[1])