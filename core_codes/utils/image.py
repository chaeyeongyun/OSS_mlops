from PIL import Image

def width_height(f):
    img = Image.open(f)
    w, h = img.size
    return {"width":w, "height":h}