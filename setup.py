import setuptools


setuptools.setup(
    name="webte", version="0.0.0",
    packages=setuptools.find_packages(),
    test_suite="webte",
    author="Stefano Palazzo",
    author_email="stefano.palazzo@gmail.com",
    url="https://github.com/sfstpala/webte/",
    license="ISC License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: ISC License (ISCL)",
    ],
    install_requires=[
        "tornado >=4.0.2",
        "tornado-couchdb >=0.2.3",
        "pyte >=0.4.8",
    ],
    entry_points={
        "console_scripts": [
            "webte = webte.__main__:main",
        ]
    },
    package_data={
        "webte": [
            "templates/*.html",
            "static/css/*.css",
        ],
    },
)
