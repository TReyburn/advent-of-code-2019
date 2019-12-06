class IntComputer(object):
    def __init__(self, opcode: list):
        self._opcode = opcode
        self._length = int(len(opcode) / 4)
        self._command = None
        self._vpos1 = None
        self._vpos2 = None
        self._store = None
        self._travel = None
        self._status = True
        self._pop = 0

    def __str__(self) -> str:
        return str(self._opcode)

    def update(self, position: int, value: int):
        self._opcode[position] = value

    def run(self):
        self._repair()
        while self._check_status():
            self._travel = self._traverse()
            for _code in range(self._length):
                next(self._travel)
                self._process()
                if not self._check_status():
                    break
            if not self._check_status():
                for x in range(self._pop):
                    self._opcode.pop()
                print(self)
                return self._opcode
            self.run()

    def _traverse(self):
        for _code in range(self._length):
            self._command = self._opcode[_code * 4]
            self._vpos1 = self._opcode[_code * 4 + 1]
            self._vpos2 = self._opcode[_code * 4 + 2]
            self._store = self._opcode[(_code + 1) * 4 - 1]
            yield self._command, self._vpos1, self._vpos2, self._store

    def _process(self):
        if type(self._interpret()) == list:
            self._status = False
        else:
            return self.update(self._store, self._interpret())

    def _add(self):
        return self._opcode[self._vpos1] + self._opcode[self._vpos2]

    def _multiply(self):
        return self._opcode[self._vpos1] * self._opcode[self._vpos2]

    def _interpret(self):
        if self._command == 99:
            return self._opcode
        elif self._command == 1:
            return self._add()
        elif self._command == 2:
            return self._multiply()
        else:
            print(self)
            raise Exception(f'unrecognized command: {self._command}')

    def _check_status(self):
        return self._status

    def _repair(self):
        if len(self._opcode) % 4 == 0:
            pass
        else:
            for x in range(_pop := (4 - len(self._opcode) % 4)):
                self._opcode.append(0)
            self._length += 1
            self._pop = _pop
