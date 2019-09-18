import unittest

from preview_card import cardview, MediaSourceType


class TestCardView(unittest.TestCase):
    def test_article_ko_with_url_blank_nodata(self):
        str = "가나다라마바사 http://naver.com 안녕하세요1"
        result = cardview.get_data(str)

        self.assertEqual(result.ms_type, MediaSourceType.ARTICLE)

        print(result)

    def test_article_ko_with_url_nodata(self):
        str = "가나다라마바사http://naver.com안녕하세요2"
        result = cardview.get_data(str)
        print(result)

    def test_article_ko_with_url_blank_data(self):
        str = "가나다라마바사 https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=008&aid=0004279021 하세요1"
        result = cardview.get_data(str)

        self.assertEqual(result.ms_type, MediaSourceType.ARTICLE)

        print(result)

    def test_article_ko_with_url_data(self):
        str = "가나다라마바사https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=008&aid=0004279021하세요2"
        result = cardview.get_data(str)
        print(result)

    def test_article_en_with_url_blank_nodata(self):
        str = "가나다라마바사 https://www.nytimes.com 안녕하세요1"
        result = cardview.get_data(str)
        print(result)

    def test_article_en_with_url_nodata(self):
        str = "가나다라마바사https://www.nytimes.com안녕하세요2"
        result = cardview.get_data(str)
        print(result)

    def test_article_en_with_url_blank_data(self):
        str = "가나다라마바사 https://www.nytimes.com/2019/09/17/technology/personaltech/iphone-11-review.html 하세요1"
        result = cardview.get_data(str)

        self.assertEqual(result.ms_type, MediaSourceType.ARTICLE)

        print(result)

    def test_article_en_with_url_data(self):
        str = "가나다라마바사https://www.nytimes.com/2019/09/17/technology/personaltech/iphone-11-review.html하세요2"
        result = cardview.get_data(str)
        print(result)

    def test_youtube_type_1(self):
        str = "가나다라 https://www.youtube.com/watch?v=Jzz4AEIddzY 하하하하"
        result = cardview.get_data(str)

        self.assertEqual(result.ms_type, MediaSourceType.YOUTUBE)

        print(result)

    def test_youtube_type_2(self):
        str = "가나다라 https://youtu.be/Jzz4AEIddzY 하하하하"
        result = cardview.get_data(str)

        self.assertEqual(result.ms_type, MediaSourceType.YOUTUBE)

        print(result)


if __name__ == '__main__':
    unittest.main()
