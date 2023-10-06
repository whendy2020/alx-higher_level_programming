#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = len(sys.argv) - 1
    if (total == 1):
        print("{} argument:".format(total))

    if total > 1:
        print("{} arguments:".format(total))
    if total == 0:
        print("{} argument.".format(total))
    count = 1
    arguments = sys.argv[1:]
    for arg in arguments:
        print(f"{count}: {arg}")
        count += 1
