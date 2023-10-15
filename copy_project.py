import os
import shutil


def should_exclude(file, exclude_list):
    for pattern in exclude_list:
        if pattern in file:
            return True
    return False


def copy_project(src_dir, dest_dir, exclude_file):
    # Read exclude patterns from file

    if exclude_file:
        with open(exclude_file, 'r') as f:
            exclude_list = [line.strip() for line in f]
    else:
        exclude_list = ['venv', 'folders', '.idea', '__pycache__', '.pytest_cache']

    for root, dirs, files in os.walk(src_dir):
        # Exclude directories and files
        dirs[:] = [d for d in dirs if not should_exclude(d, exclude_list)]
        files = [f for f in files if not should_exclude(f, exclude_list)]

        # Construct destination directory
        rel_root = os.path.relpath(root, src_dir)
        dest_root = os.path.join(dest_dir, rel_root)

        # Create destination directory
        if not os.path.exists(dest_root):
            os.makedirs(dest_root)

        # Copy files
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_root, file)
            shutil.copy2(src_file, dest_file)


if __name__ == '__main__':
    src_dir = './projects'  # Replace with your source directory
    dest_dir = './'  # Replace with your destination directory
    copy_project(src_dir, dest_dir)
