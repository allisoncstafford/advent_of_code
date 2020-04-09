def parse_relationship(string):
    """Parses relationship from string of format A)B where A is the parent and
    B is the child.

    Args:
        original string

    Returns:
        Parent, Child: string, string
    """
    parsed = string.strip().split(')')
    return parsed[0], parsed[1]


def get_input_str(filename):
    """returns list of inputs from data file.

    Args:
        filename: the name of the file with the input data.

    Returns:
        a list of strings read from the file
    """
    text_file = open(filename, "r")
    input_strs = text_file.readlines()
    text_file.close()
    return input_strs


class Planet:
    """A planet - linked list -  with name, parent, children, and count of the
    number of planets it orbits (that come between it and the base planet)
    """
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.count = None
        self.children = []

    def set_count(self):
        if self.parent != None:
            self.count = self.parent.count +1
        else:
            self.count = 0

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)


def build_tree(instructions):
    """builds a tree based on the instructions passed. Instructions expected to
    be a list of strings in the form parent)child.
    """
    first_name, _ = parse_relationship(instructions[0])
    first_planet = Planet(name=first_name, parent=None)
    planets = [first_planet]

    for instruction in instructions:
        parent_name, child_name = parse_relationship(instruction)

        # initialize next_planet and parent
        next_planet = None
        parent = None

        # search for existing planet or parent
        for planet in planets:
            if planet.name == parent_name:
                parent = planet
            elif planet.name == child_name:
                next_planet = planet
        
        # if no existing planet or parent, make them, and add to planet list
        if parent == None:
            parent = Planet(name=parent_name)
            planets.append(parent)
        if next_planet == None:
            next_planet = Planet(name=child_name)
            planets.append(next_planet)

        # add parent to the next planet
        next_planet.set_parent(parent)

        # add next planet to parent's children
        parent.add_child(next_planet)

    return planets


def set_orbit_counts(planets):
    """sets the orbit counts by finding base planet and traversing the tree,
    setting the counts from root to leaf.
    """
    base_planet = None

    # find base planet
    for planet in planets:
        if planet.parent == None:
            base_planet = planet
            break
    
    # traverse tree setting count
    base_planet.set_count()
    planet = base_planet
    s = []
    s.append(planet)
    while len(s) > 0:
        planet = s.pop()
        planet.set_count()
        if planet.children != None:
            for child in planet.children:
                s.append(child)


def count_orbits(planets):
    """counts(sums) the number of orbits from all planets
    """
    set_orbit_counts(planets)
    count = 0
    for planet in planets:
        count += planet.count
    return count


def main():
    lines = get_input_str('day6_input.txt')
    planets = build_tree(lines)
    print(count_orbits(planets))

def t(lines):
    """test build_tree and count_orbits without reading text file
    """
    planets = build_tree(lines)
    return count_orbits(planets)

if __name__ == "__main__":
    main()