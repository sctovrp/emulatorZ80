class Linker:
    def resolve(self, machine_code):
        n = len(machine_code[0])
        assert n <= 200
        free_mem_positions = []
        for index in range(n * 3):
            free_mem_positions.append(hex(index))
        result = [free_mem_positions]
        result.extend(machine_code)
        return result
