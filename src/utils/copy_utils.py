import os
import shutil


def copy_directory(src_path: str, dst_path: str) -> None:
    # 1. Delete all the contents of the destination directory
    if os.path.exists(dst_path):
        print(f"Removing existing directory: {dst_path}")
        shutil.rmtree(dst_path)

    # 2. Create destination directory
    print(f"Creating directory: {dst_path}")
    os.makedirs(dst_path, exist_ok=True)

    # 3. Copy all files and subdirectories of source directory
    if os.path.exists(src_path):
        for entry in os.listdir(src_path):
            full_src = os.path.join(src_path, entry)
            full_dst = os.path.join(dst_path, entry)

            if os.path.isdir(full_src):
                print(f"Descending into directory: {full_src} → {full_dst}")
                copy_directory(full_src, full_dst)
            else:
                print(f"Copying file: {full_src} → {dst_path}")
                shutil.copy(full_src, dst_path)
    else:
        print(f"Source path not found: {src_path}")
        raise FileNotFoundError("Source directory not found.")
