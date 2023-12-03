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


class Node:
    def __init__(self, mapping, key=None):
        self.key = key
        self.val = ""
        letter_map = {}
        for key, val in mapping.items():
            if key == "":
                self.val = val
            else:
                first, rest = key[0], key[1:]
                letter_map.setdefault(first, {})[rest] = val

        if not self.val:
            self.items = {
                k: Node(v, k) for k, v in letter_map.items()
            }

    def traverse(self, val):
        if self.val:
            return self.val

        if not val:
            return ""

        key, rest = val[0], val[1:]
        node = self.items.get(key)

        if node is None:
            if self.key:
                return ""
            return self.traverse(rest)

        traverse = node.traverse(rest)

        if not traverse:
            return self.traverse(rest)

        return traverse


def part_one():
    graph = Node(NUMBERS)

    val = 0
    with open("./fixtures/data.txt") as f:
        data = f.read()
    for line in data.splitlines():
        first = graph.traverse(line)
        last = graph.traverse(line[::-1])
        val += int(first+last)
    return val


def part_two():
    first_graph = Node({**MAPPING, **NUMBERS})
    last_graph = Node({**REVERSED, **NUMBERS})

    val = 0
    with open("./fixtures/data.txt") as f:
        data = f.read()
    for line in data.splitlines():
        first = first_graph.traverse(line)
        last = last_graph.traverse(line[::-1])
        val += int(first+last)
    return val


def test():
    first_graph = Node({**MAPPING, **NUMBERS})
    last_graph = Node({**REVERSED, **NUMBERS})
    val = 0

    with open("./fixtures/test.txt") as f:
        data = f.read()

    for line in data.splitlines():
        first = first_graph.traverse(line)
        last = last_graph.traverse(line[::-1])
        val += int(first+last)
    return val


def main():
    print(f"test: {test()}")
    print(f"part_one: {part_one()}")
    print(f"part_two: {part_two()}")


if __name__ == "__main__":
    main()

