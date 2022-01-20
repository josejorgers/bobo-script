from robobopy.Robobo import Robobo
from constants.connections import LOCAL
from subsumed_architecture.states.implementations import MoveForward
from subsumed_architecture.augmented_fsm import AugmentedFSM
from robobo.pan import adjust_tilt

robot = Robobo(LOCAL)
robot.connect()

adjust_tilt(robot)

initial_state = MoveForward(robot, {"logs": []})

state_machine = AugmentedFSM([initial_state])

state_machine.run()