import sys, codecs

from uuid import uuid4
from . import d


def obfuscate_file(filename):
    first_var = f"OBS332166891_{uuid4().hex}_w_o_w_o"
    second_var = f"t_e_k_{uuid4().hex}"
    
    try:
        file = open(filename)
        file.readlines()
    except:
        print(f"File {filename} Not Found !", file=sys.stderr)
        exit(0)
    
    with open(f"obf_{filename}", "w") as f:
        f.write(f"import codecs\n{first_var},{second_var} = ({d[1]},'''{d[0](open(filename).readlines())}''')\nexec({first_var}({second_var}))")


if __name__ == "__main__":
    for i in sys.argv[1::]:
        obfuscate_file(i)