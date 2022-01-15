

def look_to_the_left(bot):
    bot.movePanTo(-40, 100)

def look_to_the_left_full(bot):
    bot.movePanTo(-80, 100)

def look_to_the_right(bot):
    bot.movePanTo(40, 100)

def look_to_the_right_full(bot):
    bot.movePanTo(80, 100)

def look_straight(bot, wait=False):
    bot.movePanTo(0, 100, wait=wait)