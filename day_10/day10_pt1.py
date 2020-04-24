from operator import attrgetter

class Astroid():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n_detects = None

    def set_n_detects(self, astroids):
        count = 0
        blocked_slopes_right = []
        blocked_slopes_left = [] # accounting for  -/- ==> pos
        for astroid in astroids:
            # initialize bool right
            right = False

            if astroid != self:
                # check for divide by zero error
                if astroid.x - self.x == 0:
                    if astroid.y - self.y > 0:
                        slope = 'below'
                    if astroid.y - self.y < 0:
                        slope = 'above'
                else:
                    # calculate slope
                    slope = (astroid.y - self.y)/(astroid.x - self.x)

                    # check for right/left
                    if astroid.x - self.x >= 0:
                        right = True

                # if not blocked/duplicated, add slope to list of slopes and count
                if (right) and (slope not in blocked_slopes_right):
                    count += 1
                    blocked_slopes_right.append(slope)

                elif (not right) and (slope not in blocked_slopes_left):
                    count += 1
                    blocked_slopes_left.append(slope)
        self.n_detects = count


def create_astroids(input_lines):
    """creates a list of Astroids from .#...# inputs"""
    astroids = []
    for y, line in enumerate(input_lines):
        for x, char in enumerate(line):
            if char == '#':
                astroids.append(Astroid(x, y))
    return astroids


def read_lines(file):
    """reads the input from file path and returns a list of strings
    """
    text_file = open(file, "r")
    input_strs = text_file.readlines()
    text_file.close()
    return input_strs


def get_best(astroids):
    max_detects = max(astroids, key=attrgetter('n_detects')).n_detects
    best_astroids = [a for a in astroids if a.n_detects == max_detects]
    return best_astroids


def main():
    # read input
    input_lines = read_lines('day10_input.txt')

    # parse into (x,y) positions
    astroids = create_astroids(input_lines)

    # get number each can detect
    for astroid in astroids:
        astroid.set_n_detects(astroids)

    # get best (max num able to detect)
    best_astroids = get_best(astroids)

    # return number detected and location
    bests = [{'x':a.x, 'y':a.y, 'n':a.n_detects} for a in best_astroids]
    print(bests)


def best(input_lines):
    """For testing"""
    # parse into (x,y) positions
    astroids = create_astroids(input_lines)

    # get number each can detect
    for astroid in astroids:
        astroid.set_n_detects(astroids)

    # get best (max num able to detect)
    best_astroids = get_best(astroids)

    # return number detected and location
    bests = [{'x':a.x, 'y':a.y, 'n':a.n_detects} for a in best_astroids]
    return bests


if __name__ == "__main__":
    main()