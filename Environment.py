import copy
from random import randint


class Environment:
    Map = [[]]
    initial = [[]]

    name = None
    generation = 0

    totalUniverses = 0

    def __init__(self, map_x, map_y, name, time_machine):
        self.Map = [[Node(x, y) for y in range(map_y)] for x in range(map_x)]

        if time_machine:
            machine_x = randint(0, self.Map.__len__() - 1)
            machine_y = randint(0, self.Map[0].__len__() - 1)
            self.Map[machine_x][machine_y] = TimeComputerNode(machine_x, machine_y)
            self.set_state(machine_x, machine_y, True)

        self.initial = copy.deepcopy(self.Map)
        self.name = name
        print("[3]Beginning simulation number", Environment.totalUniverses)
        print("Current deepest simulation: ", name)
        # print ("Beginning", Environment.totalUniverses, "th universe")
        Environment.totalUniverses += 1

    def update_initial(self):
        self.initial = copy.deepcopy(self.Map)

    def step(self):
        print("[2]Processing generation", self.generation)
        print("SMNEXT")
        for row in self.Map:
            for node in row:
                node.precalculate(self)

        for row in self.Map:
            for node in row:
                node.update()

        self.generation += 1

    def print_map(self):
        for y in range(self.Map[0].__len__()):
            print("[1]", end='')
            for x in range(self.Map.__len__()):
                if self.get_state(x, y):

                    print(" ", end='')
                    print(self.Map[x][y].get_symbol(), end='')
                    print(" ", end='')
                else:
                    print(" . ", end='')
            print()

    def get_state(self, x_pos, y_pos):
        if x_pos < 0 or x_pos >= self.Map.__len__():
            return False

        if y_pos < 0 or y_pos >= self.Map[0].__len__():
            return False

        return self.Map[x_pos][y_pos].alive

    def set_state(self, x_pos, y_pos, alive):
        if x_pos < 0 or x_pos >= self.Map.__len__():
            return False

        if y_pos < 0 or y_pos >= self.Map[0].__len__():
            return False

        self.Map[x_pos][y_pos].alive = alive
        return True


class Node:
    alive = False

    next_generation_alive = False

    x_pos = None
    y_pos = None

    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def precalculate(self, env):
        neighbors_alive = 0

        if env.get_state(self.x_pos + 1, self.y_pos):
            neighbors_alive += 1

        if env.get_state(self.x_pos - 1, self.y_pos):
            neighbors_alive += 1

        if env.get_state(self.x_pos, self.y_pos + 1):
            neighbors_alive += 1

        if env.get_state(self.x_pos, self.y_pos - 1):
            neighbors_alive += 1

        if env.get_state(self.x_pos + 1, self.y_pos + 1):
            neighbors_alive += 1

        if env.get_state(self.x_pos + 1, self.y_pos - 1):
            neighbors_alive += 1

        if env.get_state(self.x_pos - 1, self.y_pos + 1):
            neighbors_alive += 1

        if env.get_state(self.x_pos - 1, self.y_pos - 1):
            neighbors_alive += 1

        self.next_generation_alive = False

        if self.alive and neighbors_alive < 2:
            self.next_generation_alive = False

        if self.alive and (neighbors_alive == 2 or neighbors_alive == 3):
            self.next_generation_alive = True

        if self.alive and (neighbors_alive > 3):
            self.next_generation_alive = False

        if (not self.alive) and (neighbors_alive == 3):
            self.next_generation_alive = True

    def get_symbol(self):
        if self.alive:
            return "X"
        else:
            return "."

    def update(self):
        self.alive = self.next_generation_alive


class TimeComputerNode(Node):

    def precalculate(self, env):
        neighbors_alive = 0

        if env.get_state(self.x_pos + 1, self.y_pos):
            neighbors_alive += 1

        if env.get_state(self.x_pos - 1, self.y_pos):
            neighbors_alive += 1

        if env.get_state(self.x_pos, self.y_pos + 1):
            neighbors_alive += 1

        if env.get_state(self.x_pos, self.y_pos - 1):
            neighbors_alive += 1

        if env.get_state(self.x_pos + 1, self.y_pos + 1):
            neighbors_alive += 1

        if env.get_state(self.x_pos + 1, self.y_pos - 1):
            neighbors_alive += 1

        if env.get_state(self.x_pos - 1, self.y_pos + 1):
            neighbors_alive += 1

        if env.get_state(self.x_pos - 1, self.y_pos - 1):
            neighbors_alive += 1

        if self.alive and (neighbors_alive >= 4):
            if not self.is_future_bright(self.compute_state(env.initial, env.generation + 20, ("Copy of " + env.name))):
                env.set_state(self.x_pos, self.y_pos - 1, False)
                env.set_state(self.x_pos + 1, self.y_pos - 1, False)
                env.set_state(self.x_pos - 1, self.y_pos - 1, False)
                env.set_state(self.x_pos + 1, self.y_pos, False)
                env.set_state(self.x_pos - 1, self.y_pos, False)
                env.set_state(self.x_pos, self.y_pos + 1, False)
                env.set_state(self.x_pos + 1, self.y_pos + 1, False)
                env.set_state(self.x_pos - 1, self.y_pos + 1, False)

    def compute_state(self, initial, generations, name):
        env = Environment(initial.__len__(), initial[0].__len__(), name, False)

        env.Map = copy.deepcopy(initial)
        env.initial = initial

        for gen in range(generations):
            env.step()

        return env.Map

    def is_future_bright(self, future):
        alive = 0

        for row in future:
            for node in row:
                if node.alive:
                    alive += 1

        return not (alive == 0)

    def update(self):
        return True

    def get_symbol(self):
        return "M"
