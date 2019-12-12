class Wire(object):

    def __init__(self, user_list: list):
        self._central_port = {'x': 0, 'y': 0}
        self._wire = user_list
        self._length = len(user_list)
        self._wire_end = {'x': 0, 'y': 0}
        self._wire_coords = [{'x': 0, 'y': 0}, ]
        self._list_position = 0
        self._status = False
        self._steps = 0

    def travel(self) -> list:
        if not self._status:
            self._reset()
            for val in range(self._length):
                self._interpret()
                self._list_position += 1
        self._status = True
        return self._wire_coords

    def get_end(self) -> dict:
        return self._wire_end

    def manhattan_distance(self, value: dict) -> int:
        distance = abs(self._central_port['x'] + value['x']) + abs(self._central_port['y'] + value['y'])
        return distance

    def coord_test(self):
        return self._get_coords(self._wire_coords, 0)

    def get_intersections(self, comparison_list: list) -> list:
        intersections = []
        self._steps = 0
        for value in range(self._length):
            _1xfrom, _1xto, _1yfrom, _1yto = self._get_coords(self._wire_coords, value)
            if _1xfrom == _1xto:
                self._steps += abs(_1yfrom - _1yto)
                self._check_intersections(_1xto, _1yfrom, _1yto, comparison_list, intersections, side='x')
            elif _1yfrom == _1yto:
                self._steps += abs(_1xfrom - _1xto)
                self._check_intersections(_1yto, _1xfrom, _1xto, comparison_list, intersections, side='y')
        return intersections

    def _interpret(self):
        if self._wire[self._list_position][0] == 'U':
            self._up()
        elif self._wire[self._list_position][0] == 'D':
            self._down()
        elif self._wire[self._list_position][0] == 'R':
            self._right()
        elif self._wire[self._list_position][0] == 'L':
            self._left()

    def _up(self):
        self._wire_end['y'] += int(self._wire[self._list_position][1:])
        self._wire_coords.append(dict(self._wire_end))
        self._steps += int(self._wire[self._list_position][1:])

    def _down(self):
        self._wire_end['y'] -= int(self._wire[self._list_position][1:])
        self._wire_coords.append(dict(self._wire_end))
        self._steps += int(self._wire[self._list_position][1:])

    def _right(self):
        self._wire_end['x'] += int(self._wire[self._list_position][1:])
        self._wire_coords.append(dict(self._wire_end))
        self._steps += int(self._wire[self._list_position][1:])

    def _left(self):
        self._wire_end['x'] -= int(self._wire[self._list_position][1:])
        self._wire_coords.append(dict(self._wire_end))
        self._steps += int(self._wire[self._list_position][1:])

    def _reset(self):
        self._wire_end = {'x': 0, 'y': 0}
        self._wire_coords = [{'x': 0, 'y': 0}, ]
        self._list_position = 0
        self._status = False
        self._steps = 0

    @staticmethod
    def reversible_range(x: int, y: int) -> range:
        return range(min(x, y), max(x + 1, y + 1))

    # counting the steps is finally fixed - but this could be refactored into smaller functions
    def _check_intersections(self, coord_val: int,
                             _from: int, _to: int,
                             _list: list, return_list: list,
                             side=None) -> list:
        foreign_step = 0
        for value in range(len(_list)):
            if len(_list) > value + 1:
                _xfrom, _xto, _yfrom, _yto = self._get_coords(_list, value)
                if side == 'x':
                    if _yfrom == _yto:
                        foreign_step += abs(_xfrom - _xto)
                        for x_val in self.reversible_range(_xfrom, _xto):
                            if x_val == coord_val and _yto in self.reversible_range(_to, _from):
                                return_list.append(dict(
                                    {'x': x_val, 'y': _yto, 'step': int(self._steps - abs(_to - _yto)),
                                     'f_step': int(foreign_step - abs(_xto - x_val))}))
                    else:
                        foreign_step += abs(_yfrom - _yto)
                elif side == 'y':
                    if _xfrom == _xto:
                        foreign_step += abs(_yfrom - _yto)
                        for y_val in self.reversible_range(_yfrom, _yto):
                            if y_val == coord_val and _xto in self.reversible_range(_to, _from):
                                return_list.append(dict(
                                    {'x': y_val, 'y': _xto, 'step': int(self._steps - abs(_to - _xto)),
                                     'f_step': int(foreign_step - abs(_yto - y_val))}))
                    else:
                        foreign_step += abs(_xfrom - _xto)
        return return_list

    @staticmethod
    def _get_coords(_list: list, value: int) -> tuple:
        if len(_list) > value + 1:
            _xfrom = _list[value]['x']
            _xto = _list[value + 1]['x']
            _yfrom = _list[value]['y']
            _yto = _list[value + 1]['y']
            return _xfrom, _xto, _yfrom, _yto
