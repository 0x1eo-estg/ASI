def AverageBakupTime(logs, date):
    total_time = 0
    count = 0

    for log in logs:
        if log['date'] == date:
            total_time += log['backup_time']
            count += 1

    if count == 0:
        return 0  # or raise an exception if no logs are found for the given date

    return total_time / count