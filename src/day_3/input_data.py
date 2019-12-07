def get_data(file: str) -> dict:
    wire_dict = {}
    with open(file) as fh:
        for num, line in enumerate(fh):
            wire_dict[f'Wire_{num}'] = list(line.strip().split(','))
        return wire_dict
