import sys
# from textnode import *
# from parentnode import *
# from leafnode import *
from utilities import *


def main():
    basepath = None
    if len(sys.argv)> 1:
        basepath = sys.argv[1]
    
    refresh_directory('./static', './docs')
    generate_pages_recursive('./content', './template.html', './docs', basepath)



main()