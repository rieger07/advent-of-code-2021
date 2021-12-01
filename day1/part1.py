"""
Intended to work the problem of day 1. part 1
"""

if __name__ == "__main__":
    with open("day1/puzzleinput.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    depths = list()
    for line in lines:
        depths.append(int(line.strip().rstrip()))

    larger = 0
    smaller = 0
    same = 0
    for idx, item in enumerate(depths):
        if idx == 0:
            print("{} (N/A - no previous measurement)".format(item))
            continue
        previous = depths[idx-1]
        if item > previous:
            larger = larger + 1
            #print("{} (increased)".format(item))
        elif item == previous:
            same = same +1
            #print("{} (same)".format(item))
        else:
            smaller = smaller +1
            #print("{} (decreased)".format(item))

    print("Increased: {}".format(larger))
    print("Decreased: {}".format(smaller))
    print("Same: {}".format(same))
