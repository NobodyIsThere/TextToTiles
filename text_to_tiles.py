import argparse
import json

from PIL import Image

def load_mapping(type):
    with open("data/{}/mapping.json".format(type), 'r') as f:
        mapping = json.load(f)
        return mapping

def text_to_tiles(filename, type='smb', outfile='out.png'):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    mapping = load_mapping(type)
    tile_size = mapping["tile_size"]
    width = (len(lines[0])-1)*tile_size
    height = len(lines)*tile_size
    
    for key in mapping["tiles"].keys():
        mapping["tiles"][key] = Image.open("data/{}/{}".format(type,
                                           mapping["tiles"][key]))
    
    output = Image.new('RGB', (width, height))
    
    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            x = i*tile_size
            y = j*tile_size
            if char != '\n':
                output.paste(mapping["tiles"][char],
                             (x,y,x+tile_size,y+tile_size))
    
    output.save("out.png", "PNG")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    parser.add_argument("--type", type=str, default="smb",
                        help="Which data directory should I look at?")
    parser.add_argument("-o", "--outfile", type=str, default="out.png",
                        help="Where to place the output file.")
    args = parser.parse_args()
    
    text_to_tiles(args.filename, args.type, args.outfile)