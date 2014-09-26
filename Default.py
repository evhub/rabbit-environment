from __future__ import with_statement, absolute_import, print_function, unicode_literals
from rabbit.all import *

class __rabbit__(object):
    def __init__(self, e):
        self.proc = e.processor
        self.sums = {}
        self.vars = {}
        self.fib = {}
    def call(self, params):
        if params == None:
            return matrix(0)
        else:
            self.v, self.proc.e.overflow = useparams(params, ["var", "x", "y"])
            self.start()
            out = self.find()
            if not out:
                return matrix(0)
            else:
                return out
    def start(self):
        if not self.v["var"]:
            self.v["var"] = 0
        else:
            self.v["var"] = int(self.v["var"])
        if self.v["x"]:
            self.v["x"] = float(self.v["x"])
        if self.v["y"]:
            self.v["y"] = float(self.v["y"])
    def find(self):
        if self.v["var"] == 0:
            return self.v["x"]*self.v["y"]
        elif self.v["var"] == 1:
            print("INPUT:")
            return strcalc(raw_input(), self.proc.e)
        elif self.v["var"] == 2:
            if not self.v["y"]:
                self.v["y"] = 0
            if self.v["x"] == 0:
                self.sums[self.v["y"]] = 0.0
                if self.proc.debug:
                    print("Running Sum On y-Channel:", self.v["y"])
            if self.v["x"] >= 0:
                self.sums[self.v["y"]] += self.v["x"]
                return self.sums[self.v["y"]]
            else:
                return 0.0
        elif self.v["var"] == 3:
            if self.v["y"]:
                self.vars[self.v["x"]] = self.v["y"]
                return self.v["y"]
            else:
                return haskey(self.vars, self.v["x"])
        elif self.v["var"] == 4:
            return len(str(int(self.v["x"])))
        elif self.v["var"] == 5:
            astring = str(int(self.v["x"]))
            bstring = str(int(self.v["y"]))
            while len(astring) > len(bstring):
                bstring = "0"+bstring
            while len(bstring) > len(astring):
                astring = "0"+astring
            return int("1"+astring+bstring)
        elif self.v["var"] == 6:
            return int(str(int(self.v["x"]))[1:(len(str(self.v["x"]))-1)/2])
        elif self.v["var"] == 7:
            return int(str(int(self.v["x"]))[(len(str(self.v["x"]))-1)/2+1:])
        elif self.v["var"] == 8:
            return self.getfib(int(self.v["x"]))
        else:
            return False
    def getfib(self, x):
        if x <= 2:
            return 1.0
        elif x in self.fib:
            return self.fib[x]
        else:
            self.fib[x] = self.getfib(x-2)+self.getfib(x-1)
            return self.fib[x]
