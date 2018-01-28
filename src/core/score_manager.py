class ScoreDatabase():

    def __init__(self, path):
        self.__path = path
        self.__scores = []
    
    def load():
        self.__file = open(self.__path, 'r')
        self.__scores = []
        for line in self.__file:
            self.__scores.append(int(line))
        self.__file.close()

    def save():
        self.__file = open(self.__path, 'w')       
        for score in self.__scores:
            self.__file.write(score)

    def add(score):
        #   if less than 5 scores exist then add score
        if self.__scores.len() < 5:
            self.__scores.append(score)
        #   else check smallest value and remove if score > minimum
        else:
            minimum = min(self.__scores)
            if minimum < score:
                self.__scores.remove(minimum)
                self.__scores.append(score)
        #   sort scores
        list(reversed(sorted(self.__scores)))

    def get_scoreDatabase():
        return self.__scores

