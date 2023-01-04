from utils.fibunacci import create, locate


while True:
    line = input()
    if line == "Stop":
        break
    line_args = line.split()

nums = create(10)
idx = locate(13, nums)
if idx == -1:
    print("The number 13 is not in the sequence")
else:
    print("The number - 13 is at index 7")