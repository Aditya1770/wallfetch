from unittest.mock import patch

from wallfetch.downloader import downloadWall


def test_download_wallpaper(tmp_path):
    wallpaper_info = {
        "id": "94x38z",
        "url": "https://w.wallhaven.cc/94/wallhaven-94x38z.jpg",
        "filetype": "jpeg",
    }

    fake_image_data = b"fake image bytes"

    with patch("wallfetch.downloader.requests.get") as mock_get:
        mock_get.return_value.headers = {
            "content-length": str(len(fake_image_data))
        }

        mock_get.return_value.iter_content.return_value = [
            fake_image_data
        ]

        mock_get.return_value.raise_for_status.return_value = None

        downloadWall(
            wallpaper_info,
            tmp_path,
        )

    downloaded_file = tmp_path / "94x38z.jpeg"

    assert downloaded_file.exists()
    assert downloaded_file.read_bytes() == fake_image_data


def test_download_wallpaper_uses_correct_url(tmp_path):
    wallpaper_info = {
        "id": "ze1p56",
        "url": "https://w.wallhaven.cc/ze/wallhaven-ze1p56.jpg",
        "filetype": "jpeg",
    }

    fake_image_data = b"wallpaper data"

    with patch("wallfetch.downloader.requests.get") as mock_get:
        mock_get.return_value.headers = {
            "content-length": str(len(fake_image_data))
        }

        mock_get.return_value.iter_content.return_value = [
            fake_image_data
        ]

        mock_get.return_value.raise_for_status.return_value = None

        downloadWall(
            wallpaper_info,
            tmp_path,
        )

        mock_get.assert_called_once_with(
            "https://w.wallhaven.cc/ze/wallhaven-ze1p56.jpg",
            stream=True,
        )
