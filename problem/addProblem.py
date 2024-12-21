class AddProblem():
    def __init__(self, numbers):
        self.display = ""
        self.numbers = numbers
        self._set_display_text()
        self.answer = sum(numbers)

    def new_problem(self, numbers):
        self.numbers = numbers
        self.sum = sum(numbers)
        self._set_display_text()

    def _set_display_text(self):
        display_text = f"{self.numbers[0]}"
        if len(self.numbers) > 1:
            display_text += "".join(map(lambda number: f" + {number}", self.numbers[1:]))
        display_text += " ="
        self.display = display_text

    def __eq__(self, value):
        if type(self) != type(value): return False
        return self.display == value.display
    
    def __repr__(self):
        return f"AddProblem({self.display})"