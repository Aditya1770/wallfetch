import api
import downloader
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Script to download wallpapers from Wallhave.cc"
        )

    parser.add_argument(
            "query",
            help="Search query for wallpapers"
            )

    parser.add_argument(
            "-f",
            "--folder",
            metavar="FOLDER",
            default="~/Pictures/wallfetch",
            help="Specify a custom download folder (uses ~/Picutes/wallfetch by default)"
            )

    args = parser.parse_args()

    query = args.query
    download_folder = args.folder 

    wallpapers = api.getWallpaper(query)

    for wallpaper in wallpapers:
        downloader.downloadWall(wallpaper, download_folder)
    

if __name__ == "__main__":
    main()
