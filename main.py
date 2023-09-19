import requests
import json
from bs4 import BeautifulSoup
import urllib
import os


def download_soundvery(index: int = 0, save_folder: str = "./Code"):
    """ 下载声谷白噪音文件

    Args:
        index (int, optional): _description_. Defaults to 0.
        save_folder (str, optional): 默认保存文件夹位置. Defaults to "./Code".
    """
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    data = {
        'lbyeshu': index
    }
    url = 'https://www.soundvery.com/Ajax/AudioHandler.ashx'
    res = requests.post(url, data=data)
    res.encoding = 'utf-8'
    res_data = res.text
    bs_data = json.loads(res_data)['code']
    bs_info = BeautifulSoup(bs_data, 'lxml')
    audio_info_list = bs_info.find_all('audio')
    img_src_list = bs_info.find_all('img')
    name_list = []
    for img_src in img_src_list:
        print(img_src.get('alt'))
        name_list.append(img_src.get('alt'))
    for index_, audio_info in enumerate(audio_info_list):
        print(audio_info.get('src'))
        urllib.request.urlretrieve(
            f"https://www.soundvery.com{audio_info.get('src')}", f"{save_folder}/{name_list[index_]}.mp3")
        print(f"已下载路径:{save_folder}/{name_list[index_]}.mp3")


if __name__ == '__main__':
    for index in range(0, 100):
        download_soundvery(index)
