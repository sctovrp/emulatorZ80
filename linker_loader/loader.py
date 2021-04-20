class Loader:
    def load(self, machine_code_mem):
        n = len(machine_code_mem[0])
        result = {}
        for i in range(n):
            mem_pos = machine_code_mem[0][i]
            instruction = machine_code_mem[1][i]
            first_arg = machine_code_mem[2][i]
            second_arg = machine_code_mem[3][i]
            result[mem_pos] = instruction
            result[mem_pos] = first_arg
            result[mem_pos] = second_arg
        return result