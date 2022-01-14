from subsumed_architecture.states.implementations import MoveForward, AvoidCrash
from utils.movements import is_obstacle_close

TRANSITIONS = {
    MoveForward: {
        lambda bot: is_obstacle_close(bot): AvoidCrash,
        lambda bot: True: MoveForward
    },
    AvoidCrash: {
        lambda bot: is_obstacle_close(bot): AvoidCrash,
        lambda bot: True: MoveForward
    }
}