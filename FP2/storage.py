def read_users_file(file_path):
    users = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                users.append((parts[0], int(parts[1])))
    return users

def format_size(size_in_bytes):
    size_in_mb = size_in_bytes / (1024 * 1024)
    return f"{size_in_mb:.2f} MB"

def generate_report(users, report_path):
    total_space = sum(user[1] for user in users)
    average_space = total_space / len(users)

    with open(report_path, 'w') as report:
        report.write("ASI Lda. Uso do espaço em disco pelos utilizadores\n")
        report.write("------------------------------------------------------------------------\n")
        report.write("Nr.\tUtilizador\tEspaço utilizado\t% de uso\n")

        for i, (user, space) in enumerate(users, start=1):
            percentage = (space / total_space) * 100
            report.write(f"{i}\t{user}\t{format_size(space)}\t{percentage:.2f}%\n")

        report.write(f"\nEspaço total ocupado: {format_size(total_space)}\n")
        report.write(f"Espaço médio ocupado: {format_size(average_space)}\n")

if __name__ == "__main__":
    users = read_users_file('users.txt')
    generate_report(users, 'relatorio.txt')