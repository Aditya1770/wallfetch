import requests


def getWallpaper(
    query,
    sorting="date_added",
    order="desc",
    purity="100",
    categories="111",
    page=1,
    api_key=None
):

    url = "https://wallhaven.cc/api/v1/search"

    parameters = {
        "q": query,
        "sorting": sorting,
        "order": order,
        "purity": purity,
        "categories": categories,
        "page": page
    }

    if api_key is not None:
        parameters["apikey"] = api_key

    res = requests.get(url, params=parameters)
    res.raise_for_status()
    jsonData = res.json()

    wallpaper_info = []

    for info in jsonData["data"]:
        wall_info = {
            "id": info["id"],
            "url": info["path"],
            "filetype": info["file_type"].split("/")[1],
        }

        wallpaper_info.append(wall_info)

    return wallpaper_info
