from pynput.mouse import Listener
from global_lib import *


# consts
FILENAME = 'testing.csv'

# global
data = []


# code 
def save_data():
    open(FILENAME, 'w').write('\n'.join(
        ['x;y;info;time in microseconds'] + data)
    )


def save_info(x, y, info):
    data.append('{};{};{};{}'.format(
        x, y, info, time_elapsed_in_micro()
    ))
    return max(x, y) >= 10


def on_move(x, y):
    return save_info(x, y, "move")


def on_click(x, y, button, pressed):
    if not pressed:
        return True
    return save_info(x, y, "click-{}".format(str(button).split('.')[1]))


def on_scroll(x, y, dx, dy):
    return save_info(x, y, "scroll")



# Collect events until released
with Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
save_data()

