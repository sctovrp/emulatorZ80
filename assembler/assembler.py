import os


class Assembler:
    given_instructions = []

    def __init__(self, knew_instructions, knew_registers):
        self.knew_instructions = knew_instructions
        self.knew_registers = knew_registers

    def readFile(self, ):
        path = os.path.dirname(__file__)
        with open(path + '/input.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        read = []
        for line in lines:
            read.append(line.strip())
        Assembler.given_instructions = read

    def assemble(self, ):
        list_instructions = []
        list_operands1 = []
        list_operands2 = []
        for i in Assembler.given_instructions:
            split_line = i
            split_line = split_line.split(' ', 1)
            # print("initial", len(split_line))
            if len(split_line) == 1:
                # print("split", split_line, len(split_line))
                list_instructions.append(split_line[0])
                list_operands1.append(0)
                list_operands2.append(0)
            elif ',' not in split_line[1]:
                # print("split", split_line, len(split_line))
                list_instructions.append(split_line[0])
                list_operands1.append(split_line[1])
                list_operands2.append(0)
            elif ',' in split_line[1]:
                # print("split", split_line, len(split_line))
                operands = split_line[1].split(',', 1)
                list_instructions.append(split_line[0])
                list_operands1.append(operands[0])
                list_operands2.append(operands[1])
        print("ins", list_instructions)
        print("op1", list_operands1)
        print("op2", list_operands2)
        for i in range(len(list_instructions)):
            if list_instructions[i] in self.knew_instructions:
                list_instructions[i] = self.knew_instructions[list_instructions[i]]
        for i in range(len(list_operands1)):
            if list_operands1[i] in self.knew_registers:
                list_operands1[i] = self.knew_registers[list_operands1[i]]
            else:
                list_operands1[i] = int(list_operands1[i])
        for i in range(len(list_operands2)):
            if list_operands2[i] in self.knew_registers:
                list_operands2[i] = self.knew_registers[list_operands2[i]]
            elif list_operands2[i] == "":
                list_operands2[i] = 0
            else:
                list_operands2[i] = int(list_operands2[i])
        final_instructions = bytearray(list_instructions)
        final_operands1 = bytearray(list_operands1)
        final_operands2 = bytearray(list_operands2)
        # print(list_instructions)
        # print(list_operands1)
        # print(list_operands2)
        final_matrix = [final_instructions, final_operands1, final_operands2]
        return final_matrix
