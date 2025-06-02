import os
from src.utils.converters_blocks import markdown_to_html_node
from src.utils.extracters import extract_title


def write_file_ensuring_dir(filepath: str, content: str) -> None:
    parent_dir = os.path.dirname(filepath)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # 1. Open and read the markdown and template
    with open(from_path, "r", encoding="utf-8") as file:
        markdown_content = file.read()
    with open(template_path, "r", encoding="utf=8") as file:
        template_content = file.read()

    # 2. Extract title and generate html node from the markdown
    html_string = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    # 3. Populate template and write the html file
    page_content = template_content.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_string
    )
    write_file_ensuring_dir(dest_path, page_content)
