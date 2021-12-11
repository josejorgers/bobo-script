from queue import PriorityQueue

class PriorityBehavior:
    def __init__(self, priority, behavior):
        self.priority = priority
        self.behavior = behavior

    def __lt__(self, other):
        return self.priority < other.priority
    
    def __eq__(self, other):
        return self.priority == other.priority
    
    def __gt__(self, other):
        return self.priority > other.priority
    
    def __le__(self, other):
        return self.priority <= other.priority
    
    def __ge__(self, other):
        return self.priority >= other.priority
    
    def __call__(self, *args, **kwds):
        return self.behavior(*args, **kwds)


class SubsumedHandler:

    def __init__(self, behaviors, priorities):
        self.priorities = priorities
        self.queue = PriorityQueue()
        for behavior, priority in zip(behaviors, priorities):
            self.queue.put(PriorityBehavior(priority, behavior))

    def execute(self):
        auxiliar_list = []
        while not self.queue.empty():
            behavior = self.queue.get()
            behavior()
            auxiliar_list.append(behavior)
        for behavior in auxiliar_list:
            self.queue.put(behavior)
        self.execute()


    