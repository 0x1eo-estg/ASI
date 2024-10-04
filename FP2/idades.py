with open('./idades.txt', 'r') as file:
    idades = [int(age) for age in file.read().split(',')]

print(min(idades))

print(max(idades))

avg = sum(idades) / len(idades)
print(avg)

filtered_ages = [age for age in idades if 18 <= age <= 65]
avg_filtered = sum(filtered_ages) / len(filtered_ages)
print(avg_filtered)