import os
import json
from dotenv import load_dotenv

load_dotenv()

data_JSON = os.getenv('DATA_JSON')
data = json.loads(data_JSON)