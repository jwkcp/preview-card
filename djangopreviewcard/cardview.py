import re
from urllib.parse import urlparse

from .mediasource import _Youtube, _Article


class CardView:
    YOUTUBE_HOSTS = ['youtu.be', 'www.youtube.com', 'youtube.com']

    def __init__(self, plain_text=""):
        self.__plain_text = plain_text

    def __extract_url_from_text(self):
        """
        Extract the first occurence URL in a plain text
        """

        if self.__plain_text:
            results = re.findall(r'(https?://[^\s]+)', self.__plain_text)

            if results and len(results) > 0:
                return results[0]
            else:
                return ""
        else:
            return ""

    def __get_card_view_info(self, url):
        """
        Extract MEDIA TYPE
        :return:
        """
        if url:
            query = urlparse(url)
            if query.hostname in self.YOUTUBE_HOSTS:
                mediasource = _Youtube(url)
            else:
                mediasource = _Article(url)

            return mediasource.get_data()
        else:
            return None

    def get_data(self, plain_text=""):
        if plain_text:
            self.__plain_text = plain_text

        if not self.__plain_text:
            raise ValueError('The parameter passwd is not valid.')

        url = self.__extract_url_from_text()
        return self.__get_card_view_info(url)
