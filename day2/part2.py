from submarine import Submarine2, performInstruction



if __name__ == "__main__":
    sub = Submarine2(0,0,0)
    with open("day2/puzzleinput.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for l in lines:
        temp = l.strip().rstrip().split()
        instruction = temp[0]
        amount = temp[1]
        performInstruction(instruction, amount, sub)
    print(f"horizontal: {sub.horizontal}")
    print(f"depth: {sub.depth}")
    print(f"magnitude: {sub.magnitude}")