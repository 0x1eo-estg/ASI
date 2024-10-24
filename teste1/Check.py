from ReadLogFile import Read

def Check(file_path):
    Log = Read(file_path)
    requests = []
    for host in Log:
        for date in Log[host]:
            for request, _, bytes in Log[host][date]:
                if bytes != " -" and int(bytes) > 1024:
                    requests.append(request)
    return requests

#print(Check("accesslog.txt"))