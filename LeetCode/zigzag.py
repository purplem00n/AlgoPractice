# medium

def convert(s: str, num_rows: int) -> str:
    if len(s) <= num_rows:
        return s
        
    matrix = [[] for _ in range(num_rows)]
    step = 1
    row = 0

    for letter in s:
        matrix[row].append(letter)
        if row == num_rows - 1:
            step = -1
        if row == 0:
            step = 1
        row += step
    print(matrix)

    result = []
    for row in matrix:
        for letter in row:
            result.append(letter)
    return "".join(result)

print(convert("PAYPALISHIRING", 3))