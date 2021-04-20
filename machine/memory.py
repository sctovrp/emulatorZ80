class Memory:
    def __init__(self):
        self.size_t = 256
        self.memory = {}
        for i in range(256):
            self.memory[hex(i)] = None

    def set(self, hex_code, value):
        if hex_code not in self.memory.keys():
            return
        self.memory[hex_code] = value

    def get(self, hex_code):
        if hex_code not in self.memory.keys():
            return
        return self.memory.get(hex_code)

    def get_size(self):
        return self.size_t

    def get_memory(self):
        return self.memory

    def show(self):
        print('\nMemory')
        for pos, entry in self.memory.items():
            if entry is None:
                break
            print(f'Position: {pos} \t Value: {entry}')
