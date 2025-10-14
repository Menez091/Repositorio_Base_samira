import sqlite3

banco=sqlite3.connect('farmacia.db')
cursor = banco.cursor()

# cursor.execute("CREATE TABLE farmacia(nome TEXT,produto TEXT,valor REAL)")
# cursor.execute ("INSERT INTO farmacia Values('nathalia','creme',25.0)")
# cursor.execute ("INSERT INTO farmacia Values('beatriz','lenço humidecido',10.0)")
# cursor.execute ("INSERT INTO farmacia Values('lorrani','esfoliante',15.5)")
# cursor.execute ("INSERT INTO farmacia Values('laysla','gel',26.8)")
# cursor.execute ("INSERT INTO farmacia Values('duda','enxaguante bucal',30.0)")


# cursor.execute("DELETE FROM farmacia WHERE nome='beatriz'")

cursor.execute("UPDATE farmacia SET nome='gaby' WHERE nome='lorrani' ")

cursor.execute("SELECT * FROM farmacia")
print(cursor.fetchall())

banco.commit()
