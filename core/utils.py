import os
from datetime import datetime

def get_filename(extension):
    ts = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return '%s%s' % (ts, extension)