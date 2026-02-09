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
        # zf.write ( sub, sub )
        # Read the data from the file
        mdfile = open ( sub )
        mdtext = mdfile.read()
        mdfile.close()
        # Write the Markdown text to the Zip file as it is
        # zf.writestr ( sub, mdtext )
        # Remove MarkDown formatting from mdtext
        text = mdtext.replace('\r','\n')
        # Remove triple back quotes
        text = '\n'.join ( [s.replace('```','') for s in text.split('\n')] )
        # Remove "# " used for indenting headings
        text = '\n'.join ( [s.replace('# ','') for s in text.split('\n')] )
        # Remove all other "#" headings
        text = '\n'.join ( [s.replace('#','') for s in text.split('\n')] )
        # Replace all links of the form "[text](link)" with "text: see link"
        new_s = []
        for s in text.split('\n'):
          # These tests are not conclusive but good enough for a quick demo
          if ('[' in s) and ('](' in s) and (']' in s):
            if s.index('](') >= 0:
              if s.index('[') >= 0:
                if s.index('[') < s.index(']('):
                  if s.rindex(')') > s.index(']('):
                    s = s.replace('[','')
                    s = s.replace('](', ": see ")
                    s = s.replace(')', '')
          new_s.append(s)
        text = '\n'.join ( new_s )
        # Replace specific GitHub user names here
        text = '\n'.join ( [s.replace('bobkuczewski','_username_') for s in text.split('\n')] )
        text = '\n'.join ( [s.replace('BobKuczewski','_UserName_') for s in text.split('\n')] )
        # Write the non-MarkDown text as a ".txt" file
        zf.writestr ( sub[0:-3]+".txt", text )


zf = zipfile.ZipFile ("md_doc_tree.zip","w", zipfile.ZIP_DEFLATED)
# zf.write ( "README.md", "README.md" )

add_md_recurse ( zf, "." )

zf.close()

# __import__('code').interact(local={k: v for ns in (globals(), locals()) for k, v in ns.items()})
