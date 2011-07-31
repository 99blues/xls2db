import xlrd
import sqlite3 as sqlite
import itertools

def xls2db(infile, outfile):
    """
    Convert an xls file into an sqlite db!
    """
    wb = xlrd.open_workbook(infile)
    db_conn = sqlite.connect(outfile)
    db_cursor = db_conn.cursor()

    for s in wb.sheets():

        # Create the table.
        # Vulnerable to sql injection because ? is only able to handle inserts
        # I'm not sure what to do about that!
        db_cursor.execute("create table " + s.name + " ("
            + ','.join([s.cell(0,j).value for j in xrange(s.ncols)]) +");")

        for row in ([s.cell(i, j).value for j in xrange(s.ncols)] for i in xrange(s.nrows-1)):
            # Change blank/empty entries into nulls
            map_over = lambda l: lambda f: map(f, l)
            @map_over(row)
            def map_fxn(item):
                if (item == xlrd.empty_cell.value):
                    return None
                else:
                    return item

            # Able to do a hack to use ?'s
            db_cursor.execute("insert into " + s.name + ' values ('
                + ','.join(itertools.repeat('?', s.ncols)) +");", row)

    db_conn.commit()
    db_cursor.close()
    db_conn.close()

def db2xls(infile, outfile):
    """
    Convert an sqlite db into an xls file. Not implemented!
    Some issues: one needs to be able to figure out what the table names are!
    """
    raise NotImplementedError
