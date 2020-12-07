import sys
import os

cur_dir = os.getcwd()
print(cur_dir)

sys.stdout = sys.stderr
sys.path.inser(0, cur_dir)

from run import app as application
