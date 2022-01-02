import os


class FileWatcher(object):
    def __init__(self, filePath):
        self._cached_stamp = 0
        self.filename = filePath

    def HasChanged(self):
        lastModifiedTime = os.stat(self.filename).st_mtime

        flag = False
        if lastModifiedTime != self._cached_stamp:
            self._cached_stamp = lastModifiedTime
            flag = True
        return flag
