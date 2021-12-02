from dataclasses import dataclass


@dataclass
class Submarine:
    horizontal: int
    depth: int

    def forward(self, amount: int = 1):
        self.horizontal += amount

    def down(self, amount: int = 1):
        self.depth += amount

    def up(self, amount: int = 1):
        self.depth -= amount

    @property
    def magnitude(self) -> int:
        return self.horizontal * self.depth


@dataclass
class Submarine2:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0

    def forward(self, amount: int = 1):
        self.horizontal += amount
        self.depth += self.aim*amount

    def down(self, amount: int = 1):
        self.aim += amount

    def up(self, amount: int = 1):
        self.aim -= amount

    @property
    def magnitude(self) -> int:
        return self.horizontal * self.depth


def performInstruction(instruction: str, amount: str, sub: Submarine):
    int_amount = int(amount)
    if instruction == "forward":
        sub.forward(int_amount)
    elif instruction == "down":
        sub.down(int_amount)
    elif instruction == "up":
        sub.up(int_amount)
    else:
        print("what the fuck?", instruction, amount)
        pass
