# wallfetch

A simple command-line tool for searching and downloading wallpapers from [Wallhaven](https://wallhaven.cc/).

`wallfetch` lets you search and download wallpapers directly from the terminal without having to open Wallhaven in a browser.

## Demo



https://github.com/user-attachments/assets/512eb70d-b4b5-4091-8ef2-7de765692f51



## Features

- Search wallpapers directly from the terminal
    
- Download multiple wallpapers at once
    
- Progress bars for downloads
    
- Sort wallpapers by relevance, views, favorites, etc.
    
- Filter wallpapers by category and purity
    
- Choose how many wallpapers you want to download
    
- Save wallpapers to `~/Pictures/wallfetch` by default
    
- Specify a custom download directory
    
- Support for Wallhaven API keys
    

## Installation

Clone the repository:

```bash
git clone https://github.com/Aditya1770/wallfetch.git
cd wallfetch
```

Make a Python virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install `wallfetch` in the virtual environment:

```bash
python -m pip install .
```

You can now use:

```bash
wallfetch -h
```

## Usage

Search for wallpapers:

```bash
wallfetch <query>
```

For example:

```bash
wallfetch cyberpunk
```

You can also use queries with spaces:

```bash
wallfetch "dark forest"
```

By default, wallpapers are downloaded to:

```text
~/Pictures/wallfetch
```

### Options

|Option|Description|
|---|---|
|`-n, --count N`|Number of wallpapers to download|
|`-f, --folder FOLDER`|Folder to download wallpapers to|
|`-s, --sorting SORT`|Sort the search results|
|`-o, --order {asc,desc}`|Sorting order|
|`-p, --purity PURITY`|SFW/Sketchy/NSFW filter|
|`-c, --categories CATS`|General/Anime/People filter|
|`--page PAGE`|Page of search results|
|`--set-api-key KEY`|Set your Wallhaven API key|
|`--config`|Check the current wallfetch configuration|
|`-h, --help`|Show the help menu|

### Number of wallpapers

Use `-n` to specify how many wallpapers you want to download:

```bash
wallfetch cyberpunk -n 5
```

### Custom download directory

Use `-f` to specify where the wallpapers should be saved:

```bash
wallfetch cyberpunk -f ~/Pictures/cyberpunk
```

### Sorting

Wallpapers can be sorted using:

|Value|Sort by|
|---|---|
|`date_added`|Date added|
|`relevance`|Relevance|
|`random`|Random|
|`views`|Views|
|`favorites`|Favorites|
|`toplist`|Toplist|
|`hot`|Hot|

For example:

```bash
wallfetch cyberpunk -s favorites
```

You can also change the sorting order:

```bash
wallfetch cyberpunk -s views -o desc
```

### Categories

Wallhaven uses three digits for its category filters:

```text
General / Anime / People
```

`1` enables a category and `0` disables it.

|Value|Categories|
|---|---|
|`100`|General|
|`010`|Anime|
|`001`|People|
|`110`|General + Anime|
|`101`|General + People|
|`011`|Anime + People|
|`111`|All|

For example, to only search for anime wallpapers:

```bash
wallfetch cyberpunk -c 010
```

The default is `111`.

### Purity

Purity works the same way:

```text
SFW / Sketchy / NSFW
```

|Value|Purity|
|---|---|
|`100`|SFW|
|`010`|Sketchy|
|`001`|NSFW|
|`110`|SFW + Sketchy|
|`101`|SFW + NSFW|
|`011`|Sketchy + NSFW|
|`111`|All|

The default is `100`.

For example:

```bash
wallfetch cyberpunk -p 110
```

Some filters may require a Wallhaven API key.

### Pages

Use `--page` to get wallpapers from another page of the search results:

```bash
wallfetch cyberpunk --page 2
```

### API Key

You can save your Wallhaven API key using:

```bash
wallfetch --set-api-key <key>
```

The key is stored in:

```text
~/.config/wallfetch/config.toml
```

To check if an API key is configured:

```bash
wallfetch --config
```

## Examples

Download 5 cyberpunk wallpapers:

```bash
wallfetch cyberpunk -n 5
```

Download 10 anime wallpapers sorted by favorites:

```bash
wallfetch anime -n 10 -c 010 -s favorites
```

Download wallpapers to a different folder:

```bash
wallfetch mountains -n 5 -f ~/Pictures/mountains
```

You can combine the options however you want:

```bash
wallfetch "night city" -n 10 -s favorites -o desc -c 111 -p 100 --page 2
```

## Dependencies

`wallfetch` requires Python 3 and uses:

- [Requests](https://requests.readthedocs.io/) for API requests and downloads
    
- [Rich](https://github.com/Textualize/rich) for download progress bars
    

The dependencies are installed automatically when running:

```bash
python -m pip install .
```

## Uninstall

Since `wallfetch` is installed inside the virtual environment, you can uninstall it with:

```bash
python -m pip uninstall wallfetch
```

Or just remove the virtual environment:

```bash
rm -rf .venv
```

## Contributing

Contributions, bug reports and suggestions are welcome.

If you want to improve `wallfetch`, fork the repository, make your changes and open a pull request.

## License

This project is licensed under the MIT License. See [`LICENSE`](https://chatgpt.com/c/LICENSE) for more information.
