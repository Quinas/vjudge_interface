from setuptools import setup, find_packages

setup(
    name="vjudge-interface",
    version="0.1",
    url="https://github.com/Quinas/vjudge_interface.git",
    author="Pablo Astudillo",
    author_email="pablomaster9@gmail.com",
    description="Python interface for vjudge.net",
    packages=find_packages(),
    install_requires=["requests_html >= 2.22"],
)
