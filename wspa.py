import argparse
from libs.wspa import *

parser = argparse.ArgumentParser("WSPA programming language", description="Just a CLI tool for WSPA (swap01)")
parser.add_argument("-r", "--run", help='Runs a WSPA code.', dest='wspa_code')
parser.add_argument("--towspa", help='Converts a python code to wspa code.', dest='py_file')
parser.add_argument("--topython", help='Converts a wspa code to python code.', dest='wspa_file')

def main():
    args = parser.parse_args()
    py_file = args.py_file
    wspa_file = args.wspa_file
    wspa_code = args.wspa_code
    if (py_file):
        py_to_wspa(py_file)
    elif (wspa_file):
        wspa_to_py(wspa_file)
    elif (wspa_code):
        try:
            exec(wspa_to_pyc(wspa_code))
        except:
            print("There was an error in WSPA file!")
    else:
        print("")

if __name__ == "__main__":
    main()