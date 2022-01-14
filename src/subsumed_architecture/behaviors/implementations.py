from subsumed_architecture.behaviors.base import BaseBehavior
from robobo.movement import smart_movements, simple_movements

class move_forward(BaseBehavior):
    def __init__(self, bot, speed=10, transition_time=0.5):
        super().__init__(bot)
        self.speed = speed
        self.transition_time = transition_time
    
    def execute(self):
        simple_movements.move_forward(self.bot, self.speed)
        self.bot.wait(self.transition_time)

class avoid_crash(BaseBehavior):
    def __init__(self, bot, transition_time=0):
        super().__init__(bot)
        self.speed = 20
        self.transition_time = transition_time
    
    def execute(self): # if random_movement == 0:
        smart_movements.distance_based_turn(self.bot)
        self.bot.wait(self.transition_time)