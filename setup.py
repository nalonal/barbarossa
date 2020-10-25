import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="barbarossa", # Replace with your own username
    version="0.0.3",
    author="Rizqy Rionaldy",
    author_email="rionaldyrizqy@gmail.com",
    description="Simple Python to Crawling Google",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nalonal/barbarossa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['bs4','requests']
)