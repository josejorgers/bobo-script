from subsumed_architecture.behaviors.base import BaseBehavior
from robobo.movement import smart_movements, simple_movements

class move_forward(BaseBehavior):
    def __init__(self, bot, speed=10):
        super().__init__(bot, transition_time=1)
        self.speed = speed
    
    def execute(self):
        simple_movements.move_forward(self.bot, self.speed)

class avoid_crash(BaseBehavior):
    def __init__(self, bot):
        super().__init__(bot)
        self.speed = 20
    
    def execute(self):
        simple_movements.move_backward(self.bot, 10, time=0.5)
        smart_movements.distance_based_turn(self.bot)

class stop_motors(BaseBehavior):
    def __init__(self, bot):
        super().__init__(bot)
    
    def execute(self):
        self.bot.stopMotors()