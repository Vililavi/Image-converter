from PIL import Image
import glob

for filename in glob.glob('C:/Users/lavik/Downloads/tmp - Copy/*.tif'): #assuming tif
    im = Image.open(filename)
    rgb_im = im.convert('RGB')
    rgb_im.save(str(filename) + '.jpg')
    print(str(filename)+'.jpg is ready')
