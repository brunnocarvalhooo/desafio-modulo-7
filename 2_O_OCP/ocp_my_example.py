'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''


from abc import ABC, abstractmethod


class Verification(ABC):

    @abstractmethod
    def verifica_condicoes(self) -> bool:
        pass


class Sangue(Verification):
    def verifica_condicoes(self) -> bool:
        # implemente as condições específicas do exame de sangue
        return True


class RaioX(Verification):
    def verifica_condicoes(self) -> bool:
        # implemente as condições específicas do exame de raio-x
        return True


class AprovaExame:
    def aprovar_solicitacao_exame(self, exame: Verification):
        if exame.verifica_condicoes():
            print(f"{type(exame).__name__} aprovado!")
        else:
            print(f"{type(exame).__name__} reprovado!")


# Exemplo de uso:
exame_sangue = Sangue()
exame_raio_x = RaioX()

aprovador = AprovaExame()
aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)
