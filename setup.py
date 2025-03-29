# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='api_consola',
    version='1.0.19',
    author='Agustin Bouillet, Horacio Alvarado',
    author_email='bouilleta@jefatura.gob.ar',
    url='https://www.argentina.gob.ar/',
    description='Push notifications',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['push', 'notifications', 'console', 'messages'],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'api_consola = api_consola.__main__:main',
        ],
    },
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
    package_data={
        'api_consola': ['html/*.html'],
    },
    project_urls={
        "Bug Tracker": "https://git.argentina.gob.ar/argentina/consola-notificaciones/api-consola/-/issues",
        "Source Code": "https://git.argentina.gob.ar/argentina/consola-notificaciones/api-consola",
    },
)