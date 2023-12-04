MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

NUMBERS = {v: v for v in MAPPING.values()}

REVERSED = {k[::-1]: v for k, v in MAPPING.items()}


def graph(mapping):
    letter_map = {}
    for key, val in mapping.items():
        if not key:
            return val
        first, rest = key[0], key[1:]
        letter_map.setdefault(first, {})[rest] = val

    return {
        k: graph(v)
        for k, v in letter_map.items()
    }


def traverse(line, graph, progress=""):
    if not line:
        return ""

    key, rest = line[0], line[1:]
    node = graph.get(key)

    if node is None:
        if progress:
            return ""
        return traverse(rest, graph)
    elif type(node) is str:
        return node

    result = traverse(rest, node, progress=progress+key)
    if not result:
        return traverse(rest, graph, progress=progress)

    return result


def part_one():
    g = graph(NUMBERS)

    val = 0
    with open("./fixtures/data.txt") as f:
        data = f.read()
    for line in data.splitlines():
        first = traverse(line, g)
        last = traverse(line[::-1], g)
        val += int(first+last)
    return val


def part_two():
    forward = graph({**MAPPING, **NUMBERS})
    backward = graph({**REVERSED, **NUMBERS})

    val = 0
    with open("./fixtures/data.txt") as f:
        data = f.read()
    for line in data.splitlines():
        first = traverse(line, forward)
        last = traverse(line[::-1], backward)
        val += int(first+last)
    return val


def test():
    forward = graph({**MAPPING, **NUMBERS})
    backward = graph({**REVERSED, **NUMBERS})
    val = 0

    with open("./fixtures/test.txt") as f:
        data = f.read()

    for line in data.splitlines():
        first = traverse(line, forward)
        last = traverse(line[::-1], backward)
        val += int(first+last)
    return val


def main():
    print(f"test: {test()}")
    print(f"part_one: {part_one()}")
    print(f"part_two: {part_two()}")


if __name__ == "__main__":
    main()

