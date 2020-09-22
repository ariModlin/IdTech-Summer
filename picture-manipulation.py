from PIL import Image

img = Image.open("./images/black.bmp")
pixels = img.load()
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

div = img.height // len(colors)

for c in range(len(colors)):
	start = c * div
	end = start + div
	for y in range(start, end):
		for x in range(img.width):
			pixels[x, y] = colors[c]

img.save("./images/test.bmp")