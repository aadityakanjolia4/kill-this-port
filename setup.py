from setuptools import setup, find_packages
from setuptools.command.install import install


def writemessage():
    print("Thanks for installing kill_this_port")
    print("Author: Aaditya Kanjolia")
    print("github: https://github.com/aadityakanjolia4")


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        writemessage()
        # run_migration()


with open("README.md", "r") as f:
    long_desc = f.read()

setup(
    name="kill-this-port",
    version="1.0.1",
    description="A simple utility to kill processes running on a specified port",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    author="Aaditya Kanjolia",
    author_email="a21kanjolia@gmail.com",
    entry_points={
        "console_scripts": [
            "killport=kill_this_port.core:main",
            "checkport=kill_this_port.core:check_main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.7",
    cmdclass={
        "install": PostInstallCommand,
    },
)
