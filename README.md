GooglePlacesCLI
===============

Python Module/Command-Line Interface for Querying Google Places

```
usage: googleplaces.py [-h] [-l latitude longitude] [-r radius]
                       [-k keyword [keyword ...]] [-j filename] [-n] [-v]
                       key

positional arguments:
  key                   API key provided by Google

optional arguments:
  -h, --help            show this help message and exit
  -l latitude longitude, --location latitude longitude
                        latitude and longitude of the query (required)
  -r radius, --radius radius
                        radius of search in meters (required)
  -k keyword [keyword ...], --keywords keyword [keyword ...]
                        search keywords
  -j filename, --json filename
                        load queries from a json file
  -n, --names           only output names
  -v, --verbose         verbose output
```
