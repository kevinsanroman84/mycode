#!/usr/bin/env python3

num_lines = 0
with open("dracula.txt", "r") as foo:
    with open("vampytimex.txt", "w") as fang:
        for line in foo:
            if "vampire" in line.lower():
                print(line)
                num_lines += 1
                fang.write(line)
    print(num_lines)
