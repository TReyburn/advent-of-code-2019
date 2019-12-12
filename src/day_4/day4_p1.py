def password_slicer(value):
    double_counter = 0
    if not 5 < len(value) <= 6:
        return False
    for _slice in range(len(value) - 1):
        if value[_slice] > value[_slice + 1]:
            return False
        elif value[_slice] == value[_slice + 1]:
            double_counter += 1
    if not double_counter >= 1:
        return False
    return True


assert password_slicer('111111')
assert not password_slicer('223450')
assert not password_slicer('123789')

password_compatible = 0
for combo in range(359282, 820401 + 1):
    if password_slicer(str(combo)):
        password_compatible += 1

print(password_compatible)
