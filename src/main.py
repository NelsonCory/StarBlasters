from core.game import *
import sys


def main(argv):
	game = Game()
	return game.run()


if __name__ == '__main__':
	sys.exit(main(sys.argv))
