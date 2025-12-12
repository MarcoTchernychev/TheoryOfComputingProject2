Run ResetTuringMachineInterpreter.py and follow the prompts

a^n_b^n.csv checks to see whether the machine can correctly count and match equal numbers of symbols on the tape
    
    L = {a^n,b^n, n>0}

Even_a.csv checks to see if the TM should be able to reset, then walk back to where it left off, and continue the computation correctly
    
    L = {a string of all a's that is even in length}

Even_b_in_a.csv triggers two consecutive resets as part of processing each b to ensure back-to-back resets are handled.
    
    L = {string of a's and b's with even b's}

First_Equals_Last.csv checks to see if the machine can remember (in its finite control) the last symbol it saw while scanning to the right, then reset to the left end and use that remembered value to branch/compare at the start
    
    L = {string of a's and b's where the string starts and ends with the same char}

Starts_a_Contains_bb.csv checks whether the machine can remember the first symbol it read, scan the tape for a substring, and use a reset to return to the left end and re-check / confirm the remembered information before halting.
    
    L = {string of a's and b's that starts with a and contains bb}

