##### auto-clicker for MAC OS

## Overview

A program to record and repeat moves of your mouse. Also creates a report of recording based on main modules -- $pynput$ and $pyautogui$

When you're recording:
1. Launch recording.py. 
2. Make moves with your mouse. WARNING! Don't use your scroll button!
3. Go with your mouse to left-up corner of your screen. Then the program will automatically stop (or just force your program to stop).
4. The report successfully will be created in $FILENAME$ csv-file.

When you're repeating moves.
1. Be sure testing.csv was generated before by you. WARNING! Be sure the scroll action isn't in that, it could stop your program automatically.
2. Set flag $RANDOMIZE_MOVES$ in global_lib.py. Depeneds on this flag, the moves from the report will be a little be seem to be randomized or not.
3. Launch DataAgent.py. 
4. Use scroll (on your mouse) to stop a program. That's why you can't insert this operation in recording report. It's just demo version of a final program.

It also provides mode, where you are able to randomize a little bit moves of your mouse (it only randomize moves query, not a single clicks). 

## Preparation

Firstly you need to give input acces for your python and terminal in "Input Monitoring" setting (see screen below).

[](https://imgur.com/a/6yzWwns)

Secondary you need to create proper enviroment. Use

```pip install -r requirements.txt``` 


