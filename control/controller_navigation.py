from collections import deque

from control import controller_traffic


def path_from_to(start, stop):
    # BFS
    to_check = deque()
    to_check.append((controller_traffic.splits[start], [], [start]))  # current node, turns, nodes
    seen = set()

    while len(to_check) > 0:
        options, turns, nodes = to_check.popleft()

        if stop in options:
            turns.append(options.index(stop))
            nodes.append(stop)
            return turns, nodes

        for i in range(len(options)):
            if not controller_traffic.splits[options[i]] in seen:
                to_check.append((controller_traffic.splits[options[i]], turns + [i], nodes + [options[i]]))
                seen.add(controller_traffic.splits[options[i]])

    return -1


class Navigation:
    def __init__(self):
        self.current_dest = 'parkirisce'  # where we want to go

    def get_split_direction(self, current_split):
        if current_split == self.current_dest:
            self.current_dest = None
            return 0
        return path_from_to(current_split, self.current_dest)[0][0]

