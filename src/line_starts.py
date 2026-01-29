def build_line_starts(text: str):
    line_starts = [0]
    for i, c in enumerate(text):
        if c == "\n":
            line_starts.append(i + 1)
    return line_starts


def index_to_line_col_batch(idx: int, line_starts: list[int]):
    low, high = 0, len(line_starts) - 1
    while low <= high:
        mid = (low + high) // 2
        if line_starts[mid] <= idx:
            low = mid + 1
        else:
            high = mid - 1
    line = high + 1
    col = idx - line_starts[high] + 1
    return line, col
