from resourceManager import ResourceManager

class Goblin():
    def __init__(self, problem_manager, resource_manager, id, is_user=False):
        self.problem_manager = problem_manager
        self.id = id
        self.is_user = is_user
        self.resource_manager = resource_manager
    
    def monch(self):
        self.resource_manager.update_crunches(self.problem_manager.difficulty, True)

    def blegh(self):
        self.resource_manager.update_crunches(self.problem_manager.difficulty, False)