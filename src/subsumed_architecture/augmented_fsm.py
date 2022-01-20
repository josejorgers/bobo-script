from subsumed_architecture.states.base import State
from subsumed_architecture.transitions import TRANSITIONS


class FSM:

    def __init__(self, subsumed_states: set, initial_state: State):
        self.subsumed_states = subsumed_states
        self.current_state = initial_state
        self.context = None

    def run(self):
        print("INITIALIZING FSM")
        
        while True:
            print("==========================================================")
            print(f"Current state: {self.current_state.name}")

            if self.current_state.name in self.subsumed_states:
                print("Current state is subsumed!")
                self.make_transition()
                continue
            
            print(f"Running behavior on state {self.current_state.name}")
            self.context = self.current_state.run()
            print(f"Current context: {self.context}")
            wait_time = self.current_state.behavior.transition_time
            
            if 'logs' in self.context.keys():
                print(f"LOGS: {self.context['logs']}")
            else:
                print("NO LOGS")

            if self.current_state.is_final:
                print("Final state reached!")
                break

            print("Beginning transition")
            self.make_transition()
            self.current_state.bot.wait(wait_time)

    def make_transition(self):
        
        t = self.current_state.__class__.__name__
        transitions = TRANSITIONS[t]
        print(f"Entering to transitions for {t}")
        for condition, transition in transitions.items():
            print(f"Evaluating whether to transit to {transition}")
            evaluation = condition(self.current_state.bot, self.context)
            print(f"Result of evaluation: {evaluation}")
            if evaluation:
                print("Condition met! Transitioning to {}".format(transition))
                self.current_state = transition(self.current_state.bot, context=self.context)
                return

# class AugmentedFSM:
#     def __init__(self, initial_states: list):
#         self.subsumed_states = set()
#         self.initial_states = initial_states
    
#     def run(self):
#         for state in self.initial_states:
#             fsm = FSM(self.subsumed_states, state)
#             fsm.run()
