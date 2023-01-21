
# 2. D1
num_of_grains = 2 ** 64
wt = num_of_grains/7000
print(f"It would weigh {format(wt, ',.2f')} pounds")

# 2. D2
words_sz = 10 ** 18
down_speed = int(input("Enter the download speed in million bits per second: "))

time_reqd = words_sz / (down_speed * 1000000)
print("Time required for you to download all words ever spoken(in years): ", format(time_reqd/(3600*24*365), ',.2f'))

# 2. D3

## 800 x 600 resolutions
usb_sz = int(input("Enter the USB size (in GB): ")) * 1000000000

resolution = 800 * 600

gif_sz = (resolution) / 5
jpg_sz = (3 * resolution) / 25
png_sz = (3 * resolution) / 8
tiff_sz = 6 * resolution

print(f"You can store a max of {format(usb_sz/gif_sz, ',.2f')} of these GIFs in your USB")
print(f"You can store a max of {format(usb_sz/jpg_sz, ',.2f')} of these JPEGs in your USB")
print(f"You can store a max of {format(usb_sz/png_sz, ',.2f')} of these PNGs in your USB")
print(f"You can store a max of {format(usb_sz/tiff_sz, ',.2f')} of these TIFFs in your USB")


# 2. D4
age = float(input("Enter your age in years: "))
mins_in_yr = 365 * 24 * 60
breaths = (45 * mins_in_yr if age >= 1 else 45 * age * mins_in_yr) + (25 * 3 * mins_in_yr if age >= 3 else (25 * (age - 1) * mins_in_yr if age >= 1 else 0)) + (20 * 9 * mins_in_yr if age >= 14 else (20 * (age - 4) * mins_in_yr if age >= 1 else 0)) + (16 * (age-14) * mins_in_yr if age >= 15 else 0)
print(f"You have breathed approximately {format(breaths, ',.2f')} times since your birth")
heart_bts = 67.5 * age * mins_in_yr * 60
print(f"You have had approximately {format(heart_bts, ',.2f')} heartbeats since your birth")