import os
from bitstring import BitArray


class Assembler:
    given_instructions = []
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
        'JP': 22,  # grupo de decisiones--------------
        'CALL': 23,
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

    def readFile(self):
        path = os.path.dirname(__file__)
        with open(path + '/input.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        read = []
        for line in lines:
            read.append(line.strip())
        Assembler.given_instructions = read

    def assemble(self):
        list_instructions = []
        list_operands1 = []
        list_operands2 = []
        for i in Assembler.given_instructions:
            split_line = i
            split_line = split_line.split(' ', 1)
            operands = split_line[1].split(',', 1)
            list_instructions.append(split_line[0])
            list_operands1.append(operands[0])
            if len(operands) == 2:
                list_operands2.append(operands[1])
            else:
                list_operands2.append("")
        for i in range(len(list_instructions)):
            if list_instructions[i] in Assembler.knew_instructions:
                list_instructions[i] = Assembler.knew_instructions[list_instructions[i]]
        for i in range(len(list_operands1)):
            if list_operands1[i] in Assembler.knew_registers:
                list_operands1[i] = Assembler.knew_registers[list_operands1[i]]
            else:
                list_operands1[i] = int(list_operands1[i])
        for i in range(len(list_operands2)):
            if list_operands2[i] in Assembler.knew_registers:
                list_operands2[i] = Assembler.knew_registers[list_operands2[i]]
            elif list_operands2[i] == "":
                list_operands2[i] = 0
            else:
                list_operands2[i] = int(list_operands2[i])
        final_instructions = bytearray(list_instructions)
        final_operands1 = bytearray(list_operands1)
        final_operands2 = bytearray(list_operands2)
        final_matrix = [final_instructions, final_operands1, final_operands2]
        return final_matrix
