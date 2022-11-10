### Rezka info
Request:
```
https://zalupa-cinema-api-test.herokuapp.com/rezka/https://rezka.ag/series/thriller/9364-mister-robot-2015.html
```

Response example:

```json
{
  "TVShows": {
    "episodes": {
      "1": {
          "1": "Серия 1"
        }
      }
    },
    "seasons": {
      "1": "Сезон 1"
    },
    "translator_id": "232"
}
```

### Rezka selector

*If it's a movie, you don't need to set the parameters*

Example select 4 season 1 episode
```
https://zalupa-cinema-api-test.herokuapp.com/https://rezka.ag/series/thriller/9364-mister-robot-2015.html@s4e1
```

Params:
```
s = season id
e = episode id
t = translator id
```