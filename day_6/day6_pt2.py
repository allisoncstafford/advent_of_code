from day6_pt1 import get_input_str, build_tree

def get_prior_chain(target_planet_name, planets):
    """creates a list of the prior planets/nodes in the tree"""
    # get planet from the name
    for planet in planets:
        if planet.name == target_planet_name:
            target_planet = planet
    
    # while traverse the tree, collecting the parents
    prior_planets = []
    current = target_planet
    while current.parent != None:
        prior_planets.append(current.parent)
        current = current.parent

    return prior_planets


def count_distance(chain1, chain2):
    counts = []
    for planet in chain1:
        if planet in chain2:
            counts.append(chain2.index(planet) + chain1.index(planet))
    return min(counts)


def main():
    lines = get_input_str('day6_input.txt')
    planets = build_tree(lines)

    # get list of "parents" for YOU and SAN
    you_chain = get_prior_chain('YOU', planets)
    santa_chain = get_prior_chain('SAN', planets)

    # count and print distance between YOU and SAN
    print(count_distance(you_chain, santa_chain))


if __name__ == "__main__":
    main()