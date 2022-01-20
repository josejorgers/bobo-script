from subsumed_architecture.states.implementations import MoveForward, AvoidCrash, LookForGoalLeft, \
                                                            LookForGoalLeftFull, LookForGoalRight, LookForGoalRightFull,\
                                                                LocateGoal, MoveToGoal, Stop, LookForGoalStraight, \
                                                                    LookForGoalLeftReturn, LookForGoalRightReturn
from utils.movements import is_obstacle_close, is_goal_close, is_goal_close_to_camera, is_goal_far_to_camera

TRANSITIONS = {
    MoveForward.__name__: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context=None: True: LookForGoalStraight
    },
    AvoidCrash.__name__: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context=None: True: MoveForward
    },
    LookForGoalStraight.__name__: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context: not 'blob' in context.keys() or context['blob'] != None: LocateGoal,
        lambda bot, context=None: True: LookForGoalLeft
    },
    LookForGoalLeft.__name__: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context: not 'blob' in context.keys() or context['blob'] != None: LocateGoal,
        lambda bot, context=None: True: LookForGoalLeftFull
    },

    LookForGoalLeftFull.__name__: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context: not 'blob' in context.keys() or context['blob'] != None: LocateGoal,
        lambda bot, context=None: True: LookForGoalLeftReturn
    },

    LookForGoalLeftReturn.__name__: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context: not 'blob' in context.keys() or context['blob'] != None: LocateGoal,
        lambda bot, context=None: True: LookForGoalRight
    },

    LookForGoalRight.__name__: {
        lambda bot, context: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context: not 'blob' in context.keys() or context['blob'] != None: LocateGoal,
        lambda bot, context: True: LookForGoalRightFull
    },

    LookForGoalRightFull.__name__: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context: not 'blob' in context.keys() or context['blob'] != None: LocateGoal,
        lambda bot, context=None: True: LookForGoalRightReturn
    },

    LookForGoalRightReturn.__name__: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context: not 'blob' in context.keys() or context['blob'] != None: LocateGoal,
        lambda bot, context=None: True: MoveForward
    },

    LocateGoal.__name__: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context: not 'blob' in context.keys() or context['blob'] != None: MoveToGoal,
        lambda bot, context=None: True: MoveForward
    },

    MoveToGoal.__name__: {
        lambda bot, context: is_goal_close(bot) and is_goal_close_to_camera(context['blob']): Stop,
        lambda bot, context=None: not 'blob' in context.keys() or context['blob']  == None: MoveForward,
        lambda bot, context=None: is_obstacle_close(bot) and is_goal_far_to_camera(context['blob']): AvoidCrash,
        lambda bot, context: context['blob'] != None : MoveToGoal,
    }
}