from typing import List, Any
from machine.memory import Memory
from assembler.assembler import Assembler


class Operations:

    u = Assembler()
    u.readFile()

    inpSheet = Assembler().assemble()

    instructions = []
    arg1 = []
    arg2 = []

    flagP = True

    memoir = [0] * 25
    ports = [0]*25
    registries = [0] * 25

    for i in range(len(inpSheet[0])):
        instructions.append(inpSheet[0][i])
        arg1.append(inpSheet[1][i])
        arg2.append(inpSheet[2][i])

    # print(instructions)
    # print(arg1)
    # print(arg2)

    # insDictionary = Assembler().knew_instructions
    # regDictionary = Assembler().knew_registers
    #
    # print(insDictionary.get("IN"))
    # print(regDictionary)

    # b = Assembler.

    # hexInpSheet = x.assemble()
    #
    # print(inpSheet)
    #
    # opSheet = x.given_instructions
    #
    # print(opSheet)

    def LDR(argument1, argument2, storage):
        a = argument1
        b = argument2
        storage[a] = b

    def LDC(argument1, argument2, storage):
        a = argument1
        b = argument2
        storage[b] = storage[a]

    def INR(port, register, storage, ports, pflag):

        ports[port] = storage[register]
        # if (ports[port] % 2) == 0:
        #     pflag = True
        # else:
        #     pflag = False

    def OUTR(port, register, storage, ports):
        storage[register] = ports[port]

    def ADDR(register, lista):
        lista[register] += lista[3]

    def ADDV(additive, lista, lista2 = []):
        sum = additive + lista[3]
        lista2.append(sum)

    def INCR(register, regisitries):
        regisitries[register] = regisitries[register] + 1

    def INCM(address, memories):
        memories[address] = memories[address] + 1

    def DECR(register, regisitries):
        regisitries[register] = regisitries[register] - 1

    def DECM(address, memories):
        memories[address] = memories[address] - 1

    def SET(register, registries, position):

        binNum = ""
        digito = []
        numb = registries[register]
        strFinal = ""

        if numb <= 0:
            return "0"
            binNum = ""
        while numb > 0:
            residuo = int(numb % 2)
            numb = int(numb / 2)
            binNum = str(residuo) + binNum
        
        strNum = binNum

        for j in range(8-len(strNum)):
            digito.append(0)

        for digito_string in strNum:
            digito.append(int(digito_string))

        digito[7-position] = 1

        for g in range(8):
            strFinal += str(digito[g])

        binFinal = int(strFinal)

        decimal, i, n = 0, 0, 0
        while (binFinal != 0):
            dec = binFinal % 10
            decimal = decimal + dec * pow(2, i)
            binFinal = binFinal // 10
            i += 1

        registries[register] = decimal

    def RESET(register, registries, position):

        binNum = ""
        digito = []
        numb = registries[register]
        strFinal = ""

        if numb <= 0:
            return "0"
            binNum = ""
        while numb > 0:
            residuo = int(numb % 2)
            numb = int(numb / 2)
            binNum = str(residuo) + binNum

        strNum = binNum

        for j in range(8 - len(strNum)):
            digito.append(0)

        for digito_string in strNum:
            digito.append(int(digito_string))

        digito[7 - position] = 0

        for g in range(8):
            strFinal += str(digito[g])

        binFinal = int(strFinal)

        decimal, i, n = 0, 0, 0
        while (binFinal != 0):
            dec = binFinal % 10
            decimal = decimal + dec * pow(2, i)
            binFinal = binFinal // 10
            i += 1

        registries[register] = decimal

    def ADDR(register, registries):
        y = registries[register]
        x = registries[3]
        sum = x + y
        registries[3] = sum

    def ADDV(value, registries):
        y = value
        x = registries[3]
        sum = x + y
        registries[3] = sum

    def ADDM(memory, memoir, registries):
        y = memoir[memory]
        x = registries[3]
        sum = x + y
        registries[3] = sum

    def SUBR(register, registries):
        y = registries[register]
        x = registries[3]
        sum = x - y
        registries[3] = sum

    def SUBV(value, registries):
        y = value
        x = registries[3]
        sum = x - y
        registries[3] = sum

    def SUBM(memory, memoir, registries):
        y = memoir[memory]
        x = registries[3]
        sum = x - y
        registries[3] = sum
