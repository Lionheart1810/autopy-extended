import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autopy-extended",
    version="1.0.0",
    author="Leonard Kugis",
    author_email="leonard@kug.is",
    description="Few extensions to autopy, such as advanced mouse movement patterns.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
    install_requires = [
        "autopy",
		"numpy",
		"scipy"
    ],
    py_modules = [
        "AutopyExtended/Curve/Curve",
		"AutopyExtended/Curve/Linear",
		"AutopyExtended/Curve/Bezier"
		"AutopyExtended/mouse"
    ],
    scripts = []
)
