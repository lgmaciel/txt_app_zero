from textual.app import (
    ComposeResult
)
from textual.screen import (
    Screen
)
from textual.widgets import (
    Static, Header, Footer
)
from apppkg import (
    model
)

class Principal(Screen):

    SUB_TITLE = ("Principal")
    CSS_PATH = f"{model.CSSDIR}/Principal.tcss"

    BINDINGS = [
        ("f1", "app.uma_tela", "Uma Tela"),        
        ("f2", "app.outra_tela", "Outra Tela"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Principal")
        yield Footer()

class UmaTela(Screen):    
    SUB_TITLE = "(Uma Tela)"
    CSS_PATH = f"{model.CSSDIR}/UmaTela.tcss"

    BINDINGS = [        
        ("f2", "app.outra_tela", "Outra Tela"),
        ("escape", "app.tela_principal", "Principal"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Conteúdo de uma tela")
        yield Footer()


class OutraTela(Screen):    
    SUB_TITLE = "(Outra Tela)"
    CSS_PATH = f"{model.CSSDIR}/OutraTela.tcss"
    BINDINGS = [        
        ("f1", "app.uma_tela", "Uma Tela"),
        ("escape", "app.tela_principal", "Principal"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Conteúdo de outra tela")
        yield Footer()