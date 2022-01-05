import logging, time

converter = time.localtime

class LogStashFormat(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%'):
        logging.Formatter.__init__(self, fmt, datefmt, style)

    def format(self,record: logging.LogRecord):
        rv = dict()
        rv['level'] = record.levelname
        rv['message'] = record.msg
        rv['name'] = record.name
        asctime = record.created
        if self.usesTime():
            asctime = self.formatTime(record, self.datefmt)
        rv['createAt'] = asctime
        return rv

    def getSettings(self):
        mapping = {"properties" : {"level" : {"type" : "keyword"},"message" : { "type" : "text"},"name":{"type":"keyword"} }}
        return {"mapping":mapping}
