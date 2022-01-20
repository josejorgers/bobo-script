from robobo.movement.simple_movements import turn_left, stop
from robobo.pan import adjust_tilt, look_to_the_left, look_to_the_right, look_straight, look_to_the_left_full, look_to_the_right_full
from constants.motion_config import TURN_90_DEGREES
from constants.connections import LOCAL
from robobopy.Robobo import Robobo

robot = Robobo(LOCAL)
robot.connect()

stop(robot)

# turn_left(robot, TURN_90_DEGREES[0], TURN_90_DEGREES[1])

adjust_tilt(robot)

robot.movePanTo(-80, 30)