from subsumed_architecture.states.implementations import MoveForward, AvoidCrash, LookForGoalLeft, \
                                                            LookForGoalLeftFull, LookForGoalRight, LookForGoalRightFull,\
                                                                LocateGoal, MoveToGoal, Stop
from utils.movements import is_obstacle_close

TRANSITIONS = {
    MoveForward: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context=None: True: LookForGoalLeft
    },
    AvoidCrash: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context=None: True: MoveForward
    },
    LookForGoalLeft: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context: context != None: LocateGoal,
        lambda bot, context=None: True: LookForGoalLeftFull
    },

    LookForGoalLeftFull: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context: context != None: LocateGoal,
        lambda bot, context=None: True: LookForGoalRight
    },

    LookForGoalRight: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context: context != None: LocateGoal,
        lambda bot, context=None: True: LookForGoalRightFull
    },

    LookForGoalRightFull: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context: context != None: LocateGoal,
        lambda bot, context=None: True: MoveForward
    },

    LocateGoal: {
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context: context != None: MoveToGoal,
        lambda bot, context=None: True: MoveForward
    },

    MoveToGoal: {
        lambda bot, context: is_obstacle_close(bot) and context["blob"].size > 800: Stop,
        lambda bot, context=None: is_obstacle_close(bot): AvoidCrash,
        lambda bot, context: context != None : MoveToGoal,
        lambda bot, context=None: True: MoveForward
    }
}