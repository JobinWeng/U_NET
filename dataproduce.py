import os
from readdcm import dcmtopng
from PIL import Image

pationts_sir = r'G:\U_NET\ALL_DATA'
pationts = os.listdir(pationts_sir)
count1 = 0
count2 = 0
for pationt in pationts:
 dirs = os.listdir(os.path.join(pationts_sir,pationt))
 for dir in dirs:
  datasets = os.listdir(os.path.join(os.path.join(pationts_sir,pationt),dir))
  for data in datasets:
   filepath = os.path.join(os.path.join(os.path.join(pationts_sir,pationt),dir),data)
   if data.split('.')[1] == 'dcm':
       dcmtopng(filepath,r'G:\U_NET\data',str(count1)+'.png')
       count1 += 1
   elif data.split('.')[1] == 'png':
    image = Image.open(filepath)
    image.save(os.path.join(r'G:\U_NET\label',str(count2)+'.png'))
    count2 += 1