import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stocks-b3-calebecavalcante", # Replace with your own username
    version="0.0.1",
    author="Calebe Cavalcante",
    author_email="calebesantos.cavalcante@gmail.com",
    description="Buscar dados das ações na B3, hospedadas no site https://finance.yahoo.com/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CalebeCavalcante/stocks",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)