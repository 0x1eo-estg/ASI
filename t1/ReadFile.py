def Read(file_path):
    backups = {}
    
    with open(file_path, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            date_time, host, status = line.strip().split(';')
            date, time = date_time.split()
            if status == 'Success':
                if date not in backups:
                    backups[date] = {}
                if host not in backups[date]:
                    backups[date][host] = []
                backups[date][host].append(time)
    
    return backups