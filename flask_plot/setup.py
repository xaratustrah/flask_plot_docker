from setuptools import setup

with open('requirements.txt') as rf:

    setup(
        name='yourapplication',
        packages=['yourapplication'],
        include_package_data=True,
        install_requires=rf.readlines(),
    )
