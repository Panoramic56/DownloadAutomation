import os 
import shutil
import time
import colorama

class colors:
    Name = colorama.Fore.LIGHTYELLOW_EX
    Default = colorama.Fore.RESET
    Change = colorama.Fore.CYAN
    Empty = colorama.Fore.MAGENTA
    Err = colorama.Fore.RED
    Head = colorama.Fore.BLUE
    
colorama.init(convert=True)
mode = 0

def clear():
    os.system('cls||clear')

def ExcptShow():
    for e in Exception:
        print(colors.Err + 'Exception:' + e, end = '')

while True:
    path = input('Type the path adress: ')
    clear()
    while True:
        print(colors.Head + 'Path = ' + path + colors.Default)
        listdir = os.listdir(path)
        print('1 - Sort\n2 - Empty\n3 - Name\n4 - Repeated\n5 - Change Path\nMode: ', end = '')
        mode = int(input())

        if mode == 1:
            start = time.time()
            count = 1
            clear()
            while True:
                if time.time() - start >= 3600 or count == 1:
                    start = time.time()
                    listdir = os.listdir(path)
                    for fileY in listdir:
                        if 'utah' in fileY or 'Utah' in fileY or 'UTAH' in fileY or 'UoU' in fileY:
                            if fileY != 'Utah':
                                print(colors.Change + 'utah = ' + colors.Default + fileY)
                                shutil.move(path + fileY,  'D:\\Utah')

                    for fileX in listdir:
                        if '.' in fileX:
                            try:
                                if fileX.endswith('.pdf') or fileX.endswith('.png'):
                                    print(colors.Change + 'pdf  = ' + colors.Default + fileX)
                                    shutil.move(path + fileX,  'D:\\DownloadedPDFs')
                                elif fileX.endswith('.jpeg') or fileX.endswith('.jpg'):
                                    print(colors.Change + 'jpeg = ' + colors.Default + fileX)
                                    shutil.move(path + fileX, 'D:\\DownloadedJPEGs')
                                elif fileX.endswith('.docx') or fileX.endswith('.odt') or fileX.endswith('.doc'):
                                    print(colors.Change + 'docx = '+ colors.Default + fileX)
                                    shutil.move(path + fileX, 'D:\\DownloadedDocx')
                                elif fileX.endswith('.pptx') or fileX.endswith('.ppt'):
                                    print(colors.Change + 'pptx = ' + colors.Default + fileX)
                                    shutil.move(path + fileX, 'D:\\DownloadedPPt')
                                elif fileX.endswith('.xlsx'):
                                    print(colors.Change + 'xlsx = ' + colors.Default + fileX)
                                    shutil.move(path + fileX, 'D:\\DownloadedXlsx')
                                elif fileX.endswith('.LOG') or fileX.endswith('.txt') or fileX.endswith('.log'):
                                    print(colors.Change + 'log  = ' + colors.Default + fileX)
                                    shutil.move(path + fileX, 'D:\\DownloadedLog')
                                elif fileX.endswith('.tif'):
                                    print(colors.Change + 'tif  = ' + colors.Default + fileX)
                                    shutil.move(path + fileX, 'D:\\DownloadedTifs')
                                elif fileX.endswith('.dat') or fileX.endswith('.exe') or fileX.endswith('.tmp') or fileX.endswith('.mp3') or fileX.endswith('.css') or fileX.endswith('.html') or fileX.endswith('.wmv') or fileX.endswith('.docx#') or fileX.endswith('.odt#') or fileX.endswith('.mp4'):
                                    print(colors.Change + 'other  = ' + colors.Default + fileX)
                                    shutil.move(path + fileX, 'D:\\Other')
                            except:
                                ExcptShow()
                                continue
                    print('Operation completed\nIteration number = %i\n' % (count))
                    count += 1

        elif mode == 2:
            for i in listdir:
                try:
                    if '.' not in i:
                        print('FOLDER: %s' % (i))
                        if 'Projects' not in i and 'D:\\.Trash-1000' not in i:
                            for files in os.listdir(path + i):
                                try:
                                    print('\t' + files)
                                    shutil.move('D:\\' + i + '\\'+ files, path)
                                    print(colors.Empty + '\t\t moved %s to %s' % (files, path) + colors.Default)
                                except:
                                    continue
                except:
                    ExcptShow()
                    continue

        elif mode == 3:
            for i in listdir:
                if '.' not in i:
                    print(colors.Name + 'FOLDER: %s' % (i) + colors.Default)
                    if 'Projects' not in i:
                        if len(os.listdir(path + i)) == 0:
                            print(colors.Empty + '\tEMPTY FOLDER' + colors.Default)
                        for files in os.listdir(path + i):
                            print('\t' + files)
                    else:
                        print(colors.Empty + '\tPROTECTED FOLDER' + colors.Default)
                    print()

        elif mode == 4:
            repeated = []
            for i in listdir:
                if '.' not in i:
                    if 'Projects' not in i:
                        try:
                            for files in os.listdir(path + i):
                                if files in repeated:
                                    print(colors.Name + 'FOLDER: %s' % (i) + colors.Default)
                                    print(colors.Err + 'REPEATED: ' + colors.Default + files)
                                else:
                                    repeated.append(files)
                        except:
                            continue
        elif mode == 5:
            break