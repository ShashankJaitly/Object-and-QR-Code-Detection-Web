import qrcode
from MyQR import myqr
import os
import base64


for i in range(0,len(lines)):
    data = lines[i].encode() # To encode
    print(data)
    name = base64.b64encode(data)
    print(name)
    version,level,qr_name = myqr.run(str(name),
                                 level='H',
                                 version = 2,
                                 picture = 'bg.jpg', # Background Image
                                 colorized=True,
                                 contrast = 1.0,
                                 brightness = 1.0,
                                 save_name = str(lines[i]+'.bmp'), #.bmp for jpg format and save_name depicts with which name the qr code is to be saved
                                 save_dir = os.getcwd() # getcwd == current working directory
                                )

for i in lines:
    qr = qrcode.make('{}'.format(i))
    qr.save('{}.png'.format(i))



