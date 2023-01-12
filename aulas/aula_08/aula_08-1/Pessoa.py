class Pessoa:

    def __init__(self, id, nome, idade, sexo):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id 

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade

    def get_sexo(self):
        return self.sexo

    def set_sexo(self, sexo):
        self.sexo = sexo
