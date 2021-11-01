# VA-11 HALL-A Dialogues in .json
Especially thanks to  [Charlotte](https://github.com/dressupgeekout) and her Ruby [Script](https://github.com/dressupgeekout/va11halla-tools/blob/master/bin/va11halla_reader)

## Languages available:
- [English (en)](https://github.com/NoPlagiarism/va11halla-dialogues/tree/master/en)
- [Russian (ru)](https://github.com/NoPlagiarism/va11halla-dialogues/tree/master/ru) [using translation by koshk.ru](https://koshk.ru/uploads/va11_rus_fin-10_190330.zip)

## Structure
### dialogue_scripts.json
```json
[
    [
        [
            {
                "line": 0,
                "filename": Filename (script),
                "lines": Num of script lines,
                "type": "META"
            }
        ],
        [
            {
                "line": Num of line in script,
                "type": "dialogue",
                "character": Character,
                "text": Text
            }
        ],
and e.t.c
```

### dialogue_grouped.json
```json
{
    Character: [
        {
            "script": {
                "filename": Filename (script),
                "lines": Num of script lines,
                "type": "META"
            },
            "line": Num of line in script,
            "text": Text
        },
and e.t.c

```
_All rights belongs to [SUKEBAN GAMES](https://sukeban.moe/)_
