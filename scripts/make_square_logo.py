from PIL import Image
import os

def make_square_logo(src_path, dest_path, size=512, bg=(0,0,0,0)):
    img = Image.open(src_path).convert("RGBA")
    # compute scale to fit inside size
    w, h = img.size
    scale = min(size / w, size / h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    img = img.resize((new_w, new_h), Image.LANCZOS)

    # create square background
    square = Image.new("RGBA", (size, size), bg)
    offset = ((size - new_w) // 2, (size - new_h) // 2)
    square.paste(img, offset, img)
    # ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    square.save(dest_path)

if __name__ == '__main__':
    src = os.path.join(os.path.dirname(__file__), '..', 'assets', 'img', 'FITPRO branco.png')
    src = os.path.normpath(src)
    dest = os.path.join(os.path.dirname(__file__), '..', 'assets', 'img', 'fitpro-square-512.png')
    dest = os.path.normpath(dest)
    make_square_logo(src, dest)
    print('Saved:', dest)
