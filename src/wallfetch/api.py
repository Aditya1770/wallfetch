import requests


def getWallpaper(
    query,
    sorting="date_added",
    order="desc",
    purity="100",
    categories="111",
    page=1,
    api_key=None,
):

    url = "https://wallhaven.cc/api/v1/search"

    if query[:23] == "https://wallhaven.cc/w/":
        query = query[23:]
        url = f"https://wallhaven.cc/api/v1/w/{query}"

        parameters = {}
    else:
        parameters = {
            "q": query,
            "sorting": sorting,
            "order": order,
            "purity": purity,
            "categories": categories,
            "page": page,
        }

        if api_key is not None:
            parameters["apikey"] = api_key

    try:
        res = requests.get(url, params=parameters)
        res.raise_for_status()
        jsonData = res.json()
        
        data = jsonData["data"]

        if isinstance(data, dict):
            data = [data]
        
        wallpaper_info = []

        for info in data:
            wall_info = {
                "id": info["id"],
                "url": info["path"],
                "filetype": info["file_type"].split("/")[1],
            }

            wallpaper_info.append(wall_info)

        return wallpaper_info
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error {e}")
