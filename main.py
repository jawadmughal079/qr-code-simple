# first install module pip install qrcode[pil]

#pil is module for get the images and save the link into images for qr code 


#then import module qr code


# you can assign th name of qr code like companyNameqr  by using alias name [ as enter the name you want to give ]
# like qrcode as MughalJawadQrCode

#then save the link into images tag =qrcode.make()
# make is use for create the link of code 

# image.save()-> this is use for save the qr code by name you want to give the name of qr code






import qrcode

img = qrcode.make('https://www.w3schools.com/python/python_functions.asp#gsc.tab=0')
img.save('how to make qr code in python .png')