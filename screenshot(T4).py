'''first install pyscreenshot pakage by
pip install pyscreenshot
'''


import pyscreenshot 

image = pyscreenshot.grab() 
image.show() 
image.save("Vineet.png") 
