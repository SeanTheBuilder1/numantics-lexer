import sys

from lexer_analyzer import analyzeSource


def main():
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "[file]")
        return
    file = open(sys.argv[1], "r")
    code = file.read()
    tokens = analyzeSource(code)
    print(tokens)
    file.close()


if __name__ == "__main__":
    main()
