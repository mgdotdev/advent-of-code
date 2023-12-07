def parse(f):
    with open(f) as f:
        data = f.read()

    _iter = iter(data.splitlines())

    meta = {}

    seeds = next(_iter)
    _, seeds = seeds.split(":")
    meta["seed"] = list(int(x) for x in seeds.strip().split())
    maps = {}

    assert not next(_iter)

    name = None
    items = {}
    for line in _iter:
        if not line:
            source, _, dest = name.split("-")
            coll = {
                "next": dest,
                "items": items
            }
            maps[source] = coll
            name = None
            items = {}
            continue
        if not name:
            name, _ = line.split()
        else:
            dest_cat, source_cat, length = line.split()
            items[int(source_cat)] = {
                "destination": int(dest_cat),
                "length": int(length)
            }

    return meta, maps


def invert(maps):
    res = {}

    for k, v in maps.items():
        new = {}
        new["next"] = k
        items = {}
        new["items"] = items
        res[v["next"]] = new
        for src, data in v["items"].items():
            items[data["destination"]] = {
                "destination": src,
                "length": data["length"]
            }
    return res

def find_key(keys, val) -> int:
    if len(keys) == 0:
        return val

    if val >= keys[-1]:
        return keys[-1]

    if val < keys[0]:
        return keys[0]

    left = 0
    right = len(keys) - 1

    while True:
        assert right >= left >= 0
        mid = (right + left) // 2
        lval = keys[mid]
        rval = keys[mid+1]

        if val < lval:
            right = mid - 1
        elif val > rval:
            left = mid + 1
        elif val == rval:
            return rval
        else:
            return lval


def find(key, val, maps, match):
    while True:
        m = maps[key]
        tgt = find_key(sorted(m["items"].keys()), val)
        tm = m["items"][tgt]

        if val in range(tgt, tgt+tm["length"]):
            diff = tm["destination"] - tgt
            val += diff
        key = m["next"]
        if key == match:
            return val


def test():
    meta, maps = parse("./fixtures/test.txt")
    key, val = meta.popitem()

    k = key
    location = float("inf")
    for v in val:
        v = find(k, v, maps, "location")
        if v < location:
            location = v
        k = key
    return location


def part_one():
    meta, maps = parse("./fixtures/data.txt")
    key, val = meta.popitem()

    k = key
    location = float("inf")
    for v in val:
        v = find(k, v, maps, "location")
        if v < location:
            location = v
        k = key

    return location


def part_two():
    meta, maps = parse("./fixtures/data.txt")
    imaps = invert(maps)

    _, ranges = meta.popitem()

    _iter = iter(ranges)
    ranges = {k: next(_iter) for k in _iter}

    start = 0
    while True:
        v = find("location", start, imaps, "seed")
        tgt = find_key(sorted(ranges.keys()), v)
        if v in range(tgt, tgt + ranges[tgt]):
            return find("seed", v, maps, "location")
        start += 1


def main():
    print(f"test: {test()}")
    print(f"one: {part_one()}")
    print(f"two: {part_two()}")


if __name__ == "__main__":
    main()

