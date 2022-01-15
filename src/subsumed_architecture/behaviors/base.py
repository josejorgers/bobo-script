class BaseBehavior:

    def __init__(self, bot, transition_time=0.5):
        self.bot = bot
        self.transition_time = transition_time

    def execute(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return self.execute(*args, **kwargs)