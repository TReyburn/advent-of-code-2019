# def _get_coords(_list: list, value: int):
#     if len(_list) - 1 > value:
#         _xfrom = _list[value]['x']
#         _xto = _list[value + 1]['x']
#         _yfrom = _list[value]['y']
#         _yto = _list[value + 1]['y']
#         return _xfrom, _xto, _yfrom, _yto
#
#
# my_test_list = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}]
#
# xfrom, xto, yfrom, yto = _get_coords(my_test_list, 0)
#
# print(xfrom)
# print(xto)
# print(yfrom)
# print(yto)
from calculations import Wire

wire1 = Wire(['R8', 'U5', 'L5', 'D3'])
wire2 = Wire(['U7', 'R6', 'D4', 'L4'])
coords1 = wire1.travel()
coords2 = wire2.travel()
intersection_cords1 = wire1.get_intersections(coords2)
assert min(wire1.manhattan_distance(value) for value in intersection_cords1[1:]) == 6

print(intersection_cords1)
