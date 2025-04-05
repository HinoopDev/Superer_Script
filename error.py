# file stuff
def NoFile()->str: return f"ERROR:\nNo file given to compile.\nNo content to compile.\n\n"
def FileNotFound(file:str)->str: return f"ERROR:\nFile [{file}] not found.\nNo content to compile.\n\n"
def DirNotFound(file:str)->str: return f"ERROR:\nDirectory of the file [{file}] not found.\nCouldn't compile the file.\n\n"