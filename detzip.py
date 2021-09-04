#!/usr/bin/env python

import glob
import os
import zipfile

files = glob.glob('shared' + os.sep + '**', recursive=True)
files += glob.glob('client' + os.sep + 'configs' + os.sep + '**', recursive=True)
files += glob.glob('server' + os.sep + 'configs' + os.sep + '**', recursive=True)

files = sorted(files)

arcnames = []
for i in range(len(files)):
    if files[i].startswith('client' + os.sep):
        arcnames.append(files[i][len('client' + os.sep):])
    elif files[i].startswith('server' + os.sep):
        arcnames.append(files[i][len('server' + os.sep):])
    elif files[i].startswith('shared' + os.sep):
        arcnames.append(files[i][len('shared' + os.sep):])
    else:
        arcnames.append(files[i])

i = 0
seen = set()
with zipfile.ZipFile('soldat.smod', 'w') as smod:
    for file in files:
        if arcnames[i] not in seen:
            smod.write(file, arcname=arcnames[i])
            seen.add(arcnames[i])
        i += 1

    for zinfo in smod.infolist():
        zinfo.create_system = 0
        zinfo.date_time = (1980, 1, 1, 0, 0, 0)
