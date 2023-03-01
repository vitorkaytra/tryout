h_pulo = int(input('altura do pulo: '))
n_canos = int(input('numero de canos: '))

h_canos = []

for i in range(n_canos):
    h_canos.append(int(input('alturas: ')))

print(h_canos)

i = 0
if h_canos[i+1] - h_canos[i] > h_pulo:
    print('game over')
else:
    print('you win')