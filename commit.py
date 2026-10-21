class Commit:
    
    # O construtor recebe e guarda os dados
    # O primeiro commit nao tem pai, por isso o padrao e None.
    def __init__(self, id, mensagem, autor, pai=None):
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    # Imprime a mensagem desse commit e depois manda o pai imprimir tambem.
    # Ele vai fazendo isso de tras pra frente ate chegar no primeiro commit,
    # que nao tem pai.
    def historico(self):
        print(f"#{self.id} {self.mensagem} ({self.autor})")
        
        # Se tiver um commit anterior (pai), pede pra ele imprimir
        if self.pai is not None:
            self.pai.historico()
    