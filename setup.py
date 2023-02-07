from setuptools import setup, find_packages


with open("readme.rst", "r") as f:
    readme = f.read()

setup(
    name="ck8s",
    version="0.0.1",
    description="CK8S POC command line",
    long_description=readme,
    author='Ayoub ED-DAFALI',
    author_email='ayoub.eddafali@elastisys.com',
    packages=find_packages('src'),
    package_dir={'':'src'},
    setup_requires=[],
    install_requires=["kubernetes"],
    entry_points={
        'console_scripts': ['ck8s=ck8s.cli:main'],
    }
)


