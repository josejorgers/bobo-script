from subsumed_architecture.states.base import State
from subsumed_architecture.transitions import TRANSITIONS


class FSM:

    def __init__(self, subsumed_states: set, initial_state: State):
        self.subsumed_states = subsumed_states
        self.current_state = initial_state

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
            self.current_state.run()
            print("Beginning transition")
            self.make_transition()
            self.current_state.bot.wait(0.5)

    def make_transition(self):
        for t, transitions in TRANSITIONS.items():
            if isinstance(self.current_state, t):
                print(f"Entering to transitions for {t}")
                for condition, transition in transitions.items():
                    print(f"Evaluating whether to transit to {transition}")
                    print(f"Result of evaluation: {condition(self.current_state.bot)}")
                    if condition(self.current_state.bot):
                        print("Condition met! Transitioning to {}".format(transition))
                        self.current_state = transition(self.current_state.bot)
                        return

class AugmentedFSM:
    def __init__(self, initial_states: list):
        self.subsumed_states = set()
        self.initial_states = initial_states
    
    def run(self):
        for state in self.initial_states:
            fsm = FSM(self.subsumed_states, state)
            fsm.run()
