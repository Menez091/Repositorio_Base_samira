import sqlite3

banco=sqlite3.connect('clinica_medica.db')
cursor = banco.cursor()

# cursor.execute("CREATE TABLE clinica_medica (medico TEXT, especialidade TEXT,paciente TEXT,consulta DATE)")
cursor.execute ("INSERT INTO clinica_medica Values('nathalia','pediatra','samira','01-11-2025')")
cursor.execute ("INSERT INTO clinica_medica Values('beatriz','odontologia','duda','03-11-2025')")
cursor.execute ("INSERT INTO clinica_medica Values('lorrani','dermatologista','nat','22-11-2025')")
cursor.execute ("INSERT INTO clinica_medica Values('laysla','psiquiatra','bea','25-11-2025')")
cursor.execute ("INSERT INTO clinica_medica Values('duda','neurologista','loris','02-12-2025')")


# cursor.execute("DELETE FROM farmacia WHERE nome='beatriz'")

# cursor.execute("UPDATE farmacia SET nome='gaby' WHERE nome='lorrani' ")

cursor.execute("SELECT * FROM clinica_medica")
print(cursor.fetchall())

banco.commit()



