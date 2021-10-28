# Canvas File Link Generator

Given the canvas domain, access token and set of file id's of variable length, this very simple script will grab every verified url such that it is accessible through `curl`, `wget` or even can be used to avoid CORS issues.

## Usage

``` sh
python get_canvas_link.py [-h] [--course_number c] [-p PREFIX] [--files files [files ...]] access_token
```
