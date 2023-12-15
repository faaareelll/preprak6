from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan Pillow
image = Image.open(r"C:\Users\faaareell\Downloads\Programs\P.Fungsional\m6\preprak6\3.jpg")

# TODO 2: Ubah Tingkat kecerahan dan kontras
brightness_factor = 5
contrast_factor = 1.2

enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(brightness_factor)

enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(contrast_factor)

# TODO 3: Simpan gambar
final_image.save("brightness_contrast_image.jpg")

# TODO 4: Tampilkan
final_image.show()
