import sys
sys.path.insert(0, './src/')

from robobo.movement import no_crashing_movements, simple_movements
from robobopy.Robobo import Robobo
from constants.connections import LOCAL

robot = Robobo(LOCAL)
robot.connect()

simple_movements.turn_left(robot, 20, time=1)
simple_movements.move_forward(robot, 20, time=2)
simple_movements.turn_right(robot, 20, time=1)

no_crashing_movements.no_crash_move_forward(robot, 20)

no_crashing_movements.no_crash_turn_right(robot, 20, time=1)

no_crashing_movements.no_crash_move_forward(robot, 10)

no_crashing_movements.no_crash_turn_left(robot, 20, time=1)

no_crashing_movements.no_crash_move_forward(robot, 10)

no_crashing_movements.no_crash_turn_right(robot, 20, time=1)

no_crashing_movements.no_crash_move_forward(robot, 10)

simple_movements.stop(robot)