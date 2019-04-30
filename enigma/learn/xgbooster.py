import xgboost as xgb
from .learner import Learner

DEFAULTS = {
   'max_depth': 9, 
   'eta': 0.3, 
   'objective': 'binary:logistic', 
   'num_round': 200
}

class XGBooster(Learner):

   def efun(self):
      return "EnigmaXgb"

   def ext(self):
      return "xgb"

   def name(self):
      return "XGBoost"

   def __repr__(self):
      return "id string"

   def train(self, f_in, f_mod, params=None):
      dtrain = xgb.DMatrix(f_in)
      labels = dtrain.get_label()
      pos = float(len([x for x in labels if x == 1]))
      neg = float(len([x for x in labels if x == 0]))

      pars = dict(DEFAULTS)
      pars["scale_pos_weight"] = (neg/pos)
      if params:
         pars.update(params)
      num_round = pars["num_round"]
      del pars["num_round"]

      bst = xgb.train(pars, dtrain, num_round, evals=[(dtrain, "training")])
      bst.save_model(f_mod)
      return bst

