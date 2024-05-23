from setuptools import setup, find_packages

setup(
    name="formidable",
    version="0.1.0",
    description="A robust HTMX inline form validation and CSRF protection package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Thandden",
    author_email="your.email@example.com",
    url="https://github.com/thandden/formidable",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)