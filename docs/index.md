## Simple documentation for minidl

### Get client IP
Request:
```
https://zalupa-cinema-api-test.herokuapp.com/ip
```

Response example:
```json
{
  "ip": "127.0.0.1"
}
```

### Verify client sign
Request:
```
https://zalupa-cinema-api-test.herokuapp.com/ip/<token>
```

Response example:
```json
{
  "valid": true
}
```

### Proxy media
Request:
```
https://zalupa-cinema-api-test.herokuapp.com/media_proxy/<token>/<sign>
```

Response example:
#### Video/Audio/Stream

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

### Rezka raw
Request:
```
https://zalupa-cinema-api-test.herokuapp.com/rezka/raw/https://rezka.ag/films/horror/52592-varvar-2022.html
```

Response example:
```html
<html lang="ru">{{ source_body }}</html>
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

Response example:
```json
{
  "duration": 1,
  "title": "Мистер Робот",
  "url": "https://zalupa-cinema-api-test.herokuapp.com/media_proxy/gAAAAABjboAHObALk-uQnITyCLvsQ7K_4Xv_ipBr4nkGYQf471RwMOQzKt6gXBPagXSD5C_pxFnRkhLjEyOJ8iRd7iIHU5-b7z46I7DldFY9UstWKaMpxLiBP1KAnV366P61IVdK5XV76KQUaAlgDT02BW0IY06PL9HHTKgzTzdUuq_qKmXTuGmKAnutlS-77VEcoIDUSqtw1smaSjRSHEvhZiYiKXDugJ34Z4xB4tuy2-90MsbJj6kI38ZqoZ8-0g5P1BVZdYlJ355YZxQch-Z0Ut4muztWkyaGwZWokjO6k06qq9lnUjQqk2T6X0rBe8hOXArMYNzONDF2a4FFK-fftUCH2Eyl6v1DoaafrRWxUpjAJLlnHkJEttt9qH97pXy5JLeG7Cun/027391b4c640b30858513b9689c9b77e1a8e41272b55b6c2d3214e5ea5397f88"
}
```