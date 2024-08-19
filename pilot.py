
import random
import numpy as np

class Pilot():

    def __init__(self, minimum_threshold, in_bounds):
        self.minimum_threshold = minimum_threshold
        self.in_bounds = in_bounds
        # also known as X in formula
        self.state = np.array([0, 0, 0, 0, 0, 0])
        # TODO, might need to make some of these like y, z and r object variables
        self.F = np.array([[1, 1, 0, 0, 0, 0],
                           [0, 1, 1, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 1, 1, 0],
                           [0, 0, 0, 0, 1, 1],
                           [0, 0, 0, 0, 0, 1]])
        self.P = np.array([[2, 0, 0, 0, 0, 0],
                           [0, 2, 0, 0, 0, 0],
                           [0, 0, 2, 0, 0, 0],
                           [0, 0, 0, 2, 0, 0],
                           [0, 0, 0, 0, 2, 0],
                           [0, 0, 0, 0, 0, 2]])
        # FIXME fill this in accurately
        self.H = np.array([[1, 0, 0, 0, 0, 0],
                           [0, 1, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 1, 0],
                           [0, 0, 0, 0, 0, 1]])
        self.y = None
        self.k = None


    # updates for movement
    def update_pmove(self):
        self.P = np.dot(np.dot(self.F, self.P), np.transpose(self.F))

    # updates for sensing
    def update_psense(self):
        self.P = np.dot((np.identity(6) - np.dot(self.K, self.H)), self.P)

    # TODO figure out if R is self variable of parameter, and how to calculate
    def s(self):
        return self.dot(self.dot(self.H, self.P), np.transpose(self.H)) + self.r

    def kalman_gain(self):
        self.k = np.dot(np.dot(self.P, self.transpose(self.H)), np.inverse(self.s(self.r)))

    # aka y in math
    def error(self, z):
        self.y = z - np.dot(self.H, self.state)

    def update_state(self):
        self.state += np.dot(self.k, self.y)

    def observe_asteroids(self, asteroid_locations):
        """
           asteroid_locations - a list of asteroid observations. Each 
           observation is a tuple (i,x,y) where i is the unique ID for
           the asteroid, and x,y are the x,y locations (with noise) of the
           current observation of the asteroid for this timestep.
           Only asteroids that are currently 'in-bounds' will appear
           in this list.  The list may change in size as asteroids move
           out-of-bounds or new asteroids appear in-bounds.

           Return Values:
                    None
        """

        pass
        # <STUDENT IMPLEMENTATION GOES HERE>


    def estimate_asteroid_locs(self):
        """ Should return an iterable (list or tuple for example) that
            contains data in the format (i,x,y), consisting of estimates
            for all in-bound asteroids. """

        pass
        # <STUDENT IMPLEMENTATION GOES HERE>

        return []

    def next_move(self, craft_state):
        """
            craft_state - implemented as CraftState in craft.py.

            return values: 
              angle change: the craft may take the following actions:
                                turn left: 1
                                turn right: -1
                                go straight: 0
                            Turns adjust the craft's heading by 
                             angle_increment.
              speed change: the craft may:
                                accelerate: 1,
                                decelerate: -1
                                continue at its current velocity: 0
                            Speed changes adjust the craft's velocity by
                            speed_increment, maxing out at max_speed.
         """

        pass
        # <STUDENT IMPLEMENTATION GOES HERE>

        return (0,0)
