class Phoenix:
    def __init__(self):
        self.state = "merge"
        self.steps = []

    def step(self, mode, target):
        if self.state == "merge":
            if mode == "stress_align":
                self.state = "merge"
                self.steps.append("● merge")
                return self.state

        if self.state == "merge" and mode == "dynamo":
            self.state = "replicate"
            self.steps.append("●● replicate")
            return self.state

        if self.state == "replicate":
            self.state = "terminal"
            self.steps.append("◆ terminal")
            return self.state

        return self.state

    def is_terminal(self):
        return self.state == "terminal"

    def __repr__(self):
        return f"PhoenixEngine(state={self.state}, steps={self.steps})"
