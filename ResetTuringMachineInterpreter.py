import csv
import os

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
    def getNextStateReplacementCharDirection(self, currentState, inputValue):
        for transition in self.transitions:
            if transition.currState == currentState and transition.input == inputValue:
                return {'next state': transition.nextState, 'replacement char': transition.replacement, 'direction': transition.direction}
        return False

def get_data(file):
    if not os.path.exists(file):
        raise FileNotFoundError(f"CSV file not found: '{file}'")
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

def ask_for_file():
    while True:
        filename = input("Enter the CSV file name: ").strip()
        if os.path.exists(filename):
            return filename
        print(f"File '{filename}' does not exist. Try again.\n")

def ask_for_string():
    while True:
        string = input("Enter a string starting with $ and ending with _: ").strip()
        if string[0]=='$' and string[-1]=='_':
            return string
        print(f"String must start with '$' and end with '_'\n")


file = ask_for_file()
data = get_data(file)

inputString = ask_for_string()
inputStringList = list(inputString)

turingMachine = populate_turing_machine(data)

headIndex = 0
currentState = turingMachine.start
inputValue = inputStringList[headIndex]
counter = 0

while currentState not in (turingMachine.reject, turingMachine.accept):
    print(f"step: {counter+1:02d}   "
            f"state: {currentState:<7}   "   
            f"string: {''.join(inputStringList[:headIndex])}"
            f"\033[43m{inputValue}\033[0m"
            f"{''.join(inputStringList[headIndex+1:])}")
    
    transitionResult = turingMachine.getNextStateReplacementCharDirection(currentState, inputValue)
    if(transitionResult==False):
        print("invalid string")
        exit(0)

    nextState, replacementChar, direction = transitionResult['next state'], transitionResult['replacement char'], transitionResult['direction']

    inputStringList[headIndex] = replacementChar
    if(direction=='R'):
        if headIndex == len(inputStringList) - 1:
            inputStringList.append('_')
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