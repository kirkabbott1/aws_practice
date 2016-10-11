import pg
db = pg.DB(dbname='test_db', user='postgres', passwd='teenage mutant ninja turtles', host='localhost')
query = db.query('select * from student')
print query
