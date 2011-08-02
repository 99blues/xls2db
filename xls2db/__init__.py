import xlrd
import sqlite3 as sqlite
import itertools

def xls2db(infile, outfile):
    """
    Convert an xls file into an sqlite db!
    """
    #Now you can pass in a workbook!
    if type(infile) == str:
        wb = xlrd.open_workbook(infile)
    elif type(infile) == xlrd.Book:
        wb = infile
    else:
        raise TypeError

    #Now you can pass in a sqlite connection!
    if type(outfile) == str:
        db_conn = sqlite.connect(outfile)
        db_cursor = db_conn.cursor()
    elif type(outfile) == sqlite.Connection:
        db_conn = outfile
        db_cursor = db_conn.cursor()
    else:
        raise TypeError

    for s in wb.sheets():

        # Create the table.
        # Vulnerable to sql injection because ? is only able to handle inserts
        # I'm not sure what to do about that!
        db_cursor.execute("create table " + s.name + " ("
            + ','.join([s.cell(0,j).value for j in xrange(s.ncols)]) +");")

        for row in ([s.cell(i+1, j).value for j in xrange(s.ncols)] for i in xrange(s.nrows-1)):
            # Change blank/empty entries into nulls
            map_over = lambda l: lambda f: map(f, l)
            @map_over(row)
            def map_fxn(item):
                if item == xlrd.empty_cell.value or item == u'':
                    return None
                else:
                    return item

            # Able to do a hack to use ?'s
            db_cursor.execute("insert into " + s.name + ' values ('
                + ','.join(itertools.repeat('?', s.ncols)) +");", row)

    db_conn.commit()
    #Only do this if we're not working on an externally-opened db
    if type(outfile) == str:
        db_cursor.close()
        db_conn.close()

def db2xls(infile, outfile):
    """
    Convert an sqlite db into an xls file. Not implemented!
    Some issues: one needs to be able to figure out what the table names are!
    """
    raise NotImplementedError
