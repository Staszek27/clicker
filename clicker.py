from global_lib import *
import pyautogui
import time

pyautogui.PAUSE = 0

def handle_query(csv_line, step):
    try:
        x, y, info, t = csv_line.split(';')
    except ValueError:
        return False
    
    x, y, t = [float(e) for e in [x, y, t]]
    x, y, t = [int(e) for e in [x, y, t]]


    info_handler = {
        'move':        lambda x, y : pyautogui.moveTo(x, y),
        'click-left':  lambda x, y : pyautogui.leftClick(x, y),
        'click-right': lambda x, y : pyautogui.rightClick(x, y),
        'scroll':      lambda x, y : pyautogui.scroll(2, x, y) # TODO
    }

    left = lambda : t - time_elapsed_in_micro()
    sleep_time = max(0, left() / 10 ** 6)
    print('[query]: {} [sleep time]: {:.7f}'.format(
            info + ' ' * (15 - len(info)),
            sleep_time
        ), 
        end = ' | ', flush=True
    )

    time.sleep(sleep_time)
    print('step {}:\t accuracy: {:.2f}%'.format(
        step, 
        abs(left() / time_elapsed_in_micro()) * 100
    ))

    info_handler[info](x, y)
    return True