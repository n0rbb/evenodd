f = open("even.py", "a+")

f.write("n = int(input(\"Please enter n: \")) \n")
f.write("if n == 1: \n")
f.write("\t" + "print(\"odd\")".strip() + "\n")

n = int(input("Max int: "))

for i in range(n - 1):
    f.write("elif n == {}: \n".format(i + 2))
    if i % 2 == 0:
        f.write("\t" + "print(\"even\")".strip() + "\n")
    else:
        f.write("\t" + "print(\"odd\")".strip() + "\n")

f.close()
