# for colab
import os
from getpass import getpass
import urllib
from pathlib import Path
import shutil

refresh = True

here = Path.cwd().parts
print(f'Currently in directory {Path.cwd()}')
# this will tell us we are in colab
condition = refresh and here[-1] == 'boulton' and here[-2] == 'content'
if condition:
    os.chdir('..')
    print(Path.cwd())
    shutil.rmtree('boulton')
else:
  print(condition,'regeneration switch:',refresh,'in',here[-1],here[-2])
# test if in correct directory
if not Path.cwd().parts[-1] == 'boulton':
  if not Path('boulton/loaded.txt').exists():
    try:
      from google.colab import userdata
      password = userdata.get('pat_boulton:')
    except:
      password = getpass('Password: ')
      password = urllib.parse.quote(password) 
    os.system(f"git clone https://{password}:{password}@github.com/profLewis/boulton.git")
  
  os.chdir('boulton')  
  os.system("pwd")

