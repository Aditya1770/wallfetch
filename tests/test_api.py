from unittest.mock import patch

from wallfetch.api import getWallpaper


def test_get_wallpaper_returns_expected_data():
    fake_response = {
        "data": [
            {
                "id": "94x38z",
                "url": "https://wallhaven.cc/w/94x38z",
                "short_url": "http://whvn.cc/94x38z",
                "views": 6,
                "favorites": 0,
                "source": "",
                "purity": "sfw",
                "category": "anime",
                "dimension_x": 6742,
                "dimension_y": 3534,
                "resolution": "6742x3534",
                "ratio": "1.91",
                "file_size": 5070446,
                "file_type": "image/jpeg",
                "created_at": "2018-10-31 01:23:10",
                "colors": [
                    "#000000",
                    "#abbcda",
                    "#424153",
                    "#66cccc",
                    "#333399",
                ],
                "path": "https://w.wallhaven.cc/94/wallhaven-94x38z.jpg",
                "thumbs": {
                    "large": "https://th.wallhaven.cc/lg/94/94x38z.jpg",
                    "original": "https://th.wallhaven.cc/orig/94/94x38z.jpg",
                    "small": "https://th.wallhaven.cc/small/94/94x38z.jpg",
                },
            },
            {
                "id": "ze1p56",
                "url": "https://wallhaven.cc/w/ze1p56",
                "short_url": "http://whvn.cc/ze1p56",
                "views": 11,
                "favorites": 0,
                "source": "",
                "purity": "sfw",
                "category": "anime",
                "dimension_x": 3779,
                "dimension_y": 2480,
                "resolution": "3779x2480",
                "ratio": "1.52",
                "file_size": 1011043,
                "file_type": "image/jpeg",
                "created_at": "2018-10-07 17:05:28",
                "colors": [
                    "#424153",
                    "#e7d8b1",
                    "#cc3333",
                    "#ffffff",
                    "#cccccc",
                ],
                "path": "https://w.wallhaven.cc/ze/wallhaven-ze1p56.jpg",
                "thumbs": {
                    "large": "https://th.wallhaven.cc/lg/ze/ze1p56.jpg",
                    "original": "https://th.wallhaven.cc/orig/ze/ze1p56.jpg",
                    "small": "https://th.wallhaven.cc/small/ze/ze1p56.jpg",
                },
            },
        ],
        "meta": {
            "current_page": 1,
            "last_page": 36,
            "per_page": 24,
            "total": 848,
            "query": "test",
            "seed": None,
        },
    }

    with patch("wallfetch.api.requests.get") as mock_get:
        mock_get.return_value.json.return_value = fake_response
        mock_get.return_value.raise_for_status.return_value = None

        wallpapers = getWallpaper("test")

    assert wallpapers == [
        {
            "id": "94x38z",
            "url": "https://w.wallhaven.cc/94/wallhaven-94x38z.jpg",
            "filetype": "jpeg",
        },
        {
            "id": "ze1p56",
            "url": "https://w.wallhaven.cc/ze/wallhaven-ze1p56.jpg",
            "filetype": "jpeg",
        },
    ]


def test_get_wallpaper_sends_correct_parameters():
    fake_response = {
        "data": []
    }

    with patch("wallfetch.api.requests.get") as mock_get:
        mock_get.return_value.json.return_value = fake_response
        mock_get.return_value.raise_for_status.return_value = None

        getWallpaper(
            query="anime",
            sorting="favorites",
            order="desc",
            purity="100",
            categories="010",
            page=2,
            api_key="testkey123",
        )

        mock_get.assert_called_once_with(
            "https://wallhaven.cc/api/v1/search",
            params={
                "q": "anime",
                "sorting": "favorites",
                "order": "desc",
                "purity": "100",
                "categories": "010",
                "page": 2,
                "apikey": "testkey123",
            },
        )
