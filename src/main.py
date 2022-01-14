from robobopy.Robobo import Robobo
from constants.connections import LOCAL
from subsumed_architecture.states.implementations import MoveForward
from subsumed_architecture.augmented_fsm import AugmentedFSM

robot = Robobo(LOCAL)
robot.connect()

initial_state = MoveForward(robot)

state_machine = AugmentedFSM([initial_state])

state_machine.run()