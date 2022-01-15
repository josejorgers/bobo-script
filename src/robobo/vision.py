

def prepare_exclusive_color_detection(color, bot):
    if color == 'RED':
        bot.setActiveBlobs(True, False, False, False)
    elif color == 'GREEN':
        bot.setActiveBlobs(False, True, False, False)
    elif color == 'BLUE':
        bot.setActiveBlobs(False, False, True, False)
    elif color == 'CUSTOM':
        bot.setActiveBlobs(False, False, False, True)
    else:
        raise ValueError(f"Invalid color {color}. Possible options are: RED, GREEN, BLUE, CUSTOM")

def read_color_detection(color, bot):
    return bot.readAllColorBlobs()[color.lower()]