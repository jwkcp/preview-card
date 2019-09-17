import unittest
from time import sleep

from djangopreviewcard.cardview import CardView


class TestCardView(unittest.TestCase):
    # def setUp(self):
    #     pass

    def test_article_ko_with_url_blank_nodata(self):
        str = "가나다라마바사 http://naver.com 안녕하세요1"
        cardview = CardView(str)
        result = cardview.get_data()
        print(result)

    def test_article_ko_with_url_nodata(self):
        str = "가나다라마바사http://naver.com안녕하세요2"
        cardview = CardView(str)
        result = cardview.get_data(str)
        print(result)

    def test_article_ko_with_url_blank_data(self):
        str = "가나다라마바사 https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=008&aid=0004279021 하세요1"
        cardview = CardView(str)
        result = cardview.get_data()
        print(result)

    def test_article_ko_with_url_data(self):
        str = "가나다라마바사https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=008&aid=0004279021하세요2"
        cardview = CardView(str)
        result = cardview.get_data(str)
        print(result)

    def test_youtube_type_1(self):
        str = "가나다라 https://www.youtube.com/watch?v=Jzz4AEIddzY 하하하하"
        cardview = CardView(str)
        result = cardview.get_data()
        print(result)

    def test_youtube_type_2(self):
        str = "가나다라 https://youtu.be/Jzz4AEIddzY 하하하하"
        cardview = CardView(str)
        result = cardview.get_data()
        print(result)


if __name__ == '__main__':
    unittest.main()
