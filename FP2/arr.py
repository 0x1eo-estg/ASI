from collections import Counter

arr = [8, 7, 8, 6, 10, 12, 14, 12, 18, 12, 17]

frequencies = Counter(arr)
for note, frequency in frequencies.items():
    print(f"Nota: {note}, Frequência: {frequency}")

with open('notas.txt', 'w') as file:
    for note, frequency in frequencies.items():
        file.write(f"{note},{frequency}\n")
