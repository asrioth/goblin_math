class ProblemFrame():
    def __init__(self, id, labels = [], buttons = [], progress_bar = None , frame = None):
        self.id = id
        self.labels = labels
        self.buttons = buttons
        self.progress_bar = progress_bar
        self.frame = frame