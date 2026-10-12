S = 'python'
print(len(S))
print(S[0], S[1], S[-1])
print(S + '1', S * 2)

try:
    S[0] = 'Z'
except TypeError as e:
    print("Error:", e)
S1 = 'Z' + S[1:]
print("S:%s, S1:%s" % (S, S1))

print(S.split('h'))
print(S.replace('py', 'PY'))
print(S.upper())
print('PYTHON'.lower())
print(' '.join(['life', 'is', 'short']))
hw12 = '%s %s %d' % ('hello', 'world', 12)
print(hw12)