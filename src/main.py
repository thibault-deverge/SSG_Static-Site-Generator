import sys

from src.utils.copy_utils import copy_directory
from src.generate_page import generate_page_recursive

BASEPATH = "/SSG_Static-Site-Generator/"


def main():
    try:
        copy_directory("static", "docs")
        print("-------------------------")
        generate_page_recursive("content/", "template.html", "docs", BASEPATH)
    except Exception as e:
        print("Error :", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
