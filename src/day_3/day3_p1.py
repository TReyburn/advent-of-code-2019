from input_data import get_data
from calculations import Wire

wire1 = Wire(['R8', 'U5', 'L5', 'D3'])
wire2 = Wire(['U7', 'R6', 'D4', 'L4'])
coords1 = wire1.travel()
coords2 = wire2.travel()
intersection_cords1 = wire1.v2_get_intersections(coords2)
assert min(wire1.manhattan_distance(value) for value in intersection_cords1) == 6
for value in intersection_cords1:
    print(value['step'], value['f_step'])

wire3 = Wire(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'])
wire4 = Wire(['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'])
coords3 = wire3.travel()
coords4 = wire4.travel()
intersection_cords2 = wire3.v2_get_intersections(coords4)
assert min(wire3.manhattan_distance(value) for value in intersection_cords2) == 159
# print(min(value['step'] + value['f_step'] for value in intersection_cords2))

wire5 = Wire(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'])
wire6 = Wire(['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'])
coords5 = wire5.travel()
coords6 = wire6.travel()
intersection_cords3 = wire5.v2_get_intersections(coords6)
assert min(wire5.manhattan_distance(value) for value in intersection_cords3) == 135

data = get_data('data.txt')
real_wire1 = Wire(data['Wire_0'])
real_wire2 = Wire(data['Wire_1'])
real_coords1 = real_wire1.travel()
real_coords2 = real_wire2.travel()
real_intersections = real_wire1.v2_get_intersections(real_coords2 )
print(min(real_wire1.manhattan_distance(value) for value in real_intersections))
