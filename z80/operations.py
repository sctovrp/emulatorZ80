class Operations:

    def LDR(self, argument1, argument2, storage):
        a = argument1
        b = argument2
        storage[a] = b

    def INR(self, port, registries, ports):
         registries[3] = ports[port]

    def INCR(self, register, regisitries):
        regisitries[register] = regisitries[register] + 1

    def DECR(self, register, regisitries):
        regisitries[register] = regisitries[register] - 1

    def AND(self, register, registries):
        x = registries[register]
        y = registries[3]
        registries[3] = x & y

    def OR(self, register, registries):
        x = registries[register]
        y = registries[3]
        registries[3] = x | y

    def CPL(self, register, registries):
        x = registries[register]
        registries[register] = ~x

    def NEG(self, register, registries):
        x = registries[register]
        registries[register] = ~x + 1

    def XOR(self, register, registries):
        x = registries[register]
        y = registries[3]
        registries[3] = x ^ y

    def ORG(self, value, registries):
        registries[1] = value

    def SET(self, register, registries, position):

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

    def RESET(self, register, registries, position):

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

    def ADDR(self, register, registries):
        y = registries[register]
        x = registries[3]
        sum = x + y
        registries[3] = sum

    def SUBR(self, register, registries):
        y = registries[register]
        x = registries[3]
        sum = x - y
        registries[3] = sum

    def RLA(self, register, registries):

        binNum = ""
        digito = []
        numb = registries[register]
        digitoNew = []
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

        for i in range(6):
            digitoNew[i] = digito[i+1]

        digitoNew.append(digito[0])

        for g in range(8):
            strFinal += str(digitoNew[g])

        binFinal = int(strFinal)

        decimal, i, n = 0, 0, 0
        while (binFinal != 0):
            dec = binFinal % 10
            decimal = decimal + dec * pow(2, i)
            binFinal = binFinal // 10
            i += 1

        registries[register] = decimal

    def RRA(self, register, registries):

        binNum = ""
        digito = []
        numb = registries[register]
        digitoNew = []
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

        digitoNew.append(digito[7])

        for i in range(7):
            digitoNew.append(digito[i])

        for g in range(8):
            strFinal += str(digitoNew[g])

        binFinal = int(strFinal)

        decimal, i, n = 0, 0, 0
        while (binFinal != 0):
            dec = binFinal % 10
            decimal = decimal + dec * pow(2, i)
            binFinal = binFinal // 10
            i += 1

        registries[register] = decimal

    def OUT(self, port, ports, registries):
        ports[port] = registries[3]

    def HALT(self):
        pass

    def END(self):
        pass

    def PUSH(self, stack, registers, value):
        stack.append(value)
        registers[2] += 1

    def POP(self, stack, registers):
        stack.pop()
        registers[2] -= 1