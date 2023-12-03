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


def find_first_num(items, strings=()):
    for index, item in enumerate(items):
        try:
            int(item)
            return item
        except ValueError:
            for string in strings:
                if not string.startswith(item):
                    continue
                if items[index:index+len(string)] == string:
                    return (
                        MAPPING.get(string, "")
                        or MAPPING.get(string[::-1], "")
                    )
    raise ValueError


def part_one():
    val = 0
    with open("./fixtures/data.txt") as f:
        data = f.read()
    for line in data.splitlines():
            first = find_first_num(line)
            last = find_first_num(line[::-1])
            val += int(first+last)
    return val


def part_two():
    val = 0
    with open("./fixtures/data.txt") as f:
        data = f.read()
    for line in data.splitlines():
        first = find_first_num(line, MAPPING.keys())
        last = find_first_num(line[::-1], (s[::-1] for s in MAPPING.keys()))
        val += int(first+last)
    return val


def test():
    val = 0
    with open("./fixtures/test.txt") as f:
        data = f.read()
    for line in data.splitlines():
        first = find_first_num(line, MAPPING.keys())
        last = find_first_num(line[::-1], (s[::-1] for s in MAPPING.keys()))
        join = first+last
        val += int(join)
    return val


def main():
    print(f"test: {test()}")
    print(f"part_one: {part_one()}")
    print(f"part_two: {part_two()}")


if __name__ == "__main__":
    main()
