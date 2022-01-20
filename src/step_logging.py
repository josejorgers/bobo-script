
def logger(context, action, bot, *params):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            if not "logs" in context.keys():
                context["logs"] = []
            context["logs"].append({"action": action, "bot": bot, "params": params})

            return result

        return wrapper

    return decorator

def state_logger(action, *params):

    def wrapper(cls):
        class decorator(cls):
            
            def __init__(self, bot, context):
                super().__init__(bot, context)
                self.run = logger(context, action, bot, *params)(self.run)

        decorator.__name__ = cls.__name__
        return decorator

    return wrapper

def inline_log(context, action, bot, *params):
    if not "logs" in context.keys():
        context["logs"] = []
    context["logs"].append({"action": action, "bot": bot, "params": params})
    return context