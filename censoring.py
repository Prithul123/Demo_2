string = input().strip()
sub = input().strip()
for x in range(len(string)):
    samestring = string
    string = string.replace(sub, "")
    if string == samestring:
        break
print(string)