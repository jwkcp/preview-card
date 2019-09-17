from .mediasourcetype import MediaSourceType


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

