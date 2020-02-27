#!/usr/bin/env python3
"""
The *bean machine*, also known as the *Galton Board* or *quincunx*, is a device invented by Sir Francis Galton to demonstrate the central limit theorem, in particular that the normal distribution is approximate to the binomial distribution.
"""

import argparse
import random
import threading


class Board:
    """
    Class Board
    
    Contains multiple bins that collect beans
    Contains multiple levels of pegs
    """

    def __init__(self, bins: int):
        """Make a new board of the specified size"""
        self._bins = [0] * bins
        self._pegs = bins // 2

    def status(self, pos: int):
        """Print status"""
        self._pos = 0
        #raise NotImplementedError

    def __len__(self):
        """Return the board size"""
        return len(self._bins)

    def __getitem__(self, idx: int):
        """Get number of beans in the specified bin"""
        return self._bins[idx]

    def __setitem__(self, idx: int, new_value: int):
        """Set number of beans in the specified bin"""
        self._bins[idx] = new_value

    @property
    def pegs(self):
        """Return number of levels of pegs"""
        return self._pegs


class Bean(threading.Thread):
    """
    Class Bean
    Data members: board, current position, probability, lock
    """

    def __init__(self, board: object, start: int, prob: float, lock: object):
        """Make a new Bean"""
        self._board = board
        self._start = start
        self._prob = prob
        self._lock = lock
        #raise NotImplementedError

    def move_left(self):
        """Move a bean left"""
        self._board._bins[self._bins] -= 1
		self._board._bins[self._bins - 1] += 1
		self._bins = self._bins - 1
    
    def move_right(self):
        """Move a bean right"""
        self._board._bins[self._bins] += 1
		self._board._bins[self._bins + 1] -= 1
		self._bins = self._bins + 1

    def run(self):
        """Run a bean through the pegs"""
        self._lock.acquire()
        for i in range(self._board._pegs * 2):
            r = random.choices(['left','right'],weights=[0.5,0.5],k=1)
            if r == ['left']:
                if self._start != 0:
                    self.move_left()
            else:
                if self._start != len(self._board)-1:
                    self.move_right()
        self._lock.release()
        #raise NotImplementedError


def main():
    """Main function"""
    # Parse command-line arguments
    # Create a list of jobs
    # Create a shared lock
    # Create a board
    # Create jobs (beans)
    # Print the board status
    # Start jobs
    # Stop jobs
    # Print the board status
    parser = argparse.ArgumentParser(description="Process the arguments.")
    print("Start")
    parser.add_argument("--beans",default=1000,type=int)
    parser.add_argument("--bins",default=11,type=int)
    parser.add_argument("--start",default=5,type=int)
    parser.add_argument("--prob",default=0.5,type=float)
    args = parser.parse_args()
    print("Beans: {}, Bins: {}, start: {}, prob: {} ".format(args.beans,args.bins,args.start,args.prob))
    b = Board(int(args.bins))
    bean = Bean(b,0,0.5,1)
    b.__setitem__(args.start,args.beans)
    print(bean.run())
    lock = threading.Lock()
    
    print("Done")


if __name__ == "__main__":
    main()