from multiprocessing import Pool
import subprocess
from atpy import expres, eprover
import os

def proofstate(f_pre, f_pos, f_neg):
   def parse(clause):
      clause = clause[clause.rindex("proofvector")+12:].rstrip(",\n").strip().split(",")
      clause = [x.split("(")[0].split(":") for x in clause if x]
      clause = ["$%s/%s"%tuple(x) for x in clause if x]
      return " ".join(clause)
   pre = file(f_pre).read().strip().split("\n")
   pre = [x for x in pre if x]
   i = 0
   for pos in file(f_pos):
      pre[i] += " "+parse(pos)
      i += 1
   for neg in file(f_neg):
      pre[i] += " "+parse(neg)
      i += 1
   if i != len(pre):
      raise Exception("File %s does not match files %s and %s!" % (f_pre,f_pos,f_neg))
   file(f_pre, "w").write("\n".join(pre))

def prepare1(job):
   (bid, pid, problem, limit, version, force) = job

   f_problem = expres.benchmarks.path(bid, problem)
   f_cnf = expres.benchmarks.path(bid, "."+problem)+".cnf"
   if not os.path.isfile(f_cnf):
      file(f_cnf, "w").write(eprover.runner.cnf(f_problem))

   result = None
   #result = rkeys[(bid,pid,problem,limit)]
   f_pos = expres.results.path(bid, pid, problem, limit, ext="pos")
   f_neg = expres.results.path(bid, pid, problem, limit, ext="neg")
   if force or (not (os.path.isfile(f_pos) and os.path.isfile(f_neg))):
      result = expres.results.load(bid, pid, problem, limit, trains=True, proof=True)
      if force or not os.path.isfile(f_pos):
         file(f_pos, "w").write("\n".join(result["POS"]))
      if force or not os.path.isfile(f_neg):
         file(f_neg, "w").write("\n".join(result["NEG"]))
      # extract additional positive samples from the proof
      #f_sol = expres.results.path(bid, pid, problem, limit, ext="sol")
      #file(f_sol, "w").write("\n".join(result["PROOF"]))
      #f_prf = expres.results.path(bid, pid, problem, limit, ext="prf")
      #prf = file(f_prf, "w")
      #subprocess.call(["eprover", "--free-numbers", "--cnf", f_sol], stdout=prf)
      ##subprocess.call(["eprover", "--free-numbers", "--cnf", "--no-preprocessing", f_sol], stdout=prf)
      #prf.close()
      #os.system("cat %s | grep '^cnf' >> %s" % (f_prf, f_pos))
   
   f_pre = expres.results.path(bid, pid, problem, limit, ext="pre")
   if force or not os.path.isfile(f_pre):
      out = file(f_pre, "w")
      subprocess.call(["enigma-features", "--free-numbers", "--enigma-features=%s"%version, \
         f_pos, f_neg, f_cnf], stdout=out)
         #stdout=out, stderr=subprocess.STDOUT)
      out.close()
      if "W" in version:
         proofstate(f_pre, f_pos, f_neg)

def prepare(rkeys, version, force=False, cores=1):
   jobs = [rkey+(version,force) for rkey in rkeys]
   pool = Pool(cores)
   res = pool.map_async(prepare1, jobs).get(365*24*3600)
   pool.close()

def translate(f_cnf, f_conj, f_out):
   "deprecated?"

   out = file(f_out, "w")
   if not f_conj:
      subprocess.call(["enigma-features", "--free-numbers", f_cnf], stdout=out)
   else:   
      f_empty = "empty.tmp"
      os.system("rm -fr %s" % f_empty)
      os.system("touch %s" % f_empty)
      subprocess.call(["enigma-features", "--free-numbers", f_cnf, f_empty, f_conj], \
         stdout=out)
         #stdout=out, stderr=subprocess.STDOUT)
      os.system("rm -fr %s" % f_empty)
   out.close()

def make(rkeys, out=None):
   pre = []
   for (bid, pid, problem, limit) in rkeys:
      f_pre = expres.results.path(bid, pid, problem, limit, ext="pre")
      if out:
         tmp = file(f_pre).read().strip()
         if tmp:
            out.write(tmp)
            out.write("\n")
      else:
         pre.extend(file(f_pre).read().strip().split("\n"))
   return pre if not out else None

