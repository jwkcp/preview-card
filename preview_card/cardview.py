import re
import enum
import requests
from abc import *
from urllib.parse import urlparse, parse_qs

from bs4 import BeautifulSoup
from requests import HTTPError


class MediaSourceType(enum.Enum):
    NONE = 0
    ARTICLE = 1
    YOUTUBE = 2


class CardViewInfo:
    def __init__(self, ms_type=MediaSourceType.NONE, url="", image_url="", title="", description=""):
        self.__ms_type = ms_type
        self.__url = url
        self.__image_url = image_url
        self.__title = title
        self.__description = description
        self.__error = ""

    @property
    def ms_type(self):
        return self.__ms_type

    @ms_type.setter
    def ms_type(self, new_ms_type):
        self.__ms_type = new_ms_type

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_url):
        self.__url = new_url

    @property
    def image_url(self):
        return self.__image_url

    @image_url.setter
    def image_url(self, new_image_url):
        self.__image_url = new_image_url

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @property
    def error(self):
        return self.__error

    @error.setter
    def error(self, new_error):
        self.__error = new_error

    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(
            "--------------------------------------------------------------------------------------------------------",
            "ms_type\t\t{}".format(self.__ms_type),
            "url\t\t\t{}".format(self.__url),
            "image_url\t{}".format(self.__image_url),
            "title\t\t{}".format(self.__title),
            "desc\t\t{}".format(self.__description),
            "error\t\t{}".format(self.__error),
            "--------------------------------------------------------------------------------------------------------"
        )


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
        Comments:
        - This code copied from one of replies in stackoverflow.com
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


YOUTUBE_HOSTS = ['youtu.be', 'www.youtube.com', 'youtube.com']


def __extract_url_from_text(plain_text):
    """
    Extract the first occurence URL in a plain text
    """

    if plain_text:
        results = re.findall(r'(https?://[^\s]+)', plain_text)

        if results and len(results) > 0:
            return results[0]
        else:
            return ""
    else:
        return ""


def __get_card_view_info(url):
    """
    Extract MEDIA TYPE
    :return:
    """
    if url:
        query = urlparse(url)
        if query.hostname in YOUTUBE_HOSTS:
            mediasource = _Youtube(url)
        else:
            mediasource = _Article(url)

        return mediasource.get_data()
    else:
        return None


def get_data(plain_text=""):
    """
    Extracts and returns the information that a URL contains from plain text
    :param plain_text:
    :return:
    """
    if not plain_text:
        raise ValueError('The parameter passed is not valid.')

    url = __extract_url_from_text(plain_text)
    return __get_card_view_info(url)
