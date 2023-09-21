import flet as ft
import cadastraProd

def main(page: ft.Page):
    page.title = "Cadastro de produtos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def cadastro(event):
        cadastraProd.cadastro(nome.value,preco.value,categoria.value,marca.value,codigo.value)
    
    marcas_op = [
        ft.dropdown.Option("Samsung"),
        ft.dropdown.Option("Apple"),
        ft.dropdown.Option("Hp"),
        ft.dropdown.Option("Nintendo"),
        ft.dropdown.Option("Shen"),
        ft.dropdown.Option("Outro")
    ]
    categoria_op = [
        ft.dropdown.Option("Eletrônico"),
        ft.dropdown.Option("Alimentação"),
        ft.dropdown.Option("Roupas"),
        ft.dropdown.Option("Games"),
        ft.dropdown.Option("outro")
    ]
    
    # itens
    nome = ft.TextField(label="Nome",width=310)
    preco = ft.TextField(label="Preço",width=150)
    marca = ft.Dropdown(label="Marca",width=150,options=marcas_op)
    categoria = ft.Dropdown(label="Categoria",width=150,options=categoria_op)
    codigo = ft.TextField(label="Código",width=150)
    cadastrar = ft.ElevatedButton(text="Cadastrar", on_click=cadastro,width=300,height=50)
    
    #visualização
    view = ft.Column(
        width=310,
        controls=[
            nome,
            ft.Row([preco, categoria]),
            ft.Row([codigo, marca]),
            cadastrar
        ]
    )
    
    page.add(view)
    

ft.app(target=main)