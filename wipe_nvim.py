import os
import shutil
import tarfile
import time
import argparse

# Define the backup directory
BACKUP_DIR = os.path.expanduser('~/neovim_backups')
BACKUP_FILENAME = f"neovim_config_backup_{time.strftime('%Y%m%d%H%M%S')}.tar.gz"
BACKUP_PATH = os.path.join(BACKUP_DIR, BACKUP_FILENAME)

# List of directories to back up for Neovim
neovim_dirs = {
    'config_nvim': os.path.expanduser('~/.config/nvim'),
    'share_nvim': os.path.expanduser('~/.local/share/nvim'),
    'state_nvim': os.path.expanduser('~/.local/state/nvim'),
    'lib_nvim': os.path.expanduser('~/.local/lib/nvim'),
    'site_nvim': os.path.expanduser('~/.local/share/nvim/site'),
}

# List of directories to back up for Vim (if --delete-vim flag is set)
vim_dirs = {
    'vim': os.path.expanduser('~/.vim'),
}

# Function to back up directories
def backup_directories(dirs_to_backup):
    with tarfile.open(BACKUP_PATH, "w:gz") as tar:
        for arcname, directory in dirs_to_backup.items():
            if os.path.exists(directory):
                print(f"Backing up {directory} as {arcname}...")
                tar.add(directory, arcname=arcname)

# Function to remove directories
def remove_directories(dirs_to_remove):
    for directory in dirs_to_remove.values():
        if os.path.exists(directory):
            print(f"Removing {directory}...")
            shutil.rmtree(directory)

def main(delete_vim=False, dry=False):
    # Create backup directory if it doesn't exist
    os.makedirs(BACKUP_DIR, exist_ok=True)

    # Directories to back up (Neovim related)
    dirs_to_backup = neovim_dirs.copy()

    # If --delete-vim flag is set, include Vim-related directories
    if delete_vim:
        dirs_to_backup.update(vim_dirs)

    # Perform the backup
    print("Starting backup...")
    backup_directories(dirs_to_backup)
    print(f"Backup completed: {BACKUP_PATH}")

    # Remove Neovim-related directories
    print("Removing Neovim configurations and related files...")
    if not dry: remove_directories(neovim_dirs)

    # If --delete-vim flag is set, remove Vim-related directories
    if delete_vim:
        print("Removing Vim configurations and related files...")
        if not dry: remove_directories(vim_dirs)

    print("Done.")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Backup and remove Neovim and Vim configurations.")
    parser.add_argument('--delete-vim', action='store_true', help="Also delete Vim-related configurations (~/.vim)")
    
    args = parser.parse_args()

    # Run the main function with the appropriate flag
    main(delete_vim=args.delete_vim,dry=False)

