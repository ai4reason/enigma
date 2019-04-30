#!/usr/bin/python

import sys

class Learner:
   
   def __init__(self):
      pass

   def efun(self):
      "E Prover weight function name."
      return "Enigma"

   def ext(self):
      "Model filename extension."
      return "ext"

   def name(self):
      return "learner"

   def train(self, f_in, f_mod):
      pass

   def build(self, f_in, f_mod, log=None):
      if log:
         log.write("\nTraining Enigma model (%s):\n\n" % f_in)
         oldout = sys.stdout
         sys.stdout = log
      ret = self.train(f_in, f_mod)
      if log:
         sys.stdout = oldout
      return ret

   def predict(self, f_in, f_mod):
      return {}

