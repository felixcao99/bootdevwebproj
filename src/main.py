from textnode import *
from parentnode import *
from leafnode import *
from utilities import *

def main():
    refresh_directory('./public/static', './public')
    generate_pages_recursive('./content', './template.html', './public')
    # generate_page('./content/index.md', './template.html', './public/index.html')


main()