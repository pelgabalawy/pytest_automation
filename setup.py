import setuptools

# dependencies
dependencies = ["pytest", "pytest-json", "selenium", "selenium-page-factory"]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytest_automation",
    version="1.0.0",
    author="Peter Elgabalawy",
    author_email="pelgabalawy@gmail.com",
    description="pytest with selenium page factory project setup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=dependencies,
    python_requires=">=3.6",
)