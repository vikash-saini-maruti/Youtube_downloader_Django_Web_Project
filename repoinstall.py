'''

myenv\Scripts\activate`

'''

import subprocess

def install_requirements(file_path):
    failed_packages = []

    with open(file_path, 'r') as file:
        for line in file:
            package = line.strip()
            try:
                subprocess.run(['pip', 'install', package], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error installing {package}: {e}")
                failed_packages.append(package)

    if failed_packages:
        print("\nPackages that encountered errors:")
        for package in failed_packages:
            print(package)
    else:
        print("\nAll packages installed successfully.")

if __name__ == "__main__":
    requirements_file = "requirements.txt"
    install_requirements(requirements_file)
