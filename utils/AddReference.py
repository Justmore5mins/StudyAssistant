import argparse
import hashlib
import os
from markitdown import MarkItDown

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--subject", "-s", required=True, help="Subject to add reference for")
    parser.add_argument("--reference", "-r", required=True, help="Reference to add, md, pdf, or urls are ok")
    args = parser.parse_args()

    subject = args.subject
    reference = args.reference

    # Create subject directory if it doesn't exist
    raw_dir = os.path.join("data", subject, "raw")
    os.makedirs(raw_dir, exist_ok=True)

    # Generate a unique filename
    filename = hashlib.md5((subject + reference).encode()).hexdigest() + ".md"
    raw_path = os.path.join(raw_dir, filename)

    # Convert and save the content
    md = MarkItDown(enable_plugins=False)
    
    content = ""
    # The reference can be a local file path or a URL
    if os.path.isfile(reference):
        with open(reference, "rb") as f:
            content = md.convert(f).text_content
    else:
        content = md.convert(reference).text_content

    with open(raw_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Append to references.ref
    with open("data/references.ref", "a+", encoding="utf-8") as f:
        f.write(f"{subject}:{reference}\n")

    print(f"Successfully added reference for {subject} from {reference} with filename {filename}")

if __name__ == "__main__":
    main()
