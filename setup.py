from setuptools import setup, find_packages

setup(
    name="buff_api_cn",
    version="1.0.0",
    author="Cline (based on work by markzhdan)",
    author_email="",
    description="An unofficial Python API wrapper for Buff163, with Chinese language support.",
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your_github/buff_api_cn",  # 用户需要替换成自己的仓库地址
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
