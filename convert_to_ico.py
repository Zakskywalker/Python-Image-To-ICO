from PIL import Image, ImageChops, ImageEnhance, ImageFilter

source_path = r""
output_path = r""

img = Image.open(source_path).convert("RGBA")
alpha = img.getchannel("A")
bbox = alpha.getbbox()
if bbox is None:
	raise ValueError("The source image has no visible pixels")

padding = 32
left, top, right, bottom = bbox
crop_box = (
	max(0, left - padding),
	max(0, top - padding),
	min(img.width, right + padding),
	min(img.height, bottom + padding),
)
img = img.crop(crop_box)
canvas_size = max(img.size)
square = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
square.paste(img, ((canvas_size - img.width) // 2, (canvas_size - img.height) // 2))
img = square

# Make the silhouette readable on both light and dark desktop backgrounds.
alpha = img.getchannel("A")
outline_alpha = ImageChops.subtract(
	alpha.filter(ImageFilter.MaxFilter(25)), alpha
)
outline = Image.new("RGBA", img.size, (255, 255, 255, 0))
outline.putalpha(outline_alpha.point(lambda value: min(230, value)))
img = Image.alpha_composite(outline, img)
img = ImageEnhance.Contrast(img).enhance(1.15)
img = ImageEnhance.Color(img).enhance(1.1)

img.save(
	output_path,
	format="ICO",
	sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
)
