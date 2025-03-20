import os
import argparse


def create_project_structure(project_name):
    """Creates a new DevOps project folder with predefined structure."""
    base_path = os.path.join(os.getcwd(), project_name)
    folders = ["scripts", "tests", "cli_tool", "demo"]
    files = ["README.md", ".gitignore", "requirements.txt", "setup.py"]

    os.makedirs(base_path, exist_ok=True)
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)
    for file in files:
        open(os.path.join(base_path, file), "w").close()

    print(f"✅ Project '{project_name}' created successfully!")


def main():
    """Entry point for the CLI tool."""
    parser = argparse.ArgumentParser(description="DevOps Project Scaffolding Tool")
    parser.add_argument("project_name", help="Name of the new project")
    args = parser.parse_args()
    create_project_structure(args.project_name)


if __name__ == "__main__":
    main()
