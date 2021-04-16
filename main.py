from machine.memory import Memory
from assembler.assembler import Assembler

if __name__ == '__main__':
    a = Memory()
    a.hello(3)
    b = Assembler()
    b.readFile()
    print(b.given_instructions)
    print(b.assemble())
