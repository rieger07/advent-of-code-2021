from collections import defaultdict
EXAMPLE="""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

class GammaRate:
    def __init__(self, input_obj:list[defaultdict[int]]) -> None:
        self.bytestr = ""
        #self._input_obj = input_obj
        for bit in input_obj:
            self._getMostCommonBit(bit)
        self.rate = int(self.bytestr, 2)

    def _getMostCommonBit(self, bit:defaultdict[int]):
        if bit["0"] > bit["1"]:
            self.bytestr += "0"
        else:
            self.bytestr += "1"

class EpsilonRate:
    def __init__(self, input_obj:list[defaultdict[int]]) -> None:
        self.bytestr = ""
        #self._input_obj = input_obj
        for bit in input_obj:
            self._getLeastCommonBit(bit)
        self.rate = int(self.bytestr, 2)

    def _getLeastCommonBit(self, bit:defaultdict[int]):
        if bit["0"] < bit["1"]:
            self.bytestr += "0"
        else:
            self.bytestr += "1"

class BitString:
    def __init__(self, inputstr) -> None:
        self.str = inputstr

def part1():
    #input_list = EXAMPLE.splitlines()
    with open("day3/input.txt", "r", encoding="utf-8") as f:
        input_list = list()
        for line in f.readlines():
            input_list.append(line.strip().rstrip())
    

    width = len(input_list[0])
    bits = list()
    for b in range(width):
        bits.append(defaultdict(int))
    for line in input_list:
        for idx,bit in enumerate(line):
            bits[idx][bit] += 1
    g = GammaRate(bits)
    e = EpsilonRate(bits)
    print(g.rate * e.rate)

def getOxygenRating(input_list):
    width = len(input_list[0])
    bits = list()
    for b in range(width):
        bits.append(defaultdict(int))
    candidates = input_list
    for bit_idx in range(width):
        for candidate_idx, bitstr in enumerate(candidates):
            char = bitstr[bit_idx]
            bits[bit_idx][char] += 1
        thisbit = bits[bit_idx]
        if thisbit["0"] > thisbit["1"]:
            bittokeep = "0"
        else:
            bittokeep = "1"
        temp = candidates
        candidates = list()
        for candidate in temp:
            if candidate[bit_idx] == bittokeep:
                candidates.append(candidate)
        if len(candidates) == 1:
            return candidates[0]
    return None
    

def getCO2ScrubberRating(input_list):
    width = len(input_list[0])
    bits = list()
    for b in range(width):
        bits.append(defaultdict(int))
    candidates = input_list
    for bit_idx in range(width):
        for candidate_idx, bitstr in enumerate(candidates):
            char = bitstr[bit_idx]
            bits[bit_idx][char] += 1
        thisbit = bits[bit_idx]
        if thisbit["1"] < thisbit["0"]:
            bittokeep = "1"
        else:
            bittokeep = "0"
        temp = candidates
        candidates = list()
        for candidate in temp:
            if candidate[bit_idx] == bittokeep:
                candidates.append(candidate)
        if len(candidates) == 1:
            return candidates[0]
        
    return None

def part2():
    #input_list = EXAMPLE.splitlines()
    with open("day3/input.txt", "r", encoding="utf-8") as f:
        input_list = list()
        for line in f.readlines():
            input_list.append(line.strip().rstrip())
    oxygen = getOxygenRating(input_list)
    co2 = getCO2ScrubberRating(input_list)
    print(oxygen, int(oxygen, 2))
    print(co2, int(co2, 2))
    print(int(oxygen, 2) * int(co2, 2))
    
    #g = GammaRate(bits)
    #e = EpsilonRate(bits)
    #print(g.rate * e.rate)

def main():
    part2()


if __name__ == "__main__":
    main()