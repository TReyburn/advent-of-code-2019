def password_slicer_p2(value):
    double_counter = 0
    if not 5 < len(value) <= 6:
        return False
    for _slice in range(len(value) - 1):
        larger_match = 0
        if value[_slice] > value[_slice + 1]:
            return False
        elif value[_slice] == value[_slice + 1]:
            try:
                if value[_slice] == value[_slice + 2]:
                    larger_match += 1
            except IndexError:
                pass
            try:
                if value[_slice] == value[_slice - 1]:
                    larger_match += 1
            except IndexError:
                pass
            if larger_match == 0:
                double_counter += 1
    if not double_counter >= 1:
        return False
    return True


assert password_slicer_p2('112233')
assert not password_slicer_p2('123444')
assert password_slicer_p2('111122')

password_compatible = 0
for combo in range(359282, 820401 + 1):
    if password_slicer_p2(str(combo)):
        password_compatible += 1

print(password_compatible)
