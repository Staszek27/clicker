from datetime import datetime
start_time = datetime.now()

RANDOMIZE_MOVES = False


def reset_time():
    global start_time
    start_time = datetime.now()


def time_elapsed_in_micro():
    delta = (datetime.now() - start_time)
    return delta.microseconds + 10 ** 6 * delta.seconds


def time_elapsed_in_seconds():
    return time_elapsed_in_micro() / 10 ** 6