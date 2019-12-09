class Wire(object):

    def __init__(self, user_list: list):
        self._central_port = {'x': 0, 'y': 0}
        self._wire = user_list
        self._length = len(user_list)
        self._wire_end = {'x': 0, 'y': 0}
        self._wire_coords = []
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

    def v2_get_intersections(self, comparison_list: list) -> list:
        intersections = []
        self._steps = 0
        for value in range(self._length - 1):
            _1xfrom, _1xto, _1yfrom, _1yto = self._get_coords(self._wire_coords, value)
            if _1xfrom == _1xto:
                self._steps += abs(_1yfrom - _1yto)
                self._check_intersections(_1xto, _1yfrom, _1yto, comparison_list, intersections, side='x')
            elif _1yfrom == _1yto:
                self._steps += abs(_1xfrom - _1xto)
                self._check_intersections(_1yto, _1xfrom, _1xto, comparison_list, intersections, side='y')
        return intersections

    # This function is way too big and needs refactoring
    def get_intersections(self, comparison_list: list) -> list:
        intersections = []
        list_len = len(comparison_list)
        self._steps = 0
        foreign_step = 0
        for val in range(self._length + 1):
            if self._length - 1 > val:
                wire1_xfrom = self._wire_coords[val]['x']
                wire1_xto = self._wire_coords[val + 1]['x']
                wire1_yfrom = self._wire_coords[val]['y']
                wire1_yto = self._wire_coords[val + 1]['y']
                if wire1_xfrom == wire1_xto:
                    self._steps += abs(wire1_yfrom - wire1_yto)
                    for val2 in range(len(comparison_list) + 1):
                        if list_len - 1 > val2:
                            wire2_xfrom = comparison_list[val2]['x']
                            wire2_xto = comparison_list[val2 + 1]['x']
                            wire2_yfrom = comparison_list[val2]['y']
                            wire2_yto = comparison_list[val2 + 1]['y']
                            if wire2_yfrom == wire2_yto:
                                foreign_step += abs(wire2_xfrom - wire2_xto)
                                for xval in self.reversible_range(wire2_xfrom, wire2_xto):
                                    if xval == wire1_xfrom and wire2_yto in self.reversible_range(wire1_yto, wire1_yfrom):
                                        foreign_step -= abs(wire2_yto - max(wire1_yto, wire1_yfrom))
                                        self._steps -= abs(wire2_yto - max(wire1_yto, wire1_yfrom))
                                        intersections.append(dict({'x': xval, 'y': wire2_yto, 'step': int(self._steps), 'f_step': int(foreign_step)}))
                elif wire1_yfrom == wire1_yto:
                    self._steps += abs(wire1_xfrom - wire1_xto)
                    for val2 in range(len(comparison_list) + 1):
                        if list_len - 1 > val2:
                            wire2_xfrom = comparison_list[val2]['x']
                            wire2_xto = comparison_list[val2 + 1]['x']
                            wire2_yfrom = comparison_list[val2]['y']
                            wire2_yto = comparison_list[val2 + 1]['y']
                            if wire2_xfrom == wire2_xto:
                                foreign_step += abs(wire2_yfrom - wire2_yto)
                                for yval in self.reversible_range(wire2_yfrom, wire2_yto):
                                    if yval == wire1_yfrom and wire2_xto in self.reversible_range(wire1_xto, wire1_xfrom):
                                        foreign_step += abs(wire2_xto - max(wire1_xto, wire1_xfrom))
                                        self._steps += abs(wire2_xto - max(wire1_xto, wire1_xfrom))
                                        intersections.append(dict({'x': wire2_xto, 'y': yval, 'step': int(self._steps), 'f_step': int(foreign_step)}))
                                        # foreign_step = 0
                                        # self._steps = 0
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
        # print(self._steps)

    def _down(self):
        self._wire_end['y'] -= int(self._wire[self._list_position][1:])
        self._wire_coords.append(dict(self._wire_end))
        self._steps += int(self._wire[self._list_position][1:])
        # print(self._steps)

    def _right(self):
        self._wire_end['x'] += int(self._wire[self._list_position][1:])
        self._wire_coords.append(dict(self._wire_end))
        self._steps += int(self._wire[self._list_position][1:])
        # print(self._steps)

    def _left(self):
        self._wire_end['x'] -= int(self._wire[self._list_position][1:])
        self._wire_coords.append(dict(self._wire_end))
        self._steps += int(self._wire[self._list_position][1:])
        # print(self._steps)

    def _reset(self):
        self._wire_end = {'x': 0, 'y': 0}
        self._wire_coords = []
        self._list_position = 0
        self._status = False
        self._steps = 0

    @staticmethod
    def reversible_range(x: int, y: int) -> range:
        return range(min(x, y), max(x + 1, y + 1))

    #counting the steps is still messed up here
    def _check_intersections(self, coord_val: int, _from: int, _to: int, _list: list, return_list: list, side=None):
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
                                    {'x': x_val, 'y': _yto, 'step': int(self._steps + abs(_yto - _from)),
                                     'f_step': int(foreign_step + abs(_yto - _from))}))
                    else:
                        foreign_step += abs(_yfrom + _yto)
                elif side == 'y':
                    if _xfrom == _xto:
                        foreign_step += abs(_yfrom - _yto)
                        for y_val in self.reversible_range(_yfrom, _yto):
                            if y_val == coord_val and _xto in self.reversible_range(_to, _from):
                                return_list.append(dict(
                                    {'x': y_val, 'y': _xto, 'step': int(self._steps + abs(_xto - _from)),
                                     'f_step': int(foreign_step + abs(_xto - _from))}))
                    else:
                        foreign_step += abs(_xfrom + _xto)
        return return_list

    @staticmethod
    def _get_coords(_list: list, value: int):
        if len(_list) > value + 1:
            _xfrom = _list[value]['x']
            _xto = _list[value + 1]['x']
            _yfrom = _list[value]['y']
            _yto = _list[value + 1]['y']
            return _xfrom, _xto, _yfrom, _yto

    # def steps_to_point(self, point: dict) -> int:
    #     self._reset()
    #     for val in range(self._length):
    #         self._interpret()
    #         self._list_position += 1
    #         print(self._steps)
    #         if self._wire_end['x'] == point['x'] and self._wire_end['y'] == point['y']:
    #             print('point found')
    #             self._status = False
    #             return self._steps
