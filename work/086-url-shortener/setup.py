from setuptools import setup

with open("requirements.txt") as f:
    requirements = []
    for line in f.readlines():
        if line.strip() is not "":
            requirements.append(line.strip())


with open("requirements-dev.txt") as f:
    development_requirements = []
    for line in f.readlines():
        if not line.strip().startswith("-r") and line.strip() is not "":
            development_requirements.append(line.strip())

setup(
    name='URL Shortener',
    version='1.2dev',
    description='Simple URL shortener to be hosted on AWS Lambda',
    author='Tibor Leupold',
    author_email='tibor@lpld.io',
    packages=['short'],
    install_requires=requirements,
    extras_require={
        "develop": development_requirements,
    },
)
