# VA-11 HALL-A Dialogues in .json
Especially thanks to  [Charlotte](https://github.com/dressupgeekout) and her Ruby [Script](https://github.com/dressupgeekout/va11halla-tools/blob/master/bin/va11halla_reader)

## Languages available:
- [English (en)](https://github.com/NoPlagiarism/va11halla-dialogues/tree/master/en)

## Structure
### dialogue_scripts.json
```json
[
    [
        [
            {
                "line": 0
            },
            {
                "filename": Filename (script),
                "lines": Num of script lines,
                "type": "META"
            }
        ],
        [
            {
                "line": 2
            },
            {
                "type": "dialogue",
                "text": "{character}:"
            },
            {
                "type": "dialogue",
                "text": Text
            }
        ],
and e.t.c
```

### dialogue_groupped.json
```json
{
    Character: [
        {
            "script": {
                "filename": Filename (script),
                "lines": Num of script lines,
                "type": "META"
            },
            "line": 2,
            "text": Text
        },
and e.t.c

```