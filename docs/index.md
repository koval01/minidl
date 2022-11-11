### Rezka translations
Request:
```
https://zalupa-cinema-api-test.herokuapp.com/rezka/translations/https://rezka.ag/films/horror/52592-varvar-2022.html
```

Response example:

```json
{
  "TVShows": "232",
  "Оригинал (+субтитры)": "238",
  "Украинский многоголосый ": "359",
  "яскъер (Jaskier)": "32"
}
```

### Rezka serial
Request:
```
https://zalupa-cinema-api-test.herokuapp.com/rezka/serial/https://rezka.ag/films/horror/52592-varvar-2022.html
```

Response example:

```json
{
  "TVShows": {
    "episodes": {
      "1": {
        "1": "Серия 1"
      }
    },
    "seasons": {
      "1": "Сезон 1"
    },
    "translator_id": "232"
  }
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
@sIDeIDtID

s = season id
e = episode id
t = translator id
```