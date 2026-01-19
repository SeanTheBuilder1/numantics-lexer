import sys
import json

from lexer_analyzer import analyzeSource

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

def main():
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "[file] [optional: save file]")
        return
    file = open(sys.argv[1], "r")
    code = file.read()
    tokens = analyzeSource(code)
    token_list = []
    line_starts = build_line_starts(code)
    for t in tokens:
        start_line, start_col = index_to_line_col_batch(t.start, line_starts)
        end_line, end_col = index_to_line_col_batch(t.end, line_starts)
        token_list.append({
            'type': str(t.type.name),
            'start': int(t.start),
            'end': int(t.end),
            'start_line': start_line,
            'start_col': start_col,
            'end_line': end_line,
            'end_col': end_col,
            'lexeme': code[t.start:t.end],
        })
    print(tokens)
    file.close()
    if len(sys.argv) >= 3:
        with open(sys.argv[2], "w") as f:
            json.dump(token_list, f, indent=2)



if __name__ == "__main__":
    main()
