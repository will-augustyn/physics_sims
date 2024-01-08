import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

class Field:
    def __init__(self, pts, Vo, Vi):
        self.pts = pts
        self.Vo = Vo
        self.Vi = Vi
        self.grid = [[''] * self.pts for x in range(self.pts)]
    
    def __repr__(self):
        s = ''
        for r in range(self.pts):
            for c in range(self.pts):
                rounded = round((self.grid[r][c]), 1)
                s += str(rounded) + ' '
                if c == self.pts - 1:
                    s += '\n'
        return s
    
    def make_initial_field(self):
        for r in range(self.pts):  
            for c in range(self.pts):
                if r == 0 or r == self.pts-1:
                    self.grid[r][c] = self.Vo
                elif r in range((self.pts//2)-2,(self.pts//2)+3 ) and c in range((self.pts//2)-2,(self.pts//2)+3 ):
                    self.grid[r][c] = self.Vi
                    self.grid[r][0] = self.Vo 
                    self.grid[r][-1] = self.Vo
                else:
                    self.grid[r][0] = self.Vo 
                    self.grid[r][-1] = self.Vo
                    if self.grid[r][c] == '':
                        self.grid[r][c] = 0
    
    def find_field(self):
        diff = abs(self.Vo-self.Vi)
        passes = 0
        while passes<1000:
            for r in range(len(self.grid)):  
                for c in range(len(self.grid)):
                    if abs(self.grid[r][c]) != self.Vo and self.grid[r][c] != self.Vi:
                        near = [self.grid[r+1][c], self.grid[r-1][c], self.grid[r][c+1], self.grid[r][c-1]]
                        avg = sum(near)/4
                        self.grid[r][c] = avg
            passes += 1
                        
    def electric_potential(self):
        array = np.array(self.grid)
        gradient = np.gradient(array)
        x_E = -1*gradient[0]
        y_E = -1*gradient[1]
        plt.quiver(y_E, x_E)

class Field2(Field):
    def make_initial_field(self):
        for r in range(self.pts):  
            for c in range(self.pts):
                if r == 0 or r == self.pts-1:
                    self.grid[r][c] = self.Vo
                else:
                    self.grid[r][0] = -self.Vo 
                    self.grid[r][-1] = -self.Vo
                    if self.grid[r][c] == '':
                        self.grid[r][c] = 0
                        
    def find_field(self):
        diff = abs(self.Vo-self.Vi)
        passes = 0
        while passes < 1000:
            for r in range(len(self.grid)):  
                for c in range(len(self.grid)):
                    if abs(self.grid[r][c]) != self.Vo:
                        near = [self.grid[r+1][c], self.grid[r-1][c], self.grid[r][c+1], self.grid[r][c-1]]
                        avg = sum(near)/4
                        self.grid[r][c] = avg
            passes += 1
