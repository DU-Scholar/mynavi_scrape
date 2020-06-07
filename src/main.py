from src import scrape


url = 'https://job.mynavi.jp/21/pc/search/query.html?HR:27/func=PCTopQuickSearch'
urls = scrape.scrape(url)
scrape.makeData(urls)


