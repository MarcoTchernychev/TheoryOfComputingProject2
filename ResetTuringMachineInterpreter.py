import csv

TRANSITION_START = 7
START_STATE_ROW = 4
ACCEPT_STATE_ROW = 5
REJECT_STATE_ROW = 6
CURRENT_STATE_INDEX = 0
INPUT_INDEX = 1
NEXT_STATE_INDEX = 2
REPLACEMENT_CHAR_INDEX = 3
DIRECTION_INDEX = 4

class Transition:
    def __init__(self, currState, input, nextState, replacement, direction):
        self.currState = currState
        self.input = input
        self.nextState = nextState
        self.replacement = replacement
        self.direction = direction
    def __repr__(self):
        return f"Transition(currState: {self.currState}, input:{self.input}, nextState:{self.nextState}, replacement:{self.replacement}, direction:{self.direction})"

class TuringMachine:
    def __init__(self, start, accept, reject, transitions):
        self.start = start
        self.accept = accept
        self.reject = reject
        self.transitions = transitions
    def getNextState(self, currentState, inputValue):
        for transition in self.transitions:
            if transition.currState == currentState and transition.input == inputValue:
                return transition.nextState
    def getReplacementChar(self, currentState, inputValue):
        for transition in self.transitions:
            if transition.currState == currentState and transition.input == inputValue:
                return transition.replacement
    def getDirection(self, currentState, inputValue):
        for transition in self.transitions:
            if transition.currState == currentState and transition.input == inputValue:
                return transition.direction

def get_data(file):
    data = []
    with open(file, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

def populate_turing_machine(data):
    turingMachine = TuringMachine(data[START_STATE_ROW][0],data[ACCEPT_STATE_ROW][0],data[REJECT_STATE_ROW][0],[])
    for row in data[TRANSITION_START:]:
        turingMachine.transitions.append(Transition(row[CURRENT_STATE_INDEX],row[INPUT_INDEX],row[NEXT_STATE_INDEX],row[REPLACEMENT_CHAR_INDEX],row[DIRECTION_INDEX]))
    return turingMachine

#describe how each application tests the reset function

goodInput = '$aaabbb_'
badInput = '$aabbb_'
inputString = goodInput
inputStringList = list(inputString)

headIndex = 0
data = get_data("TuringMachine1.csv")
turingMachine = populate_turing_machine(data)

currentState = turingMachine.start
inputValue = inputStringList[headIndex]
counter = 0

while currentState not in (turingMachine.reject, turingMachine.accept):
    print(f"step: {counter+1:02d}   "
        f"state: {currentState:<7}   "   
        f"string: {''.join(inputStringList[:headIndex])}"
        f"\033[43m{inputValue}\033[0m"
        f"{''.join(inputStringList[headIndex+1:])}")
    
    nextState = turingMachine.getNextState(currentState, inputValue)
    replacementChar = turingMachine.getReplacementChar(currentState, inputValue)
    direction = turingMachine.getDirection(currentState, inputValue)
    
    inputStringList[headIndex] = replacementChar
    if(direction=='R'):
        headIndex+=1
    if(direction=='L'):
        headIndex=0
    inputValue = inputStringList[headIndex]
    currentState = nextState

    counter+=1

print(f"step: {counter+1:02d}   "
        f"state: {currentState:<7}   "   
        f"string: {''.join(inputStringList[:headIndex])}"
        f"\033[43m{inputValue}\033[0m"
        f"{''.join(inputStringList[headIndex+1:])}")
print(counter+1)