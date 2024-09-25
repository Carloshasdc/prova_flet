import flet as ft

def main(page: ft.Page):
    
    tarefas = []
    
    def button_clicked(e):
        if campo_texto.value:  
            tarefas.append(campo_texto.value)  
            campo_texto.value = ""  
            atualizar_lista()  

    def atualizar_lista():
        lista_tarefas.controls.clear()  
        for tarefa in tarefas:
            lista_tarefas.controls.append(ft.Text(tarefa))  
        page.update()  

    
    campo_texto = ft.TextField(label="Digite sua tarefa", width=300)    
    botao_adicionar = ft.ElevatedButton("Adicionar", on_click=button_clicked)    
    lista_tarefas = ft.Column()    
    page.add(
        ft.Row([campo_texto, botao_adicionar]),  
        lista_tarefas  
    )


ft.app(target=main)
