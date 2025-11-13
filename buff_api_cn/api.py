import logging
from typing import Iterator, Callable, Union
from .rest_adapter import RestAdapter
from .models import *
from .cs_enums import *


class BuffApiCn:
    def __init__(
        self,
        hostname: str = "buff.163.com/api",
        session_cookie: str = "",
        ssl_verify: bool = True,
        logger: logging.Logger = None,
        page_size: int = 20,
    ):
        self._rest_adapter = RestAdapter(hostname, session_cookie, ssl_verify, logger)
        self._page_size = page_size

    def get_featured_market_item(self) -> Item:
        return self.get_featured_market()[0]

    def get_featured_market(self, pageNum: int = 1) -> List[Item]:
        result = self._rest_adapter.get(
            endpoint=f"/market/goods?game=csgo&lang=zh-CN&page_num={pageNum}"
        )
        market = [Item(**item) for item in result.data["data"]["items"]]
        return market

    def get_item_market(
        self,
        category: Union[Knife, Gun, Glove, Agent, Sticker, OtherItem],
        pageNum: int = 1,
    ) -> List[Item]:
        if not isinstance(category, Enum):
            raise TypeError("Category must be an instance of an Enum.")

        result = self._rest_adapter.get(
            endpoint=f"/market/goods?game=csgo&lang=zh-CN&page_num={pageNum}&category={category.value}"
        )

        market = [Item(**item) for item in result.data["data"]["items"]]
        return market

    def fetch_image_data(self, item: Item):
        item.data = self._rest_adapter.fetch_data(url=item.goods_info.icon_url)

    def _page(
        self, endpoint: str, model: Callable[..., Model], max_amt: int = 80
    ) -> Iterator[Model]:
        amt_yielded = 0
        curr_page = last_page = 1
        ep_params = {
            "game": "csgo",
            "lang": "zh-CN",
            "page_size": self._page_size,
        }

        while curr_page <= last_page:
            ep_params["page_num"] = curr_page
            result = self._rest_adapter.get(endpoint=endpoint, ep_params=ep_params)
            data = result.data["data"]

            last_page = data["total_page"]
            curr_page = data["page_num"] + 1
            for datam in data["items"]:
                yield model(**datam)
                amt_yielded += 1
                if amt_yielded >= max_amt:
                    last_page = 0
                    break

    def get_featured_market_paged(self, max_amt: int = 80) -> Iterator[Item]:
        return self._page(endpoint="/market/goods", model=Item, max_amt=max_amt)

    def get_item(self, item_id: int) -> SpecificItem:
        result = self._rest_adapter.get(
            endpoint=f"/market/goods/info?game=csgo&lang=zh-CN&goods_id={item_id}"
        )

        return SpecificItem(**result.data["data"])

    def search_item(self, text: str, page_num: int = 1) -> List[Item]:
        result = self._rest_adapter.get(
            endpoint=f"/market/search/suggest?game=csgo&text={text}&page_num={page_num}"
        )
        market = [Item(**item) for item in result.data["data"]["items"]]
        return market
