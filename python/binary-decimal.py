n = int(input())
n_str = str(n)
i = -1
binary = ""
while i >= -len(n_str):
    binary += n_str[i]
    i -= 1
j = 0
decimal = 0
while j < len(binary):
    decimal += int(binary[j]) * (2 ** j)
    j += 1

print(decimal)
