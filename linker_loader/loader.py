

class Loader:
    def load(self, machine_code_mem, memory):
        n = len(machine_code_mem[0])
        index = 0
        for i in range(n // 3):
            mem_pos = machine_code_mem[0]
            instruction = machine_code_mem[1][i]
            first_arg = machine_code_mem[2][i]
            second_arg = machine_code_mem[3][i]
            memory[mem_pos[index]] = instruction
            memory[mem_pos[index + 1]] = first_arg
            memory[mem_pos[index + 2]] = second_arg
            index += 3