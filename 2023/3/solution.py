import itertools


def grid():
    with open("./fixtures/data.txt") as f:
        data = f.read()
    return [
        list(line) for line in data.splitlines()
    ]


def char_is_symbol(char):
    if char == ".":
        return False

    if not char.isdigit():
        return True
    return False


def part_one():
    g = grid()

    numbers = []
    for x, line in enumerate(g):
        _iter = enumerate(iter(line))
        for y, char in _iter:
            if char.isdigit():
                start = (x, y)
                while True:
                    try:
                        y, char = next(_iter)
                        if not char.isdigit():
                            stop = (x, y)
                            numbers.append([start, stop])
                            break
                    except StopIteration:
                        break


    s = 0
    for num in numbers:
        (x1, y1), (x2, y2) = num

        box = []

        xi = x1 if x1 == 0 else x1-1
        yi = y1 if y1 == 0 else y1-1

        xf = x2 if x2 == len(g) else x2+1
        yf = y2 if y2 == len(g[0]) else y2+1

        row = []

        x=xi
        y=yi
        while True:
            try:
                val = g[x][y]
                row.append(val)
            except IndexError:
                __import__('pdb').set_trace()
                pass

            y += 1
            if y == yf:
                box.append(row)
                row = []
                if x == xf:
                    break
                x += 1
                y = yi

        rep="\n".join("".join(b) for b in box)
        if any(char_is_symbol(i) for i in itertools.chain.from_iterable(box)):
            val = "".join(g[x1][y1:y2])
            s += int(val)
            print(f"TRUE: \n{rep}\n")
            print(s, val)
            print("\n\n")
        else:
            print(f"FALSE: \n{rep}\n")
            print(s, 0)
            print("\n\n")

        __import__('pdb').set_trace()

    return s


def main():
    print(f"one: {part_one()}")

if __name__ == "__main__":
    main()
