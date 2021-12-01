"""
solve the second part
"""


class SlidingWindow:
    def __init__(self, one, two, three):
        self.sum = one + two + three


if __name__ == "__main__":
    with open("day1/puzzleinput.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    depths = list()
    for line in lines:
        depths.append(int(line.strip().rstrip()))

    larger = 0
    smaller = 0
    same = 0
    windows = list()
    for idx, item in enumerate(depths):
        if idx < 2:
            continue
        one = depths[idx-2]
        two = depths[idx-1]
        three = item
        windows.append(SlidingWindow(one, two, three))

    for idx, w in enumerate(windows):
        if idx == 0:
            continue
        if w.sum > windows[idx-1].sum:
            larger = larger + 1

    print("Increased: {}".format(larger))
