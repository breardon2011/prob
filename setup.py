from setuptools import setup, find_packages

setup(
    name="my_prob_tests",
    version="0.1",
    packages=find_packages(),
    install_requires=["flask", "plotly"],  # List dependencies here
    entry_points={
        "console_scripts": [
            "run_tests=my_prob_tests.app:main",  # Set up command-line entry point
        ],
    },
)
