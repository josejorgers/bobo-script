class State:

    def __init__(self, name, behavior, bot, context=None, is_final=False):
        self.name = name
        self.is_subsumed = False
        self.behavior = behavior
        self.bot = bot
        self.context = context
        self.is_final = is_final

    def run(self):
        aux = self.behavior()
        self.context = aux if aux != None else self.context
        return self.context

class ContextChangerState(State):

    def __init__(self, name, behavior, bot, context, is_final=False):
        super().__init__(name, behavior, bot, context, is_final)

    def run(self):
        return self.behavior()