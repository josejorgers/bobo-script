from subsumed_architecture.behaviors.base import BaseBehavior
from robobo.pan import look_straight
from robobo.vision import prepare_exclusive_color_detection, read_color_detection
from robobo.movement.simple_movements import stop

class look_for_goal(BaseBehavior):

    def __init__(self, bot, direction_func, color='RED'):
        super().__init__(bot, transition_time=0)
        self.color = color
        self.blob = None
        self.direction_func = direction_func
        self.position = None

    def termination_condition(self):
        prepare_exclusive_color_detection(self.color, self.bot)
        blob = read_color_detection(self.color, self.bot)
        print(f"Blob detection result: {blob}")
        if blob and blob.size > 0:
            stop(self.bot)
            self.position = self.bot.readPanPosition()
            look_straight(self.bot)
            self.blob = blob
            return True

        return False

    def execute(self):

        if not self.termination_condition():
            self.direction_func(self.bot)

            if not self.termination_condition():
                print("No blob detected")
                return None

        return {"blob": self.blob, "position": self.position } if self.blob else None