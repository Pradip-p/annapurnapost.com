import os
import pathlib
import shutil
# import time
from io import BytesIO

import gc
import requests
from PIL import Image

def process_image_instagram(image_url, username):
    if image_url == '':
        return ''
    try:

        env = os.environ.get('APP_ENV', 'dev')
        if env.lower() == 'prd':
            base_image_path = '/home/grepsr/data/20190717-instagram/'
        else:
            base_image_path = '/home/amit/Desktop/20190717-instagram/'
        user_path = base_image_path + username + '/'

        # getting image name form image path
        image_name = image_url.split('?')[0].split('/')[-1]
        # ipdb.set_trace()
        # image_name = image_url.split('/')[-1]
        image_path = user_path + image_name
        pathlib.Path(user_path).mkdir(parents=True, exist_ok=True)
        # del image_name
        del user_path

        image_formats = ("image/png", "image/jpeg", "image/jpg")

        im = ''
        if not os.path.isfile(image_path):
            r = requests.get(image_url, stream=True)
            if r.headers["content-type"] in image_formats:  # if  The given data is image then
                # 1. check if it is already downloaded.if no, download
                # 2.  Get image dimension
                # 3. return (image_urls seperated by pipe,image_local_path_seperated_by_pipe,image dimension seperated by path)

                with open(image_path, 'wb') as out_file:
                    shutil.copyfileobj(r.raw, out_file)
                    del out_file

                im = Image.open(image_path)

                del r
            else:
                del r
                return ''
        else:
            print('Already downloaded', image_path)
            # input()
            im = Image.open(image_path)
        if im != '':
            size = im.size
            del im
            gc.collect()
            dimension = '*'.join([str(size[0]), str(size[1])])
            return dimension, username + '/' + image_name, image_url
        del im
        gc.collect()
    except:
        return ''
