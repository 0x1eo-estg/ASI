def bckSuccess(log_data):
    failed_backups = {}

    lines = log_data.strip().split('\n')

    # Skip the header
    lines = lines[1:]

    for line in lines:
        date_time, host, status = line.split(';')
        date, time = date_time.split(' ')
        
        if status == 'Failed':
            if host not in failed_backups:
                failed_backups[host] = []
            failed_backups[host].append(date + ' ' + time)

    return failed_backups

with open("./backup.txt", "r") as file:
    log_data = file.read()

print(bckSuccess(log_data))