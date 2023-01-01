# koval01/minidl
Source code: [koval01/minidl](https://github.com/koval01/minidl)

Working with this API is quite simple. You want to display something from the user - you need to request a method for the path `/rezka/serial/URL`, if the JSON is empty, then we process it like a normal movie. If the JSON is not empty, then we continue our work. We will ask for a list of translations/voiceovers `/rezka/translations/URL`, let's display it to the user so that he chooses what he needs. Further from the previously received `/rezka/serial/URL` we will get the desired fragment by translation number. Output data for users, seasons, and then series of that season. Ok, you've chosen everything, we're asking for the mp4 link `/rezka/episode/URL/SEASON/EPISODE/TRANSLATION_ID`

## Get translations
Request:
```
http://127.0.0.1:3400/rezka/translations/https://rezka.ag/series/thriller/9364-mister-robot-2015.html
```
Response:
```json
{
    "Украинский многоголосый ": "359",
    "ньюстудио (NewStudio)": "3",
}
```

## Get film info
Request (use @tINT for select translation):
```
http://127.0.0.1:3400/https://rezka.ag/films/adventures/33150-sonik-v-kino-2020.html@t358
```
Response:
```json
{
    "duration": 1,
    "title": "Соник в кино",
    "url": "https://kappa.stream.voidboost.cc/889055fba1d841b233d5c57d9ba7ef5e:2023010214:L1kyczIrazJFTzBSSEpSUkZTREw2YmR4blV2UUFSdW8zSTh0aFNNN2dBdnlIc1Vaa1psNEQzWHdOeVRBL0dDN0hBWmxOdnhwWjY1WUhBdXJlNVlCS0E9PQ==/1/0/6/0/2/6/lylx8.mp4"
}
```

## Get serial info
Request:
```
http://127.0.0.1:3400/rezka/serial/https://rezka.ag/series/thriller/9364-mister-robot-2015.html
```
Response:
```json
{
    "Украинский многоголосый ": {
        "episodes": {
            "1": {
                "1": "Серия 1",
                "2": "Серия 2",
                "3": "Серия 3",
                "4": "Серия 4",
                "5": "Серия 5",
                "6": "Серия 6",
                "7": "Серия 7",
                "8": "Серия 8",
                "9": "Серия 9",
                "10": "Серия 10"
            },
            "2": {
                "1": "Серия 1",
                "2": "Серия 2",
                "3": "Серия 3",
                "4": "Серия 4",
                "5": "Серия 5",
                "6": "Серия 6",
                "7": "Серия 7",
                "8": "Серия 8",
                "9": "Серия 9",
                "10": "Серия 10",
                "11": "Серия 11",
                "12": "Серия 12"
            },
            "3": {
                "1": "Серия 1",
                "2": "Серия 2",
                "3": "Серия 3",
                "4": "Серия 4",
                "5": "Серия 5",
                "6": "Серия 6",
                "7": "Серия 7",
                "8": "Серия 8",
                "9": "Серия 9",
                "10": "Серия 10"
            },
            "4": {
                "1": "Серия 1",
                "2": "Серия 2",
                "3": "Серия 3",
                "4": "Серия 4",
                "5": "Серия 5",
                "6": "Серия 6",
                "7": "Серия 7",
                "8": "Серия 8",
                "9": "Серия 9",
                "10": "Серия 10",
                "11": "Серия 11",
                "12": "Серия 12",
                "13": "Серия 13"
            }
        },
        "seasons": {
            "1": "Сезон 1",
            "2": "Сезон 2",
            "3": "Сезон 3",
            "4": "Сезон 4"
        },
        "translator_id": "359"
    },
    "ньюстудио (NewStudio)": {
        "episodes": {
            "1": {
                "1": "Серия 1",
                "2": "Серия 2",
                "3": "Серия 3",
                "4": "Серия 4",
                "5": "Серия 5",
                "6": "Серия 6",
                "7": "Серия 7",
                "8": "Серия 8",
                "9": "Серия 9",
                "10": "Серия 10"
            },
            "2": {
                "1": "Серия 1",
                "2": "Серия 2",
                "3": "Серия 3",
                "4": "Серия 4",
                "5": "Серия 5",
                "6": "Серия 6",
                "7": "Серия 7",
                "8": "Серия 8",
                "9": "Серия 9",
                "10": "Серия 10",
                "11": "Серия 11",
                "12": "Серия 12"
            },
            "3": {
                "1": "Серия 1",
                "2": "Серия 2",
                "3": "Серия 3",
                "4": "Серия 4",
                "5": "Серия 5",
                "6": "Серия 6",
                "7": "Серия 7",
                "8": "Серия 8",
                "9": "Серия 9",
                "10": "Серия 10"
            },
            "4": {
                "1": "Серия 1",
                "2": "Серия 2",
                "3": "Серия 3",
                "4": "Серия 4",
                "5": "Серия 5",
                "6": "Серия 6",
                "7": "Серия 7",
                "8": "Серия 8",
                "9": "Серия 9",
                "10": "Серия 10",
                "11": "Серия 11",
                "12": "Серия 12",
                "13": "Серия 13"
            }
        },
        "seasons": {
            "1": "Сезон 1",
            "2": "Сезон 2",
            "3": "Сезон 3",
            "4": "Сезон 4"
        },
        "translator_id": "3"
    }
}
```

## Get episode from serial
Request: (select Season:4 | Episode: 1 | Traslation: Украинская озвучка (ID: 359))
```
http://127.0.0.1:3400/rezka/episode/https://rezka.ag/series/thriller/9364-mister-robot-2015.html/4/1/359
```
Response:
```json
{
    "duration": 1,
    "title": "Мистер Робот",
    "url": "https://stream.voidboost.cc/d87f1d32e128aab94897f132b1dc191c:2023010214:L1kyczIrazJFTzBSSEpSUkZTREw2YmR4blV2UUFSdW8zSTh0aFNNN2dBdnlIc1Vaa1psNEQzWHdOeVRBL0dDN3ZMVmhGRitIWGIzN1BINFRvQVZFWFE9PQ==/4/4/6/5/1/5/hl9xr.mp4"
}
```