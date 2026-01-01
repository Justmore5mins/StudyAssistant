from argparse import ArgumentParser
from os import mkdir
from os.path import exists, isfile
from markitdown import MarkItDown
from hashlib import md5
from time import time

parser = ArgumentParser()
parser.add_argument("--subject", "-s", type=str, help="Subject to add reference for", required=True)
parser.add_argument("--reference", "-r", type=str, help="Reference to add, md, pdf, or urls are ok", required=True)
parser.add_argument("--type", "-t", type=str, help="Type of the reference, access", required=False)
argv = parser.parse_args()

if not exists("caches/"):
    mkdir("caches/")

FileName = ""
md = MarkItDown(enable_plugins=False)

if not argv.reference.endswith(".md"):
    FileName = f"caches/{md5((argv.subject + argv.reference).encode()).hexdigest()}.md"
    if not isfile(FileName):
        with open(FileName, 'wb') as file:
            file.write(md.convert(argv.reference).text_content.encode("utf-8"))
    else:
        print(f"Reference cache exists: {FileName}")
        pass
else:
    pass