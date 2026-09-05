# Sample Config

The configuration (`config.toml`) file looks like this
```
[api]
api_key = ""

[defaults]
folder = "~/Pictures/wallfetch/"
sorting = "date_added"
order = "desc"
purity = "100"
categories = "111"
page = 1
```

## Where
`api_key`: stores user's api key

in `[defaults]` the structure follows as

### sorting
|Value|Sort by|
|---|---|
|`date_added`|Date added|
|`relevance`|Relevance|
|`random`|Random|
|`views`|Views|
|`favorites`|Favorites|
|`toplist`|Toplist|
|`hot`|Hot|

### order
`asc` or `desc`

### purity
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


### categories
```
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


### page
default starting page
