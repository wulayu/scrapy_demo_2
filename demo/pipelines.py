import openpyxl
from demo.items import MovieItem


class MovieItemPipeline:

    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.title = 'market'
        self.sheet.append(('序号', '名称', '价格', '颜色', '尺寸', '网站货号', '详情', '大图url'))

    def process_item(self, item: MovieItem, spider):
        self.sheet.append(
            (item['num'], item['title'], item['price'], item['color'], item['size'], item['sku'], item['details'],
             item['img_urls']))
        return item

    def close_spider(self, spider):
        self.wb.save('zappos.xlsx')
