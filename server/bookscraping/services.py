from .models import YakabooStore, BookYeStore


class StoreManager:
    __services = [YakabooStore('https://www.yakaboo.ua/ua/search/?multi=0&cat=&q=', 'yakaboo'),
                  BookYeStore('https://book-ye.com.ua/search/index.php?q=', 'bookye'),
                  ]

    async def __fetch(self, url, session):



    async def get_book_info(self):
        urls = [service.url for service in self.__services]
        html_body = ""
        async with
