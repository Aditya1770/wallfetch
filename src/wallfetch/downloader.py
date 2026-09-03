from pathlib import Path
import requests
from rich.progress import Progress

def downloadWall(wallpaper_info, download_folder="~/Pictures/wallfetch/"):
    
    download_folder = Path(download_folder).expanduser()
    
    download_folder.mkdir(parents=True, exist_ok=True)

    wall_id = wallpaper_info['id']
    wall_url = wallpaper_info['url']
    filetype = wallpaper_info['filetype']

    res = requests.get(wall_url, stream=True)
    res.raise_for_status()

    block_size = 64 * 1024

    filename = f"{wall_id}.{filetype}"
    path = download_folder / filename

    total_size = int(res.headers.get("content-length", 0))

    with path.open(mode='wb') as file, Progress() as progress:
        task = progress.add_task(f"[green]{filename}", total=total_size)
        for data in res.iter_content(block_size):
            file.write(data)
            progress.update(task, advance=len(data))
