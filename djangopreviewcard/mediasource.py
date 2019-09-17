import requests

from abc import *
from urllib.parse import urlparse, parse_qs

from bs4 import BeautifulSoup
from requests import HTTPError

from .cardviewinfo import CardViewInfo
from .mediasourcetype import MediaSourceType


class _AbstractMediaSource(metaclass=ABCMeta):
    def __init__(self):
        self.cardviewinfo = CardViewInfo()

    @abstractmethod
    def get_data(self):
        raise NotImplementedError()


class _Youtube(_AbstractMediaSource):
    def __init__(self, url):
        super(_Youtube, self).__init__()
        self.__url = url

    def __get_video_id(self):
        """
        Examples:
        - http://youtu.be/SA2iWivDJiE
        - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
        - http://www.youtube.com/embed/SA2iWivDJiE
        - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
        """
        query = urlparse(self.__url)
        if query.hostname == 'youtu.be':
            return query.path[1:]
        if query.hostname in ('www.youtube.com', 'youtube.com'):
            if query.path == '/watch':
                p = parse_qs(query.query)
                return p['v'][0]
            if query.path[:7] == '/embed/':
                return query.path.split('/')[2]
            if query.path[:3] == '/v/':
                return query.path.split('/')[2]
        return ""

    def get_data(self):
        video_id = self.__get_video_id()
        self.cardviewinfo.url = "https://www.youtube.com/embed/{}".format(video_id)
        self.cardviewinfo.ms_type = MediaSourceType.YOUTUBE

        return self.cardviewinfo


class _Article(_AbstractMediaSource):
    def __init__(self, url):
        super(_Article, self).__init__()
        self.__url = url

    def get_data(self):
        self.cardviewinfo.url = self.__url

        try:
            res = requests.get(self.__url, timeout=3)

            if not res.status_code == 200:
                raise HTTPError('The response status code for the request is not 200')

            html = res.text
            soup = BeautifulSoup(html, 'html.parser')

            # Extract featured image
            image_soup = soup.find(property="og:image")
            image_url = image_soup['content']

            # Extract title
            title_soup = soup.find(property="og:title")
            title = title_soup['content']

            # Extract description
            desc_soup = soup.find(property="og:description")
            desc = desc_soup['content']

            self.cardviewinfo.image_url = image_url
            self.cardviewinfo.title = title
            self.cardviewinfo.description = desc
            self.cardviewinfo.ms_type = MediaSourceType.ARTICLE
        except Exception as e:
            self.cardviewinfo.error = e

        return self.cardviewinfo
