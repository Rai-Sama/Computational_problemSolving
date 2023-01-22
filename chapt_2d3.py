# 2. D3
## Calculating the number of media files of diff formats that 
## a USB can hold given the resolution of 800 x 600 for each and the respective compression ratios

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