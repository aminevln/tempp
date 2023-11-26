import os
import colorama
import time
import sys
from colorama import  Fore,Style

try:
	import colorama
except ModuleNotFoundError:
	print("Requests is not Installed")
	os.system("pip install colorama")

link = (f"""xdg-open https://wa.me/393791841015/?text=ciao""")
