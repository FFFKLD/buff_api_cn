# Buff API CN

An unofficial Python API wrapper for Buff163, with Chinese language support.

This is a fork/modification of the original [buff163-unofficial-api](https://github.com/markzhdan/buff163-unofficial-api) by markzhdan.

## Key Changes
- Added `lang=zh-CN` to API requests to fetch data in Chinese.
- Renamed the main class to `BuffApiCn`.

## Installation

You can install this package from your GitHub repository:
```sh
pip install git+https://github.com/your_github/buff_api_cn.git
```

## Usage

```python
from buff_api_cn import BuffApiCn

# Example cookie format
cookie = "your_full_cookie_string"

buff_api = BuffApiCn(session_cookie=cookie)

market = buff_api.get_featured_market()

for item in market:
    print(f"{item.market_hash_name}")
    print(f"¥ {item.sell_min_price}\n")
