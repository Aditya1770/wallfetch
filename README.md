# wallfetch

A simple command-line tool for searching and downloading wallpapers from [Wallhaven](https://wallhaven.cc/).

`wallfetch` lets you search for wallpapers directly from your terminal and download the results to a local directory.

## Demo

<video src="assets/demo.mp4" controls width="100%"></video>

## Features

* Search for wallpapers directly from the terminal
* Fetch wallpapers from Wallhaven
* Download multiple wallpapers from search results
* Progress bars for downloads
* Save wallpapers to `~/Pictures/wallpapers` by default
* Specify a custom download directory
* Simple CLI interface
* Install globally as the `wallfetch` command

## Installation

Clone the repository:

```bash
git clone https://github.com/Aditya1770/wallfetch.git
cd wallfetch
```

Run the installer:

```bash
chmod +x install.sh
./install.sh
```

After installation, `wallfetch` should be available globally:

```bash
wallfetch
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

or:

```bash
wallfetch "dark forest"
```

By default, downloaded wallpapers are stored in:

```text
~/Pictures/wallpapers
```

### Custom download directory

Use the `-f` option to specify where the wallpapers should be saved:

```bash
wallfetch -f <directory> <query>
```

For example:

```bash
wallfetch -f ~/Pictures/cyberpunk cyberpunk
```

## Dependencies

`wallfetch` requires Python 3 and the Python packages used by the project.

Install the required packages with:

```bash
pip install -r requirements.txt
```

## Uninstall

If `wallfetch` was installed to `/usr/local/bin`, remove it with:

```bash
sudo rm /usr/local/bin/wallfetch
```

## Why wallfetch?

Sometimes you just want to find a wallpaper without opening a browser, searching through a website, downloading the image, and moving it to your wallpaper directory.

With `wallfetch`, you can do it straight from the terminal:

```bash
wallfetch mountains
```

## Contributing

Contributions, bug reports, and suggestions are welcome.

If you'd like to improve `wallfetch`, fork the repository, make your changes, and open a pull request.

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for more information.
