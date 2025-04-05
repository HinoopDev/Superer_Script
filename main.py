import sys

import error

import file_handler
import parser
import tokenizer
import constants


def handle_args(args:list[str])->dict:
    i = 0
    arg_dict = {}
    while i < len(args):
        if   args[i] == "-o" and not args[i+1].startswith("-"): arg_dict["o"] = args[i+1]; i+=2         # to compile file
        elif args[i] == "-t" and not args[i+1].startswith("-"): arg_dict["t"] = args[i+1]; i+=2         # compiled file position
        elif args[i] == "-s" and not args[i+1].startswith("-"): arg_dict["s"] = args[i+1]; i+=2         # run as shell
        else: continue
    if arg_dict.get("t") == None: arg_dict["t"] = arg_dict.get("o").replace(".ss", ".py") if arg_dict.get("o") != None else None
    arg_dict["s"] = "false"                                                                             # not employed yet
    return arg_dict


def main()->int:
    args = handle_args(sys.argv[1:])
    if len(sys.argv) < 2 or args.get("o") == None:
        print(error.NoFile())
        return -1
    if   args.get("s") == "true":...
    elif args.get("s") == "false": 
        file_content = file_handler.get(args.get("o"))
        if file_content.strip() == "": 
            file_handler.push(args.get("t"), file_content)
            return 0
        pass
        
    return 0




if __name__ == "__main__":
    print(f"compilation run with the exit code: {main()}")



    run = not True
    while run:
        ui = input("> ")
        pui = parser.parse(ui)
        print(pui)
        print(parser.parse("hello-world(was up)\n"))