# for colab
import os
from pathlib import Path

try:
  # ie this is colab
  os.chdir('/content')
  print("I think this is colab ...")
  if refresh:
    print(f"refresh set {refresh} so cleaning up ...")
    try:
      import shutil
      shutil.rmtree('boulton')
    except:
      pass
  else:
    print(f"refresh set {refresh}");

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
      password = getpass('Password: ')
      password = urllib.parse.quote(password)
    os.system(f"git clone https://{password}:{password}@github.com/profLewis/boulton.git")
except:
  pass

