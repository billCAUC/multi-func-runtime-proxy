with open('rsa.py', 'r', encoding='UTF-8') as f2:
    line = f2.readline()    # 读取第一行
    res = line
    while line is not None and line != '':
        print(line)
        line = f2.readline()    # 读取下一行
        res = res + line
        
print(repr(res))


