from textual.app import (
    App
)
from apppkg import (
    model, view
)

class AppMain(App):
    
    TITLE = "Título da App"
    
    CSS_PATH = f"{model.CSSDIR}/main.tcss"
    SCREENS = {
        "principal": view.Principal,
        "uma_tela": view.UmaTela,
        "outra_tela": view.OutraTela,
    }

    def on_mount(self):
        self.push_screen("principal")

    def action_tela_principal(self):
        self.switch_screen("principal")

    def action_uma_tela(self):
        self.switch_screen("uma_tela")

    def action_outra_tela(self):
        self.switch_screen("outra_tela")


