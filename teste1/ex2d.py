import re

with open ("accesslog.txt", 'r') as fp:
    next(fp)
    count = 1
    for line in fp:
        count+=1
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3};\d{4}/\d{2}/\d{2};.* /.* HTTP/\d\.\d; [1-5]\d{2}; \d{1,}$", line): #perdi-me
            print(f"Linha nº {count} está bem formatada")
        else:
            print(f"Linha nº {count} não está bem formatada")