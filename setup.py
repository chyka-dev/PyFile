from setuptools import setup, find_packages

setup(
    name="PyFile",
    version="1.0.1",
    description="More human-friendly file access interface",
    author="Shunsuke Hondo",
    author_email="shunsuke.hondo@gmail.com",
    url="http://github.com/chyka-dev/PyFile",
    license="MIT",
    keywords=["file"],
    packages=find_packages(),
    install_requires=["six"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
)

