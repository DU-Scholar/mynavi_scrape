from src import scrape


def getOsakaData():
    # 大阪のデータ100件取得
    url = 'https://job.mynavi.jp/21/pc/search/query.html?HR:27/func=PCTopQuickSearch'
    urls = scrape.scrape(url)
    scrape.makeData(urls, '../data/data.csv')


def getHyogoData():
    # 兵庫のデータ100件取得
    url = 'https://job.mynavi.jp/21/pc/search/query.html?HR:28/func=PCTopQuickSearch'
    urls = scrape.scrape(url)
    scrape.makeData(urls, '../data/data2.csv')


getHyogoData()