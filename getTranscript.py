from elevenlabs.client import ElevenLabs
import yaml
from dotenv import load_dotenv
from io import BytesIO
import os 
import string

def MakeTranscript(fileName, foldername): 
    '''Makes transcript of wav files'''
    
    def transcribe(audio_file_path, elevenlabs): #input wav files and api key
        os.chdir(foldername) #Path to wav file
        with open(audio_file_path, 'rb') as audio_file: #Load information of wav file 
            result = elevenlabs.speech_to_text.convert(
                file=audio_file, #What file is being loaded
                model_id='scribe_v2', #which elevenlabs model is being used
                diarize=True, #true so that the model distiguishes between speakers
                timestamps_granularity='word'
            )
            return result
    # Process the response


    def create_conversation_transcript(result):
        """Create a conversation-style transcript with speaker labels"""
        all_words = [] #create empty list
        if hasattr(result, 'words'):
            # Collect all words from all channels
                for word in result.words or []: #cycle through all the words in the wav file
                    if word.type == 'word': #Add all the words to one big list with speaker name and time stamp
                        text = word.text 
                        translator = str.maketrans('', '', string.punctuation)
                        clean_text = text.translate(translator)
                        all_words.append({ #Create a dict of all the words 
                            'text': clean_text,
                            'start': word.start,
                            'speaker_id': word.speaker_id,
                        })
        # Sort by timestamp
        all_words.sort(key=lambda w: w['start']) #orders by timestamp
        # Group consecutive words by speaker
        conversation = []
        current_speaker = None
        current_text = [] 
        # Combine words into sentences based on speaker 
        for word in all_words: #loop through each word
            if word['speaker_id'] != current_speaker: #If speakers are different
                if current_text: #Appends to a new list
                    conversation.append({
                        'speaker': current_speaker, #dict with key of speaker
                        'text': current_text #dict with key of text
                    })
                current_speaker = word['speaker_id'] #Set new speaker to the speaker of this word
                current_text = [word['text']] #Set new current text to this word
            else:
                current_text.append(word['text']) #If words have same speaker they append to a list
        # Add the last segment
        if current_text:
            conversation.append({
                'speaker': current_speaker,
                'text': current_text
            })
        return conversation
    # Format the output



    with open ('secrets.yaml', 'r') as f:  #opens yaml with apikey
        secrets = yaml.safe_load(f)
    apikey = (secrets ['secrets'] ['elevenlabs']['apikey']) #read and store API key
    elevenlabs = ElevenLabs( #tells 11labs what the api key is 
        api_key= apikey,
    )

    for file in fileName: 
        result = transcribe(file, elevenlabs)
        filetranscript = create_conversation_transcript(result)

    return (filetranscript)    