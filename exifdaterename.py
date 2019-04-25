import exifread
import sys
import os

for file_path in sys.argv[1:]:
    # The absolute path should be retrieved to ensure that we
    # stick the renamed file in the same directory as the original
    # image.  If file_path is something like "DSC_001.NEF" then
    # dir is the empty string and new_file_path below is "/YYYY-MM-DD...NEF"
    # and the new file will just be at the root of the current drive.
    file_path = os.path.abspath(file_path)
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
