# 2. D2

## Calculating an approximation of how long it would take someone to download
## a dataset of all words ever spoken

words_sz = 10 ** 18
down_speed = int(input("Enter the download speed in million bits per second: "))

time_reqd = words_sz / (down_speed * 1000000)
print("Time required for you to download all words ever spoken(in years): ", format(time_reqd/(3600*24*365), ',.2f'))
