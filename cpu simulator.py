import random

class CPU:
    def __init__(self):
        self.registers = [0] * 32  # 32 general-purpose registers
        self.pc = 0  # Program Counter
        for i in range(len(self.registers)): # intialize random values
            value = random.randint(0,100)
            self.registers[i] = value

    def execute(self, instruction):
        opcode = instruction[0]

        if opcode == "ADD":
            rd, rs, rt = map(int, instruction[1:])
            self.registers[rd] = self.registers[rs] + self.registers[rt]
            print(f'\nAdding values from register {rs} and {rt}. Storing result in register {rd}')
        elif opcode == "SUB":
            rd, rs, rt = map(int, instruction[1:])
            self.registers[rd] = self.registers[rs] - self.registers[rt]
            print(f'\nSubtracting values from register {rs} and {rt}. Storing result in register {rd}')
        elif opcode == "HLT":
            print("\nHalt the CPU")
            return False  # Halt the CPU
        self.pc += 1  # Increment Program Counter
        return True

    # variation instructions to cpu
    #def run(self, instructions):
    #    while self.pc < len(instructions):
    #        instruction = instructions[self.pc]
    #        result = self.execute(instruction)
    #        if not result:
    #            break

    # variation instructions to memory_bus to cpu
    def run(self, memory_bus):
        for i in range(len(memory_bus.memory)):
            instruction = memory_bus.memory[i]
            result = self.execute(instruction)
            if not result:
                break

class MemoryBus:
    def __init__(self):
        self.memory = [0] * 1024  # 1024 memory locations

    def read(self, address):
        return self.memory[address]

    def write(self, address, data):
        if address > len(self.memory):
            print("Memory full")
            return False
        self.memory[address] = data


def parse_instruction(line):
    return line.strip().split()

def load_instructions(filename):
    with open(filename, "r") as file:
        instructions = [parse_instruction(line) for line in file]
    return instructions


def main():
    cpu = CPU()
    memory_bus = MemoryBus()

    # Print inital CPU register values
    print("\nInitial CPU register values:")
    for i, value in enumerate(cpu.registers):
        print(f"Register R{i}: {value}")

    # Load instructions from file
    instructions = load_instructions("instructions.txt")

    # Set memory bus values
    for i in range(len(instructions)):
        memory_bus.write(i, instructions[i])

    # Send instructions and initial memory bus values to CPU and Memory Bus
    cpu.run(memory_bus)

    # Print final CPU register values
    print("\nFinal CPU register values:")
    for i, value in enumerate(cpu.registers):
        print(f"Register R{i}: {value}")


if __name__ == "__main__":
    main()