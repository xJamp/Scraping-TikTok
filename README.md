# [Tikotk](https://www.tiktok.com/) Scraping

## With the module you can:
1. [search ](#1-search)
2. [trends](#2-trends)
3. [user info ](#3-user-info)
4. [user videos](#4-user-videos)


- - -
## Tecnologies
- [requests] - send the requests
- [json] - load objects
- - -
## Uso
```sh
from TikTok import Tiktok
Object = Tiktok()
```
# `1. search`
- keyword: string - required - this keyword search.

```sh
Object.search(keyword = 'charlie')
```
# `2. trends`
- not have params.

```sh
Object.trends()
```
# `3. user info`
- username: string - required - with this username get info.

```sh
Object.user_info(username = 'celessalas')
```
# `4. user videos`
- username: string - required - with this username get videos.

```sh
Object.user_videos(username = 'celessalas')
```

## License

MIT


   [requests]: <https://docs.python-requests.org/en/master/>
   [json]: <https://docs.python.org/3/library/json.html>
