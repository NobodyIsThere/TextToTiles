TextToTiles
===========
Simple program to turn a text-based tile map into an image. You can use this to,
for example, visualise Mario levels in the format used in
[TheVGLC](https://github.com/TheVGLC/TheVGLC), or visualise levels created in
[VGDL](https://github.com/EssexUniversityMCTS/gvgai/wiki/Level-Description-File).

Usage:
```
python text_to_tiles.py filename [--type TYPE] [-o OUTFILE] filename
```
where `type` is by default `smb` (Super Mario Bros), which is included as an
example in the `data/smb` directory. Other mappings should be placed in their
own subdirectories under `data/`, including a `mapping.json` file which
specifies the tile size and which characters correspond to which images.
