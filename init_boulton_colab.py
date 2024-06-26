# for colab
import os
from pathlib import Path
import sys

try:
  refresh = sys.argv[1]
except:
  refresh = False
  pass

print(f"refresh set {refresh}");

try:
  # ie this is colab
  os.chdir('/content')
  print("I think this is colab ...")
  from google.colab import drive
  if refresh:
    print(f"refresh set {refresh} so cleaning up ... ",end="")
    try:
      import shutil
      shutil.rmtree('boulton')
      print("done")
    except:
      pass

  from pathlib import Path
  if not Path('boulton').exists():
    # try to get the required token (used as a passwd)
    try:
      # in case token is stored as secret (pat_boulton)
      from google.colab import userdata
      password = userdata.get('pat_boulton:')
    except:
      from getpass import getpass
      import urllib
      password = getpass('Token: ')
      password = urllib.parse.quote(password)
    print(f"cloning github.com/profLewis/boulton.git ",end="")
    os.system(f"git clone https://{password}:{password}@github.com/profLewis/boulton.git")
    print(f"done")

  os.chdir('/content/boulton')
except:
  print("Either this is a local install or you entered an incorrect token ... please check.")
  pass

