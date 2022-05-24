import urllib
import json
import pandas as pd
from os.path import exists

def fetch_descriptor(desc):
    """
    Fetch the descriptor 'desc' from the ngdc.nooa.gov API.
    
    -------
    Returns: pandas dataframe
        Dataframe containing content contained within descriptor.        
    """
    
    filename = desc.replace('/','-')+'.json'
    url = f'https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/descriptors/{desc}'
    urllib.request.urlretrieve(url, filename)
    with open(filename,'r') as f:
        j_file = json.loads(f.read())
    return pd.json_normalize(j_file, record_path=['items'])



