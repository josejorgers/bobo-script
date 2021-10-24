import sys
sys.path.insert(0, './src/')

from robobo.movement import complex_movements
from robobopy.Robobo import Robobo
from constants.connections import LOCAL

robot = Robobo(LOCAL)
robot.connect()

# complex_movements.no_crash_move_forward(robot, 30, 2)

complex_movements.no_crash_turn_right(robot, 30, 1)

complex_movements.no_crash_move_forward(robot, 30, 2)

# complex_movements.no_crash_turn_left(robot, 30, 1)

# complex_movements.no_crash_move_forward(robot, 30, 2)

# complex_movements.no_crash_turn_right(robot, 30, 1)

# complex_movements.no_crash_move_forward(robot, 30, 2)

# complex_movements.stop(robot)