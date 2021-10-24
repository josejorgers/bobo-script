import sys
sys.path.insert(0, './src/')

from robobo.movement import simple_movements
from robobopy.Robobo import Robobo
from constants.connections import LOCAL

robot = Robobo(LOCAL)
robot.connect()

simple_movements.move_forward(robot, 20, 4)

simple_movements.stop(robot)