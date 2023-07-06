# 0x01-shell_permissions

This repository contains shell scripts that demonstrate various file and directory permissions in Unix-like systems. Each script focuses on a specific aspect of permissions and provides examples and explanations.


## Scripts

- `0-iam_betty`: This script changes the user owner of the file `hello` to the user `betty`.
- `1-who_am_i`: This script prints the effective username of the current user.
- `2-groups`: This script lists all the groups the current user is part of.
- `3-new_owner`: This script changes the owner of the file `hello` to the user `betty` and the group owner to the group `holberton`.
- `4-empty`: This script creates an empty file named `hello`.
- `5-execute`: This script adds execute permissions to the owner of the file `hello`.
- `6-multiple_permissions`: This script adds execute permissions to the owner and the group owner, and read permissions to other users for the file `hello`.
- `7-everybody`: This script adds execute permissions to the owner, the group owner, and other users for the file `hello`.
- `8-James_Bond`: This script sets the permissions of the file `hello` to `-rwxr-----`.
- `9-John_Doe`: This script sets the permissions of the file `hello` to `-rwxr-x-wx`.
- `10-mirror_permissions`: This script sets the permissions of the file `hello` to the same as the file `olleh`.
- `11-directories_permissions`: This script adds execute permissions to all subdirectories of the current directory for the owner, group owner, and other users.
- `12-directory_permissions`: This script creates a directory named `dir_holberton` with specific permissions.
- `13-change_group`: This script changes the group owner of the file `hello` to the group `holberton`.


## Usage

To run any of the scripts, navigate to the project directory and execute the desired script using the following syntax:

./script_name

Make sure to replace `script_name` with the actual name of the script you want to run.


## Author

[@ykellyk](https://github.com/ykellyk)

