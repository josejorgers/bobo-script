from subsumed_architecture.states.base import State
from subsumed_architecture.behaviors.implementations import move_forward, avoid_crash

class MoveForward(State):
    def __init__(self, bot):
        super().__init__('move_forward', move_forward(bot), bot)

class AvoidCrash(State):
    def __init__(self, bot):
        super().__init__('avoid_crash', avoid_crash(bot), bot)