import re
s = "How are you doing&& today?"
p = r'[^\w\s]'
rep_char = ""
pr = re.sub(p, rep_char, s)
print(pr)

