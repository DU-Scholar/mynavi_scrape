import Export
import unittest
import requests
from bs4 import BeautifulSoup


class ScrapeTest(unittest.TestCase):
    """
    url取得テスト
    """


    def test_URL取得(self):
        baseUrl = "https://job.mynavi.jp"
        urls = "/21/pc/search/corp244653/outline.html"
        res = requests.get(baseUrl + urls)
        soup = BeautifulSoup(res.content, 'html.parser')
        url = Export.getUrl(soup, "corpDescDtoListDescText120")
        self.assertEqual("http://www.plant-kikou.co.jp/", url)


if __name__ == '__main__':
    unittest.main()
