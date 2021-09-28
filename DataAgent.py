from clicker import *
from pynput.mouse import Listener
import threading
from random import randint
pyautogui.FAILSAFE = False

stop_flag = False

def shift_pos(pos, delta):
    return tuple([e + randint(-delta, delta) for e in pos])


def get_position(query_line):
    result = query_line.split(';')[:2]
    return [int(float(e)) for e in result]


def get_info(query_line):
    return query_line.split(';')[2]


def get_time(query_line):
    return int(query_line.split(';')[3])


def insert_position(query_line, pos):
    parts = query_line.split(';')
    parts[:2] = [str(e) for e in pos]
    return ';'.join(parts)


def insert_time(query_line, t):
    parts = query_line.split(';')
    parts[3] = str(t)
    return ';'.join(parts)


def watch_out():
    listener = Listener(on_scroll=lambda *args : exit(0))
    listener.start()
    listener.join()
    global stop_flag
    stop_flag = True


class DataAgent:
    def __init__(self, data = []):
        self.data = [e for e in data if len(e.split(';')) == 4] 
        

    def download_data(self, filename):
        self.__init__(open(filename).read().split('\n')[1:])


    def run(self):
        reset_time()
        for i, query in enumerate(self.data):
            handle_query(query, i)
            global stop_flag
            if stop_flag:
                exit(0)


    def del_moves(self, delta = 10000):
        new_data = []
        for query in self.data:
            if (
                get_info(query) != 'move' or 
                new_data == [] or
                get_info(new_data[-1]) != 'move' or
                get_time(query) - get_time(new_data[-1]) > delta
            ):
                new_data.append(query)
        print('deleted from {} to {}'.format(
            len(self.data), len(new_data)
        ))

        return DataAgent(new_data)


    def randomize_time_in_moves(self):
        new_data = []
        lower_bound_f = lambda i : (0 if i == 0 else get_time(new_data[-1]))
        upper_bound_f = lambda i : get_time(self.data[min(i, len(self.data) - 1)])
        for i, query in enumerate(self.data):
            new_data.append(insert_time(
                query, 
                randint(lower_bound_f(i), upper_bound_f(i))
                    if get_info(query) == 'move' else
                get_time(query)
            ))
        self.data = new_data


    def randomize_positions_in_moves(self, delta = 10):
        new_data = []
        for query in self.data:
            new_data.append(
                insert_position(query, shift_pos(get_position(query), delta))
                    if get_info(query) == 'move' else
                query
            )
        self.data = new_data


    def get_prepared(self):
        clone = self.del_moves()
        clone.randomize_positions_in_moves()
        clone.randomize_positions_in_moves()
        return clone



if __name__ == '__main__':
    t = threading.Thread(target=watch_out)
    t.start()

    d1 = DataAgent()
    d1.download_data('testing.csv')
    d2 = d1



    while True:
        if RANDOMIZE_MOVES:
            d2 = d2.get_prepared()
        d2.run()
        time.sleep(10)

