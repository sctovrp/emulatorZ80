from machine.memory import Memory
from assembler.assembler import Assembler
from linker_loader.linker import Linker
from linker_loader.loader import Loader
from z80.operations import Operations

knew_instructions = {
    'LD': 1,  # grupo transferencia de datos------
    'IN': 2,
    'OUT': 3,
    'PUSH': 4,
    'POP': 5,
    'EXX': 6,
    'ADD': 7,  # grupo aritmetricas--------------
    'SUB': 8,
    'INC': 9,
    'DEC': 10,
    'CPL': 11,  # complemento a 1
    'NEG': 12,  # complemento a 2
    'AND': 13,  # grupo logicas------------------
    'OR': 14,
    'XOR': 15,
    'RLA': 16,  # rotaciones
    'RRA': 17,
    'RLCA': 18,
    'CP': 19,  # comparar
    'SET': 20,  # grupo manipulacion de bits-----
    'RESET': 21,
    'JP': 22,  # grupo de decisiones-------------- quitar
    'CALL': 23, #
    'RET': 24,
    'RST': 25,
    'HALT': 26,
    'ORG': 27,
    'END': 28
}

knew_registers = {
    'PC': 1,  # program_counter
    'SP': 2,  # stack_pointer
    'A': 3,  # general_purpose_register
    'B': 4,
    'C': 5,
    'D': 6,
    'E': 7,
    'H': 8,
    'L': 9,
    'IX': 10,  # index_register
    'IY': 11,
    'I': 12,  # interruption_register
    'R': 13,
    # 'P': 14,  # flags
    # 'S': 15,
    # 'Z': 16,
    # 'CA': 17,
    # Aca deberia ir el aux carry?
}


class Computer:
    def __init__(self):
        self.memory = Memory()
        self.assembler = Assembler(knew_instructions, knew_registers)
        self.linker = Linker()
        self.loader = Loader()
        self.Z80 = Operations()
        self.stack = []

        self.assembler.readFile()
        machine_code = self.assembler.assemble()
        mc_memory = self.linker.resolve(machine_code)
        self.loader.load(mc_memory, self.memory.get_memory())
        self.memory.show()
        self.p_size = len(machine_code) * 3

        self.registers = {}
        for reg in knew_registers.values():
            self.registers[reg] = 0

        self.ports = {}
        for i in range(1, 6):
            self.ports[i] = 0

    def execute(self):
        index = 0
        while self.memory.get(hex(index)) is not None:
            instruction = self.memory.get(hex(index))
            first_arg = self.memory.get(hex(index + 1))
            second_arg = self.memory.get(hex(index + 2))

            if instruction == 1: # LD
                self.Z80.LDR(first_arg, second_arg, self.registers)
            elif instruction == 2: # IN
                self.Z80.INR(first_arg, self.registers, self.ports)
            elif instruction == 3: # OUT
                self.Z80.OUT(first_arg, self.ports, self.registers)
            elif instruction == 4: # PUSH
                self.Z80.PUSH(self.stack, self.registers, first_arg)
            elif instruction == 5: # POP
                self.Z80.POP(self.stack, self.registers)
            elif instruction == 7: # ADD
                self.Z80.ADDR(first_arg, self.registers)
            elif instruction == 8: # SUB
                self.Z80.SUBR(first_arg, self.registers)
            elif instruction == 9: # INC
                self.Z80.INCR(first_arg, self.registers)
            elif instruction == 10: # DEC
                self.Z80.DECR(first_arg, self.registers)
            elif instruction == 11: # CPL
                self.Z80.CPL(first_arg, self.registers)
            elif instruction == 12: # NEG
                self.Z80.NEG()
                print('Missing')
            elif instruction == 13: # AND
                self.Z80.AND(first_arg, self.registers)
            elif instruction == 14: # OR
                self.Z80.OR(first_arg, self.registers)
            elif instruction == 15: # XOR
                self.Z80.XOR(first_arg, self.registers)
            elif instruction == 16: # RLA
                self.Z80.RLA()
                print('Missing')
            elif instruction == 17: # RRA
                self.Z80.RRA()
                print('Missing')
            elif instruction == 18: # RLCA
                self.Z80.RLCA()
                print('Missing')
            elif instruction == 19: # CP
                self.Z80.CP()
                print('Missing')
            elif instruction == 20: # SET
                self.Z80.SET(first_arg, self.registers, second_arg)
                print('Missing')
            elif instruction == 21: # RESET
                self.Z80.RESET(first_arg, self.registers, second_arg)
                print('Missing')
            elif instruction == 24: # RET
                self.Z80.RET()
                print('Missing')
            elif instruction == 25: # RST
                self.Z80.RST()
                print('Missing')
            elif instruction == 26: # HALT
                self.Z80.HALT()
            elif instruction == 27: # ORG
                self.Z80.ORG(first_arg, self.registers)
            elif instruction == 28: # END
                self.Z80.END()

            index += 3

        #self.memory.show()
        print(self.registers[3])

    def test(self):
        self.registers[3] = 10
        self.registers[4] = 4
        self.Z80.SUBR(4, self.registers)
        print(self.registers[3])


if __name__ == '__main__':
    e = Computer()
    e.execute()
