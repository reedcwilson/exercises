class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def highest(self):
        return max(self.scores)

    def top(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        last = self.latest()
        diff = self.highest() - last
        s = f"{diff} short of " if diff > 0 else ""
        return f"Your latest score was {last}. That's {s}your personal best!"
