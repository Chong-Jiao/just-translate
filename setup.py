import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="just-translate", # Replace with your own username
    version="1.0.0",
    author="jiao chong",
    author_email="jch_email@qq.com",
    description="translate words via baidu translation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chong-Jiao/just-translate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)