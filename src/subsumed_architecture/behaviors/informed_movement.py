from subsumed_architecture.behaviors.base import BaseBehavior
from robobo.movement.simple_movements import turn_left, turn_right, stop, move_forward
from robobo.vision import prepare_exclusive_color_detection, read_color_detection
from robobo.pan import adjust_tilt
from constants.motion_config import TURN_90_DEGREES, TURN_45_DEGREES, SLIGHT_TURN
class locate_goal(BaseBehavior):

    def __init__(self, bot, blob, direction, transition_time=0):
        super().__init__(bot)
        self.transition_time = transition_time
        self.color = blob.color
        self.position = direction

    def execute(self):

        stop(self.bot)

        full_speed, full_time = TURN_90_DEGREES
        mid_speed, mid_time = TURN_45_DEGREES

        print(f"Moving to {self.color} goal detected at {self.position}")
        if self.position < -40:
            turn_left(self.bot, full_speed, full_time)
        elif self.position >= -40 and self.position < 0:
            turn_left(self.bot, mid_speed, mid_time)
        elif self.position < 10:
            pass
        elif self.position <= 40:
            turn_right(self.bot, mid_speed, mid_time)
        elif self.position > 40:
            turn_right(self.bot, full_speed, full_time)

        prepare_exclusive_color_detection(self.color.upper(), self.bot)

        blob = read_color_detection(self.color, self.bot)

        if blob != None and blob.size != 0 and blob.posx != 0:
            return {"blob": blob, "position": 0}

        return None

class move_to_goal(BaseBehavior):

    def __init__(self, bot, blob):
        super().__init__(bot, transition_time=0.1)
        self.color = blob.color
        self.position = blob.posx
        self.vertical_position = blob.posy
        self.size = blob.size

    def execute(self):

        print(f"Currently target has size {self.size}")
        
        if self.size == 0:
            return None
        
        differential = 50 - self.position
        center = 10 if self.size > 300 else 40
        
        if abs(differential) < center:
            print(f"Goal is straight ahead!: x={self.position}")
            move_forward(self.bot, 10)
        
        else:
            turn_speed, turn_time = SLIGHT_TURN

            print(f"Moving to goal located at: x={self.position}")
            if differential > 0:
                turn_left(self.bot, turn_speed, turn_time)
            else:
                turn_right(self.bot, turn_speed, turn_time)

        if self.vertical_position < 30:
            curr_tilt_position = self.bot.readTiltPosition()
            adjust_tilt(self.bot, curr_tilt_position + 10)

        prepare_exclusive_color_detection(self.color.upper(), self.bot)

        blob = read_color_detection(self.color, self.bot)
        print(f"New blob detection: size={blob.size}, posx={blob.posx}, posy={blob.posy}")

        if blob == None or blob.size == 0 or blob.posx == 0:
            return None

        return {"blob": blob, "position": 0}


    