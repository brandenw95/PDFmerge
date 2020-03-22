from PyPDF2 import PdfFileMerger
import os
from tqdm import tqdm
import time
import sys



def main():

    #Program startup
    os.system('mode con: cols=80 lines=4')
    os.system("color 0a")
    print('Converting, please wait....')
    print('')

    # Add all pdfs in dir to list
    pdfs = os.listdir()
    filename = os.path.basename(__file__)
    exe_filename = str(filename[:-3]) + '.exe'

    output_filename = 'results.pdf'
    count = 1

    #Remove name of this script from list
    if filename in pdfs:
        pdfs.remove(filename) 
    
    #Remove name of this script from list if converted to exe
    if exe_filename in pdfs:
        pdfs.remove(exe_filename)

    #If ran twice, remove 
    if output_filename in pdfs:
        pdfs.remove(output_filename)
        output_filename = 'results-' + str(count) + '.pdf' 
        count = count + 1

    #Sort all pages 
    pdfs = sorted(pdfs)

    #Create a merge object
    merger = PdfFileMerger(strict = False)

    #Merge
    for pdf in tqdm(pdfs):
        time.sleep(0.5)
        merger.append(pdf)

    #Write and close the file and program
    merger.write(output_filename)
    merger.close()
    sys.exit()



if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback
        traceback.print_exc()
        input("Program crashed; press Enter to exit")