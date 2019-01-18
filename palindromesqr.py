"""
ID: pradyungn
LANG: PYTHON3
TASK: palsquare
"""
def toBase(n, b):
    l = 0
    result = []
    while n >= b**l:
        l += 1

    for i in reversed(range(l)):
        d = n // (b**i)
        if d < 10:
            d = str(d)
        else:
            d = chr(ord('A')+d-10)
        result.append(d)
        n %= (b**i)

    return ''.join(result)


with open('palsquare.in','r') as fin:
    B = int(fin.readline())

with open('palsquare.out','w') as fout:
    for n in range(1,301):
        #print('n', n, 'bn', toBase(n,B))

        bsq = toBase(n**2, B)
        if bsq[::-1] == bsq:
            bn = toBase(n, B)
            fout.write(bn + ' ' + bsq + '\n')

