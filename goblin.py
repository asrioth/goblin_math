from resourceManager import ResourceManager, Resource
import enum
from goblinAccuracy import GoblinAccuracy

class Goblin():
    def __init__(self, problem_manager, resource_manager, shop, id, is_user=False):
        self.problem_manager = problem_manager
        self.resource_manager = resource_manager
        self.shop = shop
        self.id = id
        self.is_user = is_user
        self.monch_display = Resource.MONCH.value
        self.blegh_display = Resource.BLEGH.value
        self.emphasis = "*"
        self.accuracy = GoblinAccuracy(1, 1, problem_manager.difficulty)
        self.answer_index = 0

    def _update_display(self, crunch):
        match crunch:
            case Resource.MONCH:
                self.monch_display = f"{self.emphasis}{self.monch_display}{self.emphasis}" 
            case Resource.BLEGH:
                self.blegh_display = f"{self.emphasis}{self.blegh_display}{self.emphasis}"

    def eat_answer(self, answer):
        if self.problem_manager.check_choice(answer):
            self.monch()
            return Resource.MONCH
        else:
            self.blegh()
            return Resource.BLEGH
        
    def solve_problem(self):
        hit = self.accuracy.does_hit()
        for choice_i in range(len(self.problem_manager.choices)):
            is_answer = self.problem_manager.check_choice(self.problem_manager.choices[choice_i]) 
            if hit and is_answer:
                self.answer_index = choice_i
                return
            elif not hit and not is_answer:
                self.answer_index = choice_i
                return
        self.answer_index = 0



    def monch(self):
        self.resource_manager.monchs += 1
        self.resource_manager.update_crunches(self.problem_manager.difficulty, True)
        self._update_display(Resource.MONCH)

    def blegh(self):
        self.resource_manager.bleghs += 1
        self.resource_manager.update_crunches(self.problem_manager.difficulty, False)
        self._update_display(Resource.BLEGH)