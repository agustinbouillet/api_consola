# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='api_consola',
    version='1.0.6',
    author='Agustin Bouillet, Horacio Alvarado',
    author_email='bouilleta@jefatura.gob.ar',
    url='https://www.argentina.gob.ar/',
    description='Push notifications',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['push', 'notifications', 'console', 'messages'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        'setuptools==66.1.1',
        'firebase-admin==6.7.0',
    ],
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/yourproject/issues",
        "Documentation": "https://yourproject.readthedocs.io/en/latest/",
        "Source Code": "https://github.com/yourusername/yourproject",
    },
)