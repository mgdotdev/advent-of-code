def parse(f):
    with open(f) as f:
        data = f.read()

    cards = {}
    for line in data.splitlines():
        name, rest = line.split(":")
        _, id = name.split()
        winnings, numbers = rest.split("|")
        winnings = list(int(x) for x in winnings.strip().split())
        numbers = list(int(x) for x in numbers.strip().split())
        cards[int(id)] = {
            "winnings": winnings,
            "numbers": numbers,
            "copies": 1
        }
    return cards

def test():
    data = parse("./fixtures/test.txt")
    total = 0
    for v in data.values():
        winnings, numbers = set(v["winnings"]), set(v["numbers"])
        count = len(set.intersection(winnings, numbers))
        if count:
            total += 2**(count - 1)
    return total

def part_one():
    data = parse("./fixtures/data.txt")
    total = 0
    for v in data.values():
        winnings, numbers = set(v["winnings"]), set(v["numbers"])
        count = len(set.intersection(winnings, numbers))
        if count:
            total += 2**(count - 1)
    return total


def part_two():
    data = parse("./fixtures/data.txt")
    for k, v in data.items():
        winnings, numbers = set(v["winnings"]), set(v["numbers"])
        count = len(set.intersection(winnings, numbers))
        if count:
            for i in range(1, count+1):
                key = k+i
                coll = data.get(key)
                if coll:
                    data[key]["copies"] += v["copies"]
    return sum(v["copies"] for v in data.values())


def main():
    print(f"test: {test()}")
    print(f"one: {part_one()}")
    print(f"two: {part_two()}")


if __name__ == "__main__":
    main()
