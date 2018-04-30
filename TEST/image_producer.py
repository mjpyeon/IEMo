import requests
import numpy as np
from skimage import io
from skimage import color

def img_to_str(img):
    flattened_img = img.flatten()
    string_img = ''
    for number in flattened_img:
        string_img += (str(number) + ',')
    return string_img

def send_img(filename, content):
    img = io.imread(filename)
    row_dim = img.shape[0]
    column_dim = img.shape[1]
    string_img = img_to_str(img)
    data={'file_name':filename, 'image': string_img, 'content': content, 'row_dim' : row_dim, 'column_dim' : column_dim}
    requests.post("http://127.0.0.1:8000/Images/post/", data)

# MAIN
#send_img('test.jpg', 'Twitter Logo')
#send_img('insta.jpeg', 'Instagram Logo')
send_img('FacebookLogo.png', 'Facebook Logo')
