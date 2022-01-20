from robobo.movement.simple_movements import *
from constants.motion_config import TURN_90_DEGREES

def return_to_start(bot, logs):

    speed, time = TURN_90_DEGREES

    turn_right(bot, speed, time)
    turn_right(bot, speed, time)

    for i in range(len(logs)-1, -1, -1):
        log = logs[i]
        action, params = log["action"], log["params"]
        print(f"Position: {i}, action: {action}, params: {params}")

        action(bot, *params)
        bot.wait(1)