CONSTRAINTS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def parse():
    with open("./fixtures/data.txt") as f:
        data = f.read()
    ledger = {}
    for line in data.splitlines():
        tag, _, rest = line.partition(":")
        _, id = tag.strip().split()
        games = rest.split(";")
        for g in games:
            g = g.strip()
            dice = g.split(", ")
            rolls = list(d.strip().split() for d in dice)
            rolls = {v: int(k) for k, v in rolls}
            ledger.setdefault(id, []).append(rolls)
    return ledger


def part_one():
    ledger = parse()
    res = 0
    for k, v in ledger.items():
        possible = True
        for g in v:
            for key in CONSTRAINTS.keys():
                if g.get(key, 0) > CONSTRAINTS.get(key, 0):
                    possible = False
        if possible:
            res += int(k)
    return res


def part_two():
    ledger = parse()
    s = 0
    for v in ledger.values():
        m = {}
        for key in CONSTRAINTS.keys():
            m[key] = max(i.get(key, 0) for i in v)
        r = 1
        for i in m.values():
            r *= i

        s += r
    return s

def main():
    print(f"one: {part_one()}")
    print(f"two: {part_two()}")


if __name__ == "__main__":
    main()


