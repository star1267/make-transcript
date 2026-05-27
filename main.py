from getTranscript import MakeTranscript
from storage_handler import write_json



if __name__ == "__main__":
    #// TODO It would be great if these could be commant window inputs
    file = "101Session2Block1" #Name of participants wav file
    folderpath = 'R:\khri-mehta-lab\Experiments\Projects\Kappa Project\HHF_KappaYear2\ParticipantResponses' 

    def getTranscripts (file, folderpath): 
        # Create transcript for participant audiofile 
        filelist = [f"{file}.wav"]
        partresponses = MakeTranscript (filelist, folderpath) #make transcript
        write_json(f"{file}.json", partresponses) #Write transcript to json
        return partresponses 
        
    partresponses= getTranscripts(file, folderpath) #if not make the transcript 