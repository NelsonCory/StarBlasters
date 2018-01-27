class EventManager:

	def __init__(self):
		self.__queue = []
		self.__callbacks = {}

	def send(self, label, value):
		self.__queue.insert(0, (label, value))

	def dispatch(self):
		while len(self.__queue) > 0:
			label, value = self.__queue.pop()
			if label in self.__callbacks:
				for f in self.__callbacks[label]:
					f(value)

	def subscribe(self, label, callback):
		if label in self.__callbacks:
			self.__callbacks[label].append(callback)
		else:
			self.__callbacks[label] = [callback]
