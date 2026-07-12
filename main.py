import os
import sys


def import_module(name):
    mod = __import__(name)
    components = name.split(".")
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


runType = sys.argv[1]
year = sys.argv[2]
day = sys.argv[3]

sys.path.append(os.path.abspath(os.path.join("..")))

dayScript = import_module(f"{year}.{day}.ff")

if runType == "test":
    print(f"Running day {year}/{day} --- TEST")
    file = open(f"{year}/{day}/input_test_1.txt", "r")
else:
    print(f"Running day {year}/{day}")
    file = open(f"{year}/{day}/input_1.txt", "r")


lines = [x.strip("\n") for x in file.readlines()]
if len(sys.argv) == 4 or sys.argv[4] == "1":
    print("Solution part 1 : ", dayScript.solution_1(lines))

if len(sys.argv) == 4 or sys.argv[4] == "2":
    print("Solution part 2 : ", dayScript.solution_2(lines))

if len(sys.argv) == 4 or sys.argv[4] == "3":
    print("Solution part 3 : ", dayScript.solution_3(lines))
