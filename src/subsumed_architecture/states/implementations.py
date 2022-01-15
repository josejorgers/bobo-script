from subsumed_architecture.states.base import State, ContextChangerState
from subsumed_architecture.behaviors.uniformed_movement import move_forward, avoid_crash, stop_motors
from subsumed_architecture.behaviors.goal_detection import look_for_goal
from subsumed_architecture.behaviors.informed_movement import locate_goal, move_to_goal
from robobo.pan import look_to_the_left, look_to_the_left_full, look_to_the_right, look_to_the_right_full

class MoveForward(State):
    def __init__(self, bot, context=None):
        super().__init__('move_forward', move_forward(bot), bot)

class AvoidCrash(State):
    def __init__(self, bot, context=None):
        super().__init__('avoid_crash', avoid_crash(bot), bot)

class LookForGoalLeft(ContextChangerState):
    def __init__(self, bot, context=None):
        super().__init__('look_for_goal_left', look_for_goal(bot, look_to_the_left), bot, context)

class LookForGoalLeftFull(ContextChangerState):
    def __init__(self, bot, context=None):
        super().__init__('look_for_goal_full_left', look_for_goal(bot, look_to_the_left_full), bot, context)

class LookForGoalRight(ContextChangerState):
    def __init__(self, bot, context=None):
        super().__init__('look_for_goal_right', look_for_goal(bot, look_to_the_right), bot, context)

class LookForGoalRightFull(ContextChangerState):
    def __init__(self, bot, context=None):
        super().__init__('look_for_goal_full_right', look_for_goal(bot, look_to_the_right_full), bot, context)

class LocateGoal(State):
    def __init__(self, bot, context):
        super().__init__('locate_goal', locate_goal(bot, context['blob'], context['position']), bot, context=context)

class MoveToGoal(ContextChangerState):
    def __init__(self, bot, context):
        super().__init__('move_to_goal', move_to_goal(bot, context['blob']), bot, context=context)

class Stop(State):
    def __init__(self, bot, context=None):
        super().__init__('stop', stop_motors(bot), bot, is_final=True)