#A estrutura de informações que tem em um chamado

class Chamado:
    def __init__(self, id,lab, comp, problem_type, description) -> None:
        self.id = id
        self.lab = lab
        self.comp = comp
        self.problem_type = problem_type
        self.description = description

