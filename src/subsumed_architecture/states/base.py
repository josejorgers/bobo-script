class State:

    def __init__(self, name, behavior, bot):
        self.name = name
        self.is_subsumed = False
        self.behavior = behavior
        self.bot = bot

    def run(self):
        self.behavior()