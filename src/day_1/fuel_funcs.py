def fuel_counter_upper(file: str) -> int:
    total = 0
    with open(file) as fh:
        for value in fh:
            total += fuel_calc(value)
    return total


def fuel_calc(value: str) -> int:
    fuel_amt = int(int(value) / 3) - 2
    return fuel_amt