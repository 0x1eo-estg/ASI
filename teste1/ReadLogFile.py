def Read(file_path):
    Log = {}
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            host, date, request, status, bytes = line.strip().split(';')
            if host not in Log:
                Log[host] = {}
            if date not in Log[host]:
                Log[host][date] = []
            Log[host][date].append((request, status, bytes))
    return Log

#print(Read("accesslog.txt"))