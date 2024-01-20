def generate_truth_table(input_values):
    headers = [f"Column {i + 1}" for i in range(len(input_values))]
    rows = [[str(int(bool(int(bit)))) for bit in f"{i:0{len(input_values)}b}"] for i in range(2 ** len(input_values))]
    truth_table = [headers] + rows
    return truth_table
