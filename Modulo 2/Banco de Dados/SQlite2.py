import sqlite3

banco=sqlite3.connect('clinica_medica.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS MEDICO (nome TEXT,onde_trabalha TEXT,dia_semana TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS ESPECIALIDADE (especialildade)")
cursor.execute("CREATE TABLE IF NOT EXISTS PACIENTE (nome TEXT,idade INTEGER,data_nascimento DATE)")
cursor.execute("CREATE TABLE IF NOT EXISTS CONSULTA (medico TEXT, especialidade TEXT,paciente TEXT,consulta DATE)")



cursor.execute ("INSERT INTO MEDICO Values('nathalia','santa_ana','seg_e_qua')")
cursor.execute ("INSERT INTO ESPECIALIDADE Values('pediatria')")
cursor.execute ("INSERT INTO ESPECIALIDADE Values('ortopedia')")
cursor.execute ("INSERT INTO ESPECIALIDADE Values('psiquiatria')")
cursor.execute ("INSERT INTO PACIENTE  Values('lorrani','15','11-03-2009')")
cursor.execute ("INSERT INTO CONSULTA Values('nathalia','psiquiatria','bea','25-11-2025')")

# cursor.execute("UPDATE MEDICO SET nome='nathalia' WHERE nome='sasa' ")
# cursor.execute("UPDATE ESPECIALIDADE SET especialidade='psiquiatria' WHERE especialidade='dermatologia' ")
# cursor.execute("UPDATE PACIENTE SET idade='16' WHERE idade='15' ")
# cursor.execute("UPDATE CONSULTA SET paciente='bea' WHERE paciente='bia' ")

# cursor.execute("DELETE FROM MEDICO WHERE nome='sasa'")
# cursor.execute("DELETE FROM ESPECIALIDADE WHERE nome='dermatologia'")
# cursor.execute("DELETE FROM PACIENTE WHERE idade='16'")
# cursor.execute("DELETE FROM CONSULTA WHERE paciente='bia'")

cursor.execute("SELECT * FROM MEDICO")
print(cursor.fetchall())

cursor.execute("SELECT * FROM ESPECIALIDADE")
print(cursor.fetchall())

cursor.execute("SELECT * FROM PACIENTE")
print(cursor.fetchall())

cursor.execute("SELECT * FROM CONSULTA")
print(cursor.fetchall())

banco.commit()



