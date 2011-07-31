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


Schema:
-------

Each worksheet represents a table with that name. Each table is written with
headers corresponding to column names/types/etc. expected in an sqlite database,
and the rest of the rows are, well, rows. For example, I have data in a
worksheet called "links" that looks like this::

    src string  dst string  dir string
    kitchen     outside     West
    kitchen     w_hwy       East
    w_hwy       ctr_hwy     East
    ctr_hwy     e_hwy       East
    e_hwy       living      East
    w_hwy       w_bath      North
    ctr_hwy     e_bath      North
    w_hwy       josh_bdr    South
    ctr_hwy     guest_bdr   South
    e_hwy       james_bdr   South

If you're familiar with sql, this probably makes sense. Somewhat.

Installation:
-------------

::

    sudo pip install -U xls2db

Dependencies:
-------------

- xlrd
- xlwt
- plac (for command line args)


Tests:
------

I haven't written any yet, because I'm lazy.

Developers! Developers! Developers!
-----------------------------------

I suspect most of you are stabbing your eyes out with rusty nails. If you're
not, however, why not give it a try? Help me track down some bugs? Fix anything
that seems like it's begging for sql injection?

License:
--------

MIT.
