def fuel_counter_upper(file: str) -> int:
    total = 0
    with open(file) as fh:
        for value in fh:
            total += fuel_calc(value)
    return total


def fuel_calc(value: str or int) -> int:
    fuel_amt = max(0, int(int(value) / 3) - 2)
    return fuel_amt


def fuel_calc_v2(value: str or int) -> int:
    fuel = fuel_calc(value)
    if fuel > 0:
        fuel += fuel_calc_v2(fuel)
    return fuel


def fuel_counter_upper_v2(file: str) -> int:
    total = 0
    with open(file) as fh:
        for value in fh:
            total += fuel_calc_v2(value)
    return total
