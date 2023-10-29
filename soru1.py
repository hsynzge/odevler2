a, b = 1, 1
fibonacciserisi = [a, b]

while len(fibonacciserisi) < 20:
    a, b = b, a + b
    fibonacciserisi.append(b)

print(fibonacciserisi)
