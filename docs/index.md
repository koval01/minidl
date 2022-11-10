## Rezka info

### Example
Request:
```https://zalupa-cinema-api-test.herokuapp.com/rezka/https://rezka.ag/series/thriller/9364-mister-robot-2015.html```

Response model:

```json
{
  "translation_name": {
    "episodes": {
      "int_key(episode_id)": "name"
    },
    "seasons": {
      "int_key(season_id)": "name"
    },
    "translator_id": "0"
  }
}
```
