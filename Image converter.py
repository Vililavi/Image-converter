from PIL import Image
import glob

PATH = 'path'

for filename in glob.glob(PATH + '*.tif'): #assuming tif
    im = Image.open(filename)
    rgb_im = im.convert('RGB')
    rgb_im.save(str(filename) + '.jpg')
    print(str(filename)+'.jpg is ready')

print('Convertion is ready')
