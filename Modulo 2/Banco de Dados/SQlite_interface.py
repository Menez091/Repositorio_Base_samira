import sqlite3
import flet as ft

def criar_tabela():
    conexao=sqlite3.connect("usuarios.db")
    cursor=conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,email TEXT NOT NULL UNIQUE,senha TEXT NOT NULL)")
    conexao.commit()
    conexao.close()

def cadastrar_usuario(nome,email,senha):
    conexao=sqlite3.connect("usuarios.db")
    cursor=conexao.cursor()
    cursor.execute("INSERT INTO usuarios (nome,email,senha)VALUES(?,?,?)",(nome,email,senha))
    conexao.commit()
    conexao.close()

def main(page:ft.Page):
    page.title="cadastro de usuario"
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    page.theme_mode="dark"
    page.padding=50
    page.window.width=600
    page.window.height=600

    criar_tabela()
    nome=ft.TextField(label="Nome",width=300,focused_border_color="BLUE")
    email=ft.TextField(label="Email",width=300,focused_border_color="BLUE")
    senha=ft.TextField(label="Senha",password=True,can_reveal_password=True,width=300,focused_border_color="BLUE")

    def cadastrar_clique(e):
        if nome.value and email.value and senha.value:
            try:
                cadastrar_usuario(nome.value,email.value,senha.value)
                page.open(ft.SnackBar(ft.Text("Usuario cadastrado com sucesso!")))
                page.update()
                nome.value=email.value=senha.value=""
                page.update()
            except sqlite3.IntegrityError:
                page.open(ft.SnackBar(ft.Text("Email já cadastrado!")))
        else:
            page.open(ft.SnackBar(ft.Text("Preencha todos os campos")))
            page.update

    botao=ft.ElevatedButton("Cadastrar",on_click=cadastrar_clique,width=200,bgcolor="green",color="white")

    page.add(
        ft.Column(
            [ft.Text("Cadastro de Usuario",size=25,weight="bold"),nome,email,senha,botao],
        )
    )

ft.app(target=main)
