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

# Essa classe faz o papel do repositorio
class Repositorio:
    
    # construtor para criar um repositorio
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador_commits = 0

    # Toda vez que a gente faz um commit novo, o contador aumenta 1 pra ser o id.
    # Ai a gente cria esse commit novo falando que o pai dele e o head antigo,
    # e depois atualiza o head pra ser esse nosso commit novo.
    def commitar(self, mensagem):
        self.contador_commits += 1
        novo_commit = Commit(self.contador_commits, mensagem, self.autor, self.head)
        self.head = novo_commit

    # Mostra a lista de todos os commits. Se nao tiver head, ja imprime o aviso e sai da funcao com o return
    def log(self):
        if self.head is None:
            print("Nenhum commit ainda")
            return
        
        # Se passou pelo if, entao chama o historico
        self.head.historico()

    # Vai contando de um em um quantos commits tem no total.
    # Comeca do ultimo (head) e vai descendo pro pai dele usando um while
    # ate chegar no vazio (None).
    def total_de_commits(self):
        contador = 0
        atual = self.head
        
        while atual is not None:
            contador += 1
            atual = atual.pai
            
        return contador
    