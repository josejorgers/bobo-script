from time import time
from subsumed_architecture.behaviors.base import BaseBehavior
from robobo.movement.simple_movements import turn_left, turn_right, diagonal_movement, move_forward
from robobo.vision import prepare_exclusive_color_detection, read_color_detection
from robobo.pan import adjust_tilt

class locate_goal(BaseBehavior):

    def __init__(self, bot, blob, direction, transition_time=0):
        super().__init__(bot)
        self.transition_time = transition_time
        self.color = blob.color
        self.position = direction

    def execute(self):
        self.bot.stopMotors()

        if self.position < -40:
            turn_left(self.bot, 20, 1)
        elif self.position < -10:
            turn_left(self.bot, 15, 1.5)
        elif self.position > 10 and self.position <= 40:
            turn_right(self.bot, 15, 1.5)
        elif self.position > 40:
            turn_right(self.bot, 20, 1)

        prepare_exclusive_color_detection(self.color.upper(), self.bot)

        blob = read_color_detection(self.color, self.bot)

        return {"blob": blob, "position": 0}

class move_to_goal(BaseBehavior):

    def __init__(self, bot, blob):
        super().__init__(bot, transition_time=0.1)
        self.color = blob.color
        self.position = blob.posx
        self.vertical_position = blob.posy
        self.size = blob.size

    def execute(self):

        print(f"Currently target has size {self.size}")
        
        differential = 50 - self.position
        
        if self.vertical_position > 30:
            curr_tilt_position = self.bot.readTiltPosition()
            adjust_tilt(self.bot, curr_tilt_position + 10)

        if abs(differential) < 10:
            print(f"Goal is straight ahead!: x={self.position}")
            move_forward(self.bot, 10)
        
        else:
            
            print(f"Moving to goal located at: x={self.position}")
            if differential < 0:
                turn_left(self.bot, 3, time=0.5)
            else:
                turn_right(self.bot, 3, time=0.5)

        prepare_exclusive_color_detection(self.color.upper(), self.bot)

        blob = read_color_detection(self.color, self.bot)
        print(f"New blob detection: size={blob.size}, posx={blob.posx}, posy={blob.posy}")

        if blob == None or blob.size == 0 or blob.posx == 0:
            return None

        return {"blob": blob, "position": 0}


    