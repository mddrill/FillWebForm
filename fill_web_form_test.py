# fill_web_form_test.py

# import statements
import unittest
import fill_web_form
import sqlite3
import sys
import argparse

form = 'test'
form_name = 'test_form'

### For this Test you must enter a random word into data
### The test succeeds if that word is successfully entered into the
### Test database through the test webpage

# Enter word here
data = "fdsa"

    
class KnownValues(unittest.TestCase):

    def test_fill_form(self):
        
        # connect to sample database
        print 'connecting to database'
        conn = sqlite3.connect('FlaskApp\FlaskApp\sample.db')
        conn.text_factory = str

        # clear database table
        print "clearing database"
        cursor = conn.cursor()
        cursor.execute("DROP TABLE if exists test_table")
        cursor.execute("CREATE TABLE if not exists test_table(test_column)")
        conn.commit()
        
        # run function
        print "running fill_web_form.py"

        fill_web_form.fill_form("http://127.0.0.1:5000", form, form_name, data)

        # get results of function from database
        print "fetching results of fill_web_form.py"
        cursor = conn.execute("SELECT test_column FROM test_table")
        result = cursor.fetchone()[0]
        print "Database contains string: " + result
        expected = data

        # check for expected output
        print "checking if output is correct"
        self.assertEquals(expected, result)

# Run tests

if __name__ == '__main__':
    unittest.main(argv=sys.argv[:1])
