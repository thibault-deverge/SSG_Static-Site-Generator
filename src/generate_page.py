import os
from src.utils.converters_blocks import markdown_to_html_node
from src.utils.extracters import extract_title


def write_file_ensuring_dir(filepath: str, content: str) -> None:
    parent_dir = os.path.dirname(filepath)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if not os.path.exists(from_path):
        raise FileNotFoundError(f"Source markdown not found: {from_path!r}")
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template not found: {template_path!r}")

    # 1. Open and read the markdown and template
    with open(from_path, "r", encoding="utf-8") as file:
        markdown_content = file.read()
    with open(template_path, "r", encoding="utf=8") as file:
        template_content = file.read()

    # 2. Extract title and generate html node from the markdown
    html_string = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    # 3. Populate template and write the html file
    page_content = template_content.replace("{{ Title }}", title)
    page_content = page_content.replace("{{ Content }}", html_string)
    # page_content = page_content.replace('src="/', f'src="{basepath}')
    # page_content = page_content.replace('href="/', f'href="{basepath}')
    print(page_content)
    write_file_ensuring_dir(dest_path, page_content)


def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, entry)
        rel_src = os.path.relpath(full_path, start="content")

        if os.path.isfile(full_path):
            dest_path = os.path.join(dest_dir_path, rel_src).replace(".md", ".html")
            generate_page(full_path, template_path, dest_path, basepath)
        else:
            generate_page_recursive(full_path, template_path, dest_dir_path, basepath)
