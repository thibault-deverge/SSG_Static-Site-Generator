from src.utils.copy_utils import copy_directory
from src.utils.extracters import extract_title
from src.generate_page import generate_page


def main():
    copy_directory("static", "public")
    print("-------------------------")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
