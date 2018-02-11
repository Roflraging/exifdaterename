import exifread
import sys
import os

for file_path in sys.argv[1:]:
    dir, filename = os.path.split(file_path)
    basename, extension = os.path.splitext(filename)
    f = open(file_path, 'rb')
    tags = exifread.process_file(f, details=False)
    date_time_original = tags['EXIF DateTimeOriginal']
    sub_sec_time_original = tags['EXIF SubSecTimeOriginal']
    new_basename = date_time_original.values.replace(':', '-') + '-' + sub_sec_time_original.values
    new_file_path = dir + '/' + new_basename + extension
    f.close()
    os.rename(file_path, new_file_path)
