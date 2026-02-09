#!/usr/bin/python

import os
import sys
import math
import zipfile

print ( str(os.getcwd()) )
os.chdir ( ".." )
print ( str(os.getcwd()) )

def add_md_recurse ( zipfile, folder ):
  folders = os.listdir ( folder )
  print ( "add all from " + folder + " containing " + str(folders) )
  for f in folders:
    if not f in ['.git', 'code']:
      sub = folder + os.path.sep + f
      print ( "Looking at " + sub )
      if os.path.isdir(sub):
        print ( sub + " is dir" )
        add_md_recurse ( zipfile, sub )
      elif sub.endswith(".md"):
        if sub.startswith("./"):
          # Remove leading "./" if found
          sub = sub[2:]
        print ( "Adding " + sub )
        zf.write ( sub, sub )

zf = zipfile.ZipFile ("md_doc_tree.zip","w", zipfile.ZIP_DEFLATED)
# zf.write ( "README.md", "README.md" )

add_md_recurse ( zf, "." )

zf.close()

__import__('code').interact(local={k: v for ns in (globals(), locals()) for k, v in ns.items()})
