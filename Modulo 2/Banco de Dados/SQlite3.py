import sqlite3

banco=sqlite3.connect('biblioteca.db')
cursor = banco.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS AUTOR(autor TEXT,data_de_nascimento DATE,genero TEXT,Obras_principais TEXT)")
# cursor.execute("CREATE TABLE IF NOT EXISTS LIVRO(nome TEXT,qauntidade_de_pagina INTEGER,genero TEXT)")
# cursor.execute("CREATE TABLE IF NOT EXISTS EMPRESTIMO(nome_do_livro TEXT,data_de_emprestimo DATE,data_de_devolução DATE)")
# cursor.execute("CREATE TABLE IF NOT EXISTS ALUNO(nome TEXT,turma INTEGER,nota REAL)")


# cursor.execute ("INSERT INTO AUTOR Values('J.K Rowling','31-07-1975','feminino','Harry Potter')")
# cursor.execute ("INSERT INTO LIVRO Values('O pequeno principe','650','fantasia')")
# cursor.execute ("INSERT INTO EMPRESTIMO Values('O iluminado','23-10-2025','02-11-2025')")
# cursor.execute ("INSERT INTO ALUNO Values('Sarah','1','9.7')")


# cursor.execute("UPDATE AUTOR SET autor='Lorrani' WHERE autor='J.K Rowling' ")
# cursor.execute("UPDATE LIVRO SET nome='Coraline' WHERE nome='O pequeno principe' ")
# cursor.execute("UPDATE EMPRESTIMO SET nome_do_livro='Wall-e' WHERE nome_do_livro='O iluminado' ")
# cursor.execute("UPDATE ALUNO SET nome='Lola' WHERE nome='Sarah' ")


# cursor.execute("DELETE FROM AUTOR WHERE autor='lorrani'")
# cursor.execute("DELETE FROM LIVRO WHERE nome='Coraline '")
# cursor.execute("DELETE FROM EMPRESTIMO WHERE nome_do_livro='Wall-e'")
# cursor.execute("DELETE FROM ALUNO WHERE nome='Lola'")



cursor.execute("SELECT * FROM AUTOR")
print(cursor.fetchall())

cursor.execute("SELECT * FROM LIVRO")
print(cursor.fetchall())

cursor.execute("SELECT * FROM EMPRESTIMO")
print(cursor.fetchall())

cursor.execute("SELECT * FROM ALUNO")
print(cursor.fetchall())

banco.commit()