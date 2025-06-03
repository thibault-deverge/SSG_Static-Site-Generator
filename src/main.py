import sys

from src.utils.copy_utils import copy_directory
from src.utils.extracters import extract_title
from src.generate_page import generate_page, generate_page_recursive


def main():
    try:
        copy_directory("static", "public")
        print("-------------------------")
        generate_page_recursive("content/", "template.html", "public")
    except Exception as e:
        print("Error :", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
