from argparse import ArgumentParser
from markitdown import MarkItDown
from pathlib import Path

parser = ArgumentParser(description="this is a program can convert files to markdown format powered by Microsoft/MarkItDown project, notice that this tool may not generate **good** contents, you need to do some postprocesses like removing the weired spaces and line changing,this process will print processed contents in terminal output.")

parser.add_argument("--reference",  "-r",nargs="+", type=str,required= True, help="the references being used, it can be file or url(not recommended)")
parser.add_argument("--output_dir", "-o", type=str, default=".", help="the directory to save the markdown output")

args = parser.parse_args()
refs = args.reference
output_dir = Path(args.output_dir)
output_dir.mkdir(parents=True, exist_ok=True)

md = MarkItDown(enable_builtins=True)

for ref in refs:
    input_path = Path(ref)
    output_filename = output_dir / f"{input_path.stem}.md" # Use stem for filename without extension

    with open(input_path, "rb") as file:
        markdown_content = md.convert(file).text_content
        with open(output_filename, "w", encoding="utf-8") as outfile:
            outfile.write(markdown_content)
        print(f"Converted {input_path} to {output_filename}")
       