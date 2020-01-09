**IMPORTANT:** Python 3.x is required

### Steps for installation:

    # clone this repo
    git clone https://github.com/felipecaon/comperio.git

    # change path
    cd comperio/

    # run comperio
    python3 comperio.py user1 user2 ...
    
    
### How to use

Run  ```comperio.py -h``` to show expected arguments

### Sites supported

The current supported site list can be found inside [sites.json](https://github.com/felipecaon/comperio/blob/master/sites.json "sites.txt") file.

### Adding new sites

In order to add new sites you must include a new json object in the sites.json file.

|    key     | value |
|------------|-------|
| identifier | site identifier, usually the name, to appear during/after script execution. |
| url        | site url where a profile can be found, with {user} showing the injection point. |

example:

```
{
  "identifier": "sample",
  "url": "http://sample.com/{user}"
}
```