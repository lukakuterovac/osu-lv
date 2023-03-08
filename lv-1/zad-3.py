def mean(arr):
    return sum(arr) / len(arr)


arr = []

while True:
    x = input()
    if x.isnumeric():
        arr.append(int(x))
    elif x.lower() == "done":
        break
    else:
        print("Enter a number")

print(f"Uneseno {len(arr)} br")
print(f"Srednja vrijednost {mean(arr)}")
print(f"Min {min(arr)}, max {max(arr)}")
arr.sort()
print(f"Sort: {arr}")
