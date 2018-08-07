import sys

if sys.version_info[0] < 3:
    sys.path.append('..')
    PermissionError = IOError
    FileNotFoundError = IOError

else:
    PermissionError = PermissionError
    FileNotFoundError = FileNotFoundError
