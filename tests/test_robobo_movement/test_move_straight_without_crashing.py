import sys
sys.path.insert(0, './src/')

from robobo.movement import complex_movements, simple_movements
from robobopy.Robobo import Robobo
from constants.connections import LOCAL

robot = Robobo(LOCAL)
robot.connect()

complex_movements.no_crash_move_forward(robot, 30)

simple_movements.stop(robot)