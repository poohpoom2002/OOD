print('*** Converting hh.mm.ss to seconds ***')
h, m, s = [x for x in input("Enter hh mm ss : ").split()]
if(int(m) < 0  or int(m) >= 60):
    print(f'mm({m}) is invalid!')
elif(int(s) < 0 or int(s) >= 60):
    print(f'ss({s}) is invalid!')
else:
    if(int(h) < 10):
        h = '0' + h
    if(int(m) < 10):
        m = '0' + m
    if(int(s) < 10):
        s = '0' + s
    ans = str(int(h)*3600+int(m)*60+int(s))
    ans_with_commas = "{:,}".format(int(ans))
    print(h, ':', m, ':', s, sep = '', end = '')
    print(' =', ans_with_commas, 'seconds')