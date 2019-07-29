from setuptools import setup


def readme():
    with open("README.md") as f:
        README = f.read()
    return README


setup(
    name="quoteland",
    version="1.0.1",
    description="A Python package to get quotes as per topics and author.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/harshraj22/pyquotes",
    author="Harsh Raj",
    author_email="harshraj22aug@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["quoteland"],
    include_package_data=True,
    install_requires=["requests", "bs4"],
    entry_points={
        # "console_scripts": [
        #     "weather-reporter=weather_reporter.cli:main",
        # ]
    },
)
