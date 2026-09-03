from . import api
from . import downloader
import argparse
import sys
from . import config


class HelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog):
        super().__init__(
            prog,
            max_help_position=35,
            width=100,
        )

def main():
    parser = argparse.ArgumentParser(
        prog="wallfetch",
        description="Script to download wallpapers from Wallhave.cc",
        formatter_class=HelpFormatter
    )

    parser.add_argument("query", nargs="?", help="Search query for wallpapers")

    parser.add_argument(
        "-n", "--count", type=int, metavar="N", help="Number of wallpapers to download"
    )

    parser.add_argument(
        "-f",
        "--folder",
        metavar="FOLDER",
        default="~/Pictures/wallfetch",
        help="Download folder (uses ~/Picutes/wallfetch by default)",
    )

    parser.add_argument(
        "-s",
        "--sorting",
        choices=[
            "date_added",
            "relevance",
            "random",
            "views",
            "favorites",
            "toplist",
            "hot",
        ],
        metavar="SORT",
        help="Sort the wallpapers",
    )

    parser.add_argument(
        "-o",
        "--order",
        choices=["asc", "desc"],
        default="desc",
        help="Sorting order (default: desc)",
    )

    parser.add_argument(
        "-p",
        "--purity",
        choices=["100", "110", "111", "001", "011", "101", "010"],
        default="100",
        metavar="PURITY",
        help="SFW/Sketchy/NSFW filters"
    )

    parser.add_argument(
        "-c",
        "--categories",
        choices=["100", "110", "111", "001", "011", "101", "010"],
        default="111",
        metavar="CATS",
        help="General/Anime/People"
    )

    parser.add_argument(
        "--page",
        type=int,
        default=1,
        metavar="PAGE",
        help="Results page (default: 1)",
    )
    
    parser.add_argument(
            "--set-api-key",
            metavar="KEY",
            help="Wallhaven.cc API key"
    )

    parser.add_argument(
        "--config",
        action="store_true",
        help="Show wallfetch configuration",
    )

    if len(sys.argv) == 1:
        print("No arguments provided. Use 'wallfetch -h' for help.")
        return

    args = parser.parse_args()

    query = args.query
    download_folder = args.folder
    count = args.count
    sort = args.sorting
    order = args.order
    purity = args.purity
    categories = args.categories
    page = args.page

    if args.set_api_key is not None:
        api_key = input("Wallhaven API key: ")
        config.saveAPI_key(api_key)
        print("API ket saved")
        return

    if args.config:
        api_key = config.getAPI_key()

        if api_key is None:
            print("API key is not configured")
        else:
            print("API key configured")

        return

    if args.query is None:
        print("No arguments provided. Use 'wallfetch -h' for help.")
        return
    
    api_key = config.getAPI_key()

    wallpapers = api.getWallpaper(query, sort, order, purity, categories, page, api_key)

    for wallpaper in wallpapers[:count]:
        downloader.downloadWall(wallpaper, download_folder)


if __name__ == "__main__":
    main()
