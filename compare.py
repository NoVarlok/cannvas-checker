from PIL import Image
import os

this_directory = r"C:\Users\admin\Desktop\не забыть\canvas\download\note_firefox"
this_pack = os.listdir(this_directory)
this_pack.remove("config.txt")
note_directory = r"C:\Users\admin\Desktop\не забыть\canvas\download\this_firefox"
note_pack = os.listdir(note_directory)
note_pack.remove("config.txt")

sorted(this_pack)
sorted(note_pack)

for canvas_name in this_pack:
    this_image = Image.open(this_directory + "\\" + canvas_name)
    this_pixel = this_image.load()
    note_image = Image.open(note_directory + "\\" + canvas_name)
    note_pixel = note_image.load()

    if this_image.size[0] != note_image.size[0] or this_image.size[1] != note_image.size[1]:
        print('different sizes')
        exit(1)
    width, height = this_image.size
    base_color = (0, 0, 0)
    color_black = (0, 0, 0)
    color_white = (255, 255, 255)
    result_image = Image.new("RGB", (width, height), color_white)
    result_pixel = result_image.load()

    for j in range(height):
        for i in range(width):
            if this_pixel[i, j] != note_pixel[i, j]:
                result_pixel[i, j] = (0, 0, 0)
            else:
                result_pixel[i, j] = (255, 255, 255)
    result_image.save("comparation_" + canvas_name, "JPEG")
