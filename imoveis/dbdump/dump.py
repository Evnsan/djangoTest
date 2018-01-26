import datetime, gzip, shutil, os

from django.core.management import call_command


def make_dump():
    timestamp = str(int(datetime.datetime.now().timestamp()))
    filename = 'db_' + timestamp + '.json'
    gz_filename = filename + '.gz'

    with open( filename, 'w') as f:
        call_command('dumpdata', exclude=['auth.permission','contenttypes'],
                 format='json', indent=3, stdout=f)
    with open( filename, 'rb') as f:
        with gzip.open(gz_filename, 'wb') as f_compress:
            shutil.copyfileobj(f, f_compress)
    os.remove(filename)

    return gz_filename




def load_dump(filename):
    call_command('loaddata', filename)
