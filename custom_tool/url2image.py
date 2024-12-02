import locale
import os
import time
import requests
import torch
import urllib3
import ssl
from PIL import Image, ImageOps, ImageSequence
import numpy as np
import subprocess
from PIL import Image, ImageSequence, ImageOps

class URL2IMG:
    def __init__(self):
        self.img_path = None
        self.img_data = None

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "url": ("STRING", {}),
                "file_name": ("STRING", {}),
                "is_enable": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING","IMAGE", "STRING",)
    RETURN_NAMES = ("file_path","img", "log",)

    FUNCTION = "url_to_img"
    CATEGORY = "大模型派对（llm_party）/转换器（converter）"


    def url_to_img(self, url, file_name=None, is_enable=True):
        if not is_enable:
            return (self.img_path, self.img_data, "Function is disabled")
        if url is None or "http" not in url:
            return (None, None, "URL is None")

        # 使用 aria2c 进行多线程下载
        try:
            # 构建img_temp目录路径
            current_dir = os.path.dirname(os.path.abspath(__file__))
            img_temp_dir = os.path.join(current_dir, 'img_temp')
            os.makedirs(img_temp_dir, exist_ok=True)

            # 时间戳
            timestamp = int(time.time())
            if file_name is None:
                img_path = os.path.join(img_temp_dir, f'image-{timestamp}.tmp')
            else:
                img_path = os.path.join(img_temp_dir, f'{file_name}-{timestamp}.tmp')

            cmd = [
                "aria2c", "-o", os.path.basename(img_path), "-x","16", "-s","16", url,"-d", img_temp_dir
            ]
            subprocess.run(cmd, check=True)

        except subprocess.CalledProcessError as e:
            return (None, None, f"Failed to download image: {str(e)}")

        # 检查图片格式并打开
        try:
            img = Image.open(img_path)
            img_out = []
            for frame in ImageSequence.Iterator(img):
                frame = ImageOps.exif_transpose(frame)
                if frame.mode == "I":
                    frame = frame.point(lambda i: i * (1 / 256)).convert("L")
                image = frame.convert("RGB")
                image = np.array(image).astype(np.float32) / 255.0
                image = torch.from_numpy(image).unsqueeze(0)
                img_out.append(image)
            img_out = img_out[0]
            self.img_path = img_path
            self.img_data = img_out

            return (img_path, img_out, f"Image file saved as {img_path}")

        except Exception as e:
            return (None, None, f"Failed to process image: {str(e)}")


    @classmethod
    def IS_CHANGED(cls,file_name=None,url=None,is_enable=True):
        current_time=time.time()
        return str(current_time) 

NODE_CLASS_MAPPINGS = {
    "URL2IMG": URL2IMG,
}
lang = locale.getdefaultlocale()[0]
import os
import sys
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(current_dir, "config.ini")
import configparser
config = configparser.ConfigParser()
config.read(config_path)
try:
    language = config.get("API_KEYS", "language")
except:
    language = ""
if language == "zh_CN" or language=="en_US":
    lang=language
if lang == "zh_CN":
    NODE_DISPLAY_NAME_MAPPINGS = {
        "URL2IMG": "下载图片🐶"
    }
else:
    NODE_DISPLAY_NAME_MAPPINGS = {
        "URL2IMG": "URL 2 IMG🐶"
    }
