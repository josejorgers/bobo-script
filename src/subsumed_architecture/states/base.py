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
        
        if not aux or not aux['blob']:
            return self.context

        for k, item in aux.items():
            self.context[k] = item
        
        return self.context

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class ContextChangerState(State):

    def __init__(self, name, behavior, bot, context, is_final=False):
        super().__init__(name, behavior, bot, context, is_final)

    def run(self):
        result = self.behavior()

        if not result:
            self.context['blob'] = None
            return self.context
        
        self.context['blob'] = result['blob']
        return self.context
        