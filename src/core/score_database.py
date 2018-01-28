import os

class ScoreDatabase():

    __instance = None

    @staticmethod
    def get_instance():
        return ScoreDatabase.__instance

    def __init__(self, path):
        self.__path = os.path.join(os.path.dirname(path), "scores.data")
        self.__scores = []
        ScoreDatabase.__instance = self

    def load(self):
        self.__scores = []
        f = open(self.__path, 'r')
        for line in f:
            self.__scores.append(int(line))
        f.close()
        if len(self.__scores) == 0:
            self.__scores.append(0)
        self.resort_scores()

    def save(self):
        f = open(self.__path, 'w')
        for score in self.__scores:
            f.write(str(score) + '\n')

    def add(self, score):
        #   if less than 5 scores exist then add score
        if len(self.__scores) < 5:
            self.__scores.append(score)
        #   else check smallest value and remove if score > minimum
        else:
            minimum = min(self.__scores)
            if minimum < score:
                self.__scores.remove(minimum)
                self.__scores.append(score)
        #   sort scores
        self.resort_scores()
        self.save()

    def resort_scores(self):
        self.__scores = list(reversed(sorted(self.__scores)))

    def get_scores(self):
        return self.__scores

