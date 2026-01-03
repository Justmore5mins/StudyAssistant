from markitdown import MarkItDown
from sys import argv
from os.path import isfile
from io import TextIOWrapper
from hashlib import md5
from google import genai

for ref in argv[1:]:
    data: str | None = None

    if isfile(ref) or "http" in ref or "www." in ref:
        data = ref
    else:
        print("Invalid reference:", ref)
    
    if data:
        md = MarkItDown(enable_builtins=True)
        model = genai.Client()
        try:
            open(f"{md5(ref.encode()).hexdigest()}.md", "x").close()
            with open(f"{md5(ref.encode()).hexdigest()}.md", "w+", encoding="utf-8") as file:
                res = model.models.generate_content(model="gemini-3-flash-preview", contents="tidy up(like removing the strange space and new lines) the following content into markdown format, and no extra text:\n\n" + md.convert(data).text_content)
                if res.text is not None:
                    file.write(res.text)
                else:
                    raise ValueError("No content generated from the model.", res)
                print("Converted and saved to", f"{md5(ref.encode()).hexdigest()}.md")
            
        except Exception as e:
            print("Error during conversion:", e)