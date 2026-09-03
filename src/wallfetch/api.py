import requests

def getWallpaper(query, api_key=None):
    
    if api_key is not None:
        url = f"https://wallhaven.cc/api/v1/search?q={query}&apikey={api_key}"

        wallpaper_info = []

        res = requests.get(url)
        jsonData = res.json()
        
        for info in jsonData["data"]:
            wall_info = {}
            wall_info['id'] = info["id"]
            wall_info['url'] = info["path"]
            wall_info['filetype'] = info["file_type"].split("/")[1]

            wallpaper_info.append(wall_info)

        return wallpaper_info
    
    else:
        url = f"https://wallhaven.cc/api/v1/search?q={query}"

        wallpaper_info = []

        res = requests.get(url)
        jsonData = res.json()
        
        for info in jsonData["data"]:
            wall_info = {}
            wall_info['id'] = info["id"]
            wall_info['url'] = info["path"]
            wall_info['filetype'] = info["file_type"].split("/")[1]

            wallpaper_info.append(wall_info)

        return wallpaper_info

