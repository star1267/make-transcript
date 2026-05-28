from getTranscript import MakeTranscript
from storage_handler import write_json
from pathlib import Path
import os 



if __name__ == "__main__":
    #// TODO It would be great if these could be commant window inputs
    file = "101Session2Block2" #Name of participants wav file

    currentDir = os.getcwd()
    wavpath = os.path.join(currentDir, 'WavFiles')
    transpath = os.path.join(currentDir, 'transcripts')

    try:
        os.mkdir(transpath)
        print(f"Directory '{transpath}' created successfully.")
    except FileExistsError:
        print(f"Directory '{transpath}' already exists.")



    def getTranscripts (file, wavpath): 
        # Create transcript for participant audiofile 
        filelist = [f"{file}.wav"]
 #make transcript
        if Path(f"{file}.json").exists(): 
            print ('transcript already exists')
        else: 
             
            partresponses = MakeTranscript (filelist , wavpath )
            os.chdir(transpath)
            write_json(f"{file}.json", partresponses) #Write transcript to json
            return partresponses 
        
    partresponses= getTranscripts(file, wavpath) #if not make the transcript 