class BaseBehavior:

    def __init__(self, bot):
        self.bot = bot

    def execute(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        self.execute(*args, **kwargs)