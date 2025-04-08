import os, sys
from PIL import Image

size = 640, 480

for infile in os.listdir("./AGH_Pictures/"):
    outfile = "./resized/" + os.path.basename(infile)
    im = Image.open('./AGH_Pictures/' + infile)
    im.thumbnail(size, Image.Resampling.LANCZOS)
    im.save(outfile, "JPEG")
