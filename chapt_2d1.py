# 2. D1

## Calculating the number of grains of rice
## you'd have if you started with 1 and doubled for each square on a chess board

num_of_grains = 2 ** 64
wt = num_of_grains/7000
print(f"It would weigh {format(wt, ',.2f')} pounds")
