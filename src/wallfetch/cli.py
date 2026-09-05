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


def parse_pages(value):
    if ":" in value:
        start, end = map(int, value.split(":", 1))

        if start < 1 or end < 1:
            raise argparse.ArgumentTypeError("Pages must be greater than 0")
        if start > end:
            raise argparse.ArgumentTypeError("Start page cannot be greater than end page")

        return range(start, end+1)

def main():

    defaults = config.getDefaults()
    # print(defaults)

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
        default=defaults["folder"],
        help="Download folder",
    )

    parser.add_argument(
            "--set-folder",
            metavar="DEF_FOLDER",
            help="Set default download folder",
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
        default=defaults["sorting"],
        metavar="SORT",
        help="Sort the wallpapers",
    )

    parser.add_argument(
        "-o",
        "--order",
        choices=["asc", "desc"],
        default=defaults["order"],
        help="Sorting order (default: desc)",
    )

    parser.add_argument(
        "-p",
        "--purity",
        choices=["100", "110", "111", "001", "011", "101", "010"],
        default=defaults["purity"],
        metavar="PURITY",
        help="SFW/Sketchy/NSFW filters"
    )

    parser.add_argument(
        "-c",
        "--categories",
        choices=["100", "110", "111", "001", "011", "101", "010"],
        default=defaults["categories"],
        metavar="CATS",
        help="General/Anime/People"
    )

    parser.add_argument(
        "--page",
        type=parse_pages,
        default=defaults["page"],
        metavar="PAGE",
        help="Results page or range, eg: 2 or 2:5",
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
    set_download_folder = args.set_folder
    count = args.count
    sort = args.sorting
    order = args.order
    purity = args.purity
    categories = args.categories
    page = args.page

    
    if args.set_api_key is not None:
        api_key = args.set_api_key
        config.saveAPI_key(api_key)
        print("API key saved")
        return

    if set_download_folder is not None:
        config.saveDownload(set_download_folder)
        print("Default folder saved")
        return

    RED = '\033[31m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    RESET = '\033[0m'

    if args.config:
        api_key = config.getAPI_key()

        if api_key is None or api_key=="":
            print(f"{RED}API key is not configured{RESET}")
        else:
            print(f"{YELLOW}API key configured{RESET}")

        print(f"{BLUE}Defaults:{RESET}")
        for default in defaults:
            print(f"\t{GREEN}{default}{RESET}: {defaults[default]}")

        return

    if args.query is None:
        print("No arguments provided. Use 'wallfetch -h' for help.")
        return
    
    api_key = config.getAPI_key()

    wallpapers = []

    for i in range(args.page):
        wallpapers.extend(
            api.getWallpaper(
                query,
                sort,
                order,
                purity,
                categories,
                page,
                api_key
            )
        )

    for wallpaper in wallpapers[:count]:
        downloader.downloadWall(wallpaper, download_folder)


if __name__ == "__main__":
    main()
