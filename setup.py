from distutils.core import setup

setup(
    name = "xls2db",
    version = "0.0.5",
    packages = ["xls2db"],
    requires = ['xlrd', 'plac'],
    install_requires = ['xlrd', 'plac'],
    description = "Convert excel files following a particular schema into sqlite database files.",
    author = "Joshua Holbrook",
    author_email = "josh.holbrook@gmail.com",
    url = "https://github.com/jesusabdullah/xls2db",
    keywords = ["excel", "sqlite", "probably_a_bad_idea", "because_f_you_thats_why"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7", #only one tested
        "Topic :: Other/Nonlisted Topic"
    ],
    scripts = ["./bin/xls2db"],
    long_description = """\
xls2db
======

xls2db is a python program that takes an excel spreadsheet following a certain
schema into an sqlite database that can be opened using python's sqlite3 module.
It can also be used as a module.

Why??
-----

Because fuck you, that's why.

But seriously: I was getting sick of doing data entry for this toy project of
mine using cursor.execute()'s, so I figured I'd try entering the data into an
excel spreadsheet, converting it into the db, and then manipulating it from
there. Crazy, I know.

Usage:
--------

As a script::

    xls2db infile.xls outfile.db

As a module::

    from xls2db import xls2db
    xls2db("infile.xls", "outfile.db")

For more, visit <https://github.com/jesusabdullah/xls2db> .
    """
)
