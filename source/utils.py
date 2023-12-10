import os
import datetime
import json

def load_json(filepath: str):
    with open(filepath, 'r') as j:
         json_dict = json.loads(j.read())

    return json_dict

def get_filename(prefix: str = None):
    if prefix==None or prefix=='':
        prefix = ''
    else:
        prefix += '_'

    # Get datetime
    filename_datetime = str(datetime.datetime.now()).replace(' ', '_').replace('.', '_').replace('-', '').replace(':', '')

    # Generate file name
    filename = prefix + filename_datetime + '.json'

    return filename

def save_webpage_local_storage(save_to_path: str, filename: str, webpage: dict):
    # Convert into JSON:
    webpage_json = json.dumps(webpage)
    
    # Get download filepath
    filepath = os.path.join(save_to_path, filename)

    # Check if the directory exists
    if not os.path.exists(save_to_path):
        # If it doesn't exist, create it
        os.makedirs(save_to_path)

    # Save to a new file
    with open(filepath, "w") as text_file:
        text_file.write(webpage_json)

def save_webpage(url: str, html: str, save_to_path: str, filename: str):
        
    # Create the webpage dict
    webpage = {
            'url': url,
            'downloaded_datetime': str(datetime.datetime.now()),
            'html': html
    }
    
    # Save file
    save_webpage_local_storage(save_to_path, filename, webpage)
