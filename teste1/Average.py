from ReadLogFile import Read

def AverageMethod(file_path, specific_date):
    Log = Read(file_path)
    methods = {}
    for host in Log:
        if specific_date in Log[host]:
            for request, _, _ in Log[host][specific_date]:
                method = request.split()[0]
                if method not in methods:
                    methods[method] = 0
                methods[method] += 1
    return max(methods, key=methods.get) if methods else None

#print(AverageMethod("accesslog.txt", "2024/10/22"))