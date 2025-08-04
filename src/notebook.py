from datetime import datetime

class NOTA:
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'

    def __init__(self, code: str, tittle: str, text: str, importance: str) -> None:
        self.code = code
        self.tittle = tittle
        self.text = text
        self.importance = importance
        self.creation_date = datetime.today()
        self.tags = []

        def add_tag(self, tag: str):
            self.tags.append(tag)

        def __str__(self):
            return f"date: {self.creation_date}, tittle: {self.tittle}, text: {self.text}"

class Notebook:
    def __init__(self):
        self.list = []

    def add_note(self, title: str, text: str, importance: str) -> int:

        def generar_nuevo_codigo(notas):
            codigos_existentes = {nota['codigo'] for nota in notas}
            nuevo_codigo = len(notas) + 1

            while nuevo_codigo in codigos_existentes:
                nuevo_codigo += 1
