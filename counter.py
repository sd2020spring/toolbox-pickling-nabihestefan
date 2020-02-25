""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dumps, load


def updateCounter(filename, reset=False):
    """Update a counter stored in the file 'filename'.

    A new counter will be created and initialized to 1 if none exists or if the
    reset True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    Parameters
    ----------
    filename: str
        The file that stores the counter to be incremented.  If the file
        doesn't exist, a counter is created and initialized to 1.
    reset: bool
        True if the counter in the file should be reset.

    Returns
    -------
    int
        The new counter value

    Examples
    --------
    >>> updateCounter('blah.txt',True)
    1
    >>> updateCounter('blah.txt')
    2
    >>> updateCounter('blah2.txt',True)
    1
    >>> updateCounter('blah.txt')
    3
    >>> updateCounter('blah2.txt')
    2
    """
    if reset or not(exists(filename)):
        counter = 1
    else:
        with open(filename,'rb+') as f:
            counter = load(f)
        counter += 1
        f.close()

    file = open(filename, 'wb')
    file.write(dumps(counter))
    return counter


if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
    else:
        print("new value is {}".format(updateCounter(sys.argv[1])))
