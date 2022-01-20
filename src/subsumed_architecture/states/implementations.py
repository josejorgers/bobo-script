from subsumed_architecture.states.base import State, ContextChangerState
from subsumed_architecture.behaviors.uninformed_movement import move_forward, avoid_crash, stop_motors
from subsumed_architecture.behaviors.goal_detection import look_for_goal
from subsumed_architecture.behaviors.informed_movement import locate_goal, move_to_goal
from robobo.pan import look_to_the_left, look_to_the_left_full, look_to_the_right, look_to_the_right_full, look_straight
from step_logging import state_logger
from robobo.movement import simple_movements 

@state_logger(simple_movements.move_forward, 10)
class MoveForward(State):
    def __init__(self, bot, context):
        super().__init__('move_forward', move_forward(bot), bot, context)
        
class AvoidCrash(State):
    def __init__(self, bot, context=None):
        super().__init__('avoid_crash', avoid_crash(bot, context), bot, context)    

@state_logger(simple_movements.move_forward, 10)
class LookForGoalStraight(ContextChangerState):
    def __init__(self, bot, context=None):
        super().__init__('look_for_goal_straight', look_for_goal(bot, look_straight), bot, context)

@state_logger(simple_movements.move_forward, 10, .7)
class LookForGoalLeft(ContextChangerState):
    def __init__(self, bot, context=None):
        super().__init__('look_for_goal_left', look_for_goal(bot, look_to_the_left), bot, context)

@state_logger(simple_movements.move_forward, 10, .7)
class LookForGoalLeftFull(ContextChangerState):
    def __init__(self, bot, context=None):
        super().__init__('look_for_goal_full_left', look_for_goal(bot, look_to_the_left_full), bot, context)

@state_logger(simple_movements.move_forward, 10, 1.4)
class LookForGoalLeftReturn(LookForGoalLeft):
    def __init__(self, bot, context=None):
        super().__init__(bot, context)

@state_logger(simple_movements.move_forward, 10, .7)
class LookForGoalRight(ContextChangerState):
    def __init__(self, bot, context=None):
        super().__init__('look_for_goal_right', look_for_goal(bot, look_to_the_right), bot, context)

@state_logger(simple_movements.move_forward, 10, .7)
class LookForGoalRightFull(ContextChangerState):
    def __init__(self, bot, context=None):
        super().__init__('look_for_goal_full_right', look_for_goal(bot, look_to_the_right_full), bot, context)

@state_logger(simple_movements.move_forward, 10, .7)
class LookForGoalRightReturn(LookForGoalRight):
    def __init__(self, bot, context=None):
        super().__init__(bot, context)

class LocateGoal(State):
    def __init__(self, bot, context):
        super().__init__('locate_goal', locate_goal(bot, context['blob'], context['position'], context), bot, context=context)

class MoveToGoal(ContextChangerState):
    def __init__(self, bot, context):
        super().__init__('move_to_goal', move_to_goal(bot, context['blob'], context), bot, context=context)

class Stop(State):
    def __init__(self, bot, context=None):
        super().__init__('stop', stop_motors(bot), bot, context=context, is_final=True)