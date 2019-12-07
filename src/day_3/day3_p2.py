from input_data import get_data
from calculations import Wire

# wire3 = Wire(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'])
# wire4 = Wire(['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'])
# coords3 = wire3.travel()
# coords4 = wire4.travel()
# intersection_cords2 = wire3.get_intersections(coords4)
# assert min(wire3.manhattan_distance(value) for value in intersection_cords2) == 159

wire5 = Wire(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'])
wire6 = Wire(['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'])
coords5 = wire5.travel()
coords6 = wire6.travel()
intersection_cords3 = wire5.get_intersections(coords6)
print(wire6.steps_to_point(intersection_cords3[0]))
