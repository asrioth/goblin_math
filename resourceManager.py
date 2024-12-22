import math
import enum

class Resource(enum.Enum):
    MONCH = "Monch"
    BLEGH = "blegh"
    CRUNCHES = "crunches"

class ResourceManager():
    def __init__(self):
        self.crunches = 0
        self.monchs = 0
        self.bleghs = 0
        self.euller_mascheroni_constant = 0.577215664901533 #approx
        self.display = "Number Debris: 0"

    def _get_digits(self):
        if self.crunches != 0:
            digits = int(math.log10(abs(self.crunches))) + 1
        else:
            digits = 1
        return digits

    def _set_display_text(self):
        self.display = f"Number Debris: {self.crunches:.{self._get_digits()}f}"

    def click_detected(self):
        self.clicks += 1

    def update_crunches(self, problem_difficulty, success):
        if (success):
            success_mod = 1
        else:
            success_mod = -1
        crunches = self._calculate_length_crunches(problem_difficulty.length, success_mod)
        crunches += self._calculate_digits_crunches(problem_difficulty.digits, success_mod)
        crunches += self._calculate_choice_crunches(problem_difficulty.choice_amount, problem_difficulty.choice_range, success_mod)
        self.crunches += crunches / 3
        self._set_display_text()

    def take_resource(self, resource_type, amount):
        match resource_type:
            case Resource.CRUNCHES:
                if (self.crunches >= amount):
                    self.crunches -= amount
                    self._set_display_text()
                    return True
        return False
    
    def get_resource_value(self, resource_type):
        match resource_type:
            case Resource.CRUNCHES:
                return self.crunches
    
    def return_resource(self, resource_type, amount):
        match resource_type:
            case Resource.CRUNCHES:
                self.crunches += amount
                self._set_display_text()

    def _calculate_length_crunches(self, length, success_mod):
        return (math.log(pow(math.e, 1-self.euller_mascheroni_constant) + (length - 1)) + self.euller_mascheroni_constant) * success_mod
    
    def _calculate_digits_crunches(self, digits, success_mod):
        return (math.log(pow(math.e, 1-self.euller_mascheroni_constant) + (pow(10, digits) - 1)) + self.euller_mascheroni_constant) * success_mod
    
    def _calculate_choice_crunches(self, choice_amount, choice_range, success_mod):
        if choice_range == 0:
            return success_mod
        if choice_amount == 1:
            return success_mod
        return (((2 * choice_range * choice_amount) + choice_amount - (2 * choice_range) - 1) * success_mod)/ choice_amount
