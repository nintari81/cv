dict = {
    "a": "01100001", "b": "01100010", "c": "01100011"
}

letter = input("enter a letter to check: ")

output = ""

for char in letter:
    output += dict.get(char, " unknown")

print(output)