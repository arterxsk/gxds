# WRITTEN BY MASTER 
# FOLLOW MY GITHUB : https://github.com/MASTER-404
#------------- IMPORT ------------#
from os import system as c
import marshal
import base64
import zlib

try:
    from Cython.Build.BuildExecutable import build as execute
except:
    c('pip install cython >/dev/null')
    
try:
    import os,cython
    from Cython.Build.BuildExecutable import build
except:
    os.system('pip install cython > /dev/null')
os.system('xdg-open https://github.com/MASTER-404') 


#---------------- LOGO -----------#
logo=("""
\033[1;91m  __  __           _____ _______ ______ _____   \x1b[1;90m 
\033[1;32m |  \/  |   /\    / ____|__   __|  ____|  __ \  \x1b[1;90m 
 \033[1;92m| \  / |  /  \  | (___    | |  | |__  | |__) | \x1b[1;90m 
\033[1;33m | |\/| | / /\ \  \___ \   | |  |  __| |  _  /  \x1b[1;90m 
\033[1;93m | |  | |/ ____ \ ____) |  | |  | |____| | \ \  \x1b[1;90m 
 \033[1;36m|_|  |_/_/    \_\_____/   |_|  |______|_|  \_\ \x1b[1;90m 
\033[1;96m==================================================
\x1b[1;36m{•} \x1b[1;93mTOOL AUTHER       \x1b[1;92m: ABDUL HAKIM  
\x1b[1;36m{•} \x1b[1;93mFACEBOOK          \x1b[1;92m: HAKIM KHAN 
\x1b[1;36m{•} \x1b[1;93mGITHUB NAME       \x1b[1;92m: \x1b[1;92mMASTER-404
\x1b[1;36m{•} \x1b[1;93mTOOL              \x1b[1;92m: COMPILE 
\x1b[1;36m{•} \x1b[1;93mI dont caree what then \033[;96mPeople Think About \033[;92m Me 
\033[1;96m==================================================
 """)



 
def line():
   print('\033[1;92m==================================================')      
    
#--------------- CLEAR FUNCTION -------------#
def clear():
    c('clear')
    print(logo)
    line()
    line()
#----------- MAIN FUNCTION ------------#


def main():
    clear()
    print(' \033[1;96m[1] Marshal ')
    print(' [2] Base64  ')
    print(' [3] Zlib    ')
    print(' [4] Cython  ')
    print(' [5] Cython1  ')
    print(' [0] Exit ')
    line()
    option=input('\033[1;93m [?] CHOICE MENU : ')
    if option in ['a','1']:
        marshal_enc()
    elif option in ['b','2']:
        base64_enc()
    elif option in ['c','3']:
        zlib_enc()
    elif option in ['d','4']:
        cython_executable()
    elif option in ['5','e']:
        cython1()
    else:
        exit(' TOOL EXITED :/')
#----------- MARSHAL ENCRYPTION --------------#
def marshal_enc():
    clear()
    file=input(' ENTER SOURCE FILE NAME : ')
    filex=input(' ENTER OUTPUT FILE NAME : ')
    try:
        file_open=open(file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR !!')
    compilex=compile(file_open,'dg','exec')
    dump=marshal.dumps(compilex)
    run_code=f'import marshal \nexec(marshal.loads({dump}))'
    out_put=open(filex,'w')
    out_put.write('#-------------------------------------##-------------------------------------#\n# ENCRYPTED BY : GXDS\n# GITHUB : HTTPS://GITHUB.COM/GOXDIES\n#-------------------------------------##-------------------------------------#\n\n')
    out_put.write(run_code)
    out_put.close()
    line()
    print(' [✓✓] ENCRYPTION COMPLETE :/ ')
    print(' [✓✓] OUTPUT FILE SAVE AS : '+filex)
#---------- BASE64 ENCRYPTION ------------#
def base64_enc():
    clear()
    input_file=input(' ENTER SOURCE FILE PATH : ')
    output_file=input(' ENTER OUTPUT FILE PATH : ')
    try:
        file_open=open(input_file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR !!')
    compile=base64.b64encode(file_open.encode())
    run_code=f'import base64\nexec(base64.b64decode({compile}))'
    out_put=open(output_file,'w')
    out_put.write('#-------------------------------------##-------------------------------------#\n# ENCRYPTED BY : GXDS\n# GITHUB : https://github.com/goxdies\n#-------------------------------------##-------------------------------------#\n\n')
    out_put.write(run_code)
    out_put.close()
    print(' [✓✓] ENCRYPTION COMPLETE :/')
    print(' [✓✓] ENC FILE SAVE AS : '+output_file)
#---------------- ZLIB ENCRYPTION -----------------#
def zlib_enc():
    clear()
    src=input(' ENTER SOURCE FILE PATH : ')
    save_file=input(' ENTER OUTPUT FILE PATH : ')
    try:
        src_file=open(src,'r').read()
    except:
        exit(' FILE NOT FOUND !!')
    compile_zlib=zlib.compress(src_file.encode())
    run_code=f'import zlib\nexec(zlib.decompress({compile_zlib}).decode())'
    out_put=open(save_file,'w')
    out_put.write('#-------------------------------------##-------------------------------------#\n# ENCRYPTED BY : ABDUL HAKIM\n# GITHUB : https://github.com/MASTER-404\n#-------------------------------------##-------------------------------------#\n\n')
    out_put.write(run_code)
    out_put.close()
    print(' [✓✓] ENCRYPTION COMPLETE :/')
    print(' [✓✓] ENC FILE SAVE AS : '+save_file)
#--------------- CYTHON EXECUTABLE -----------------#
def cython_executable():
        clear()
        os.system('xdg-open https://m.me/goxdies')       
        file = input(' Put File: ')
        try:
            open(file,'r').read()
        except:
            exit(' File Location Not Found ')
        os.system('cythonize -b '+file+'> /dev/null')
        input(' Your File Compile Done Enjoy ');main() 

#----------------- END --------------#

def cython1():
    clear()
    file=input(' ENTER SOURCE FILE PATH : ')
    try:
        filex=open(file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR :/')
    error=filex.replace('	','    ')
    solve=open(file,'w').write(error)
    execute(file)
    clear()
    print(' [✓✓] CYTHON EXECUTABLE COMPLETE :")')
    save=file[:-3]
    print(' [✓✓] EXECUTABLE FILE SAVE AS : '+save)
#----------------- END --------------#
main()
main()