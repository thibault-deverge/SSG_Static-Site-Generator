from src.utils.copy_utils import copy_directory
from src.utils.extracters import extract_title


def main():
    copy_directory("static", "public")
    print("-----")

    text = """
# Mon titre principal

Du texte…
"""

    print(extract_title(text))


if __name__ == "__main__":
    main()
