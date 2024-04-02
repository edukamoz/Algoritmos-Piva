f1 = 1
f2 = 1
fn = 0
qnt = 1

print(f'{f1}\n{f2}')
# Comando for
for i in range(1, 9):
    fn = f1 + f2
    f1 = f2
    f2 = fn
    print(fn)

# Comando while
while qnt < 9:
    fn = f1 + f2
    f1 = f2
    f2 = fn
    print(fn)
    qnt += 1
