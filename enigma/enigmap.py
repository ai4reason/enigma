import os

def sdbm(s):
   "Generic purpose string hash function (see http://www.cse.yorku.ca/~oz/hash.html)"
   h = 0
   for c in s:
      h = ord(c) + (h << 6) + (h << 16) - h
      h &= 0xFFFFFFFFFFFFFFFF
   return h

def fhash(s, base):
   return 1 + (sdbm(s) % base)

def load(f_map):
   emap = {}
   if not os.path.exists(f_map):
      return emap
   for line in file(f_map):
      if line.startswith("version"):
         continue
      # FIXME: load hashed stuff
      (fid,ftr) = line.strip().split("(")[1].split(",")
      fid = int(fid.strip(", "))
      ftr = ftr.strip('") .')
      emap[ftr] = fid
   return emap

def save(emap, f_map, version, hashing=None):
   out = file(f_map, "w")
   out.write('version("%s").\n' % version)
   if hashing:
      out.write('hash_base(%s).\n' % hashing)
      # informative hash dump to see collisions
      for x in sorted(emap):
         out.write('bucket(%s, "%s").\n' % (emap[x], x))
   else:
      rev = {emap[ftr]:ftr for ftr in emap}
      for x in sorted(rev):
         out.write('feature(%s, "%s").\n' % (x,rev[x]))
   out.close()

def create(pre, hashing=None):

   def add(features, new):
      for feature in new.strip().split(" "):
         if (not feature) or feature.startswith("$"):
            continue
         if "/" in feature:
            feature = feature.split("/")[0]
         features.add(feature)

   features = set()
   for pr in pre:
      (sign,clause,conj) = pr.strip().split("|")
      add(features, clause)
      add(features, conj)

   if hashing:
      return {f:fhash(f,hashing) for f in sorted(features)}
   else:
      return {y:x for (x,y) in enumerate(sorted(features), start=1)}

def join(f_maps):
   features = set()
   for f_map in f_maps:
      features.update(load(f_map).keys())
   return {y:x for (x,y) in enumerate(sorted(features), start=1)}

