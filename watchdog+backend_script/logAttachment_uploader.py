import logging
from datetime import datetime
import os

def logpath():
    pathlog = r'/home/arcgis/fileUploader_app/logs'
    return pathlog

class create_logAttachment():
    def logdebug(msg):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('Log_Uploader '+time+'.log')
        path = logpath()
        fullpath = '%s/%s'%(path, logfile)

        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []

        main.setLevel(logging.DEBUG)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.debug(msg)
        main.removeHandler(handler)
        del main, handler
    
    def loginfo(msg):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('Log_Uploader '+time+'.log')
        path = logpath()
        fullpath = '%s/%s'%(path, logfile)

        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []

        main.setLevel(logging.INFO)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.info(msg)
        main.removeHandler(handler)
        del main, handler

    def logwarning(msg):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('Log_Uploader '+time+'.log')
        path = logpath()
        fullpath = '%s/%s'%(path, logfile)

        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []
        
        main.setLevel(logging.WARNING)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.warning(msg)
        main.removeHandler(handler)
        del main, handler
    
    def logerror(msg):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('Log_Uploader '+time+'.log')
        path = logpath()
        fullpath = '%s/%s'%(path, logfile)

        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []

        main.setLevel(logging.ERROR)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.error(msg)
        main.removeHandler(handler)
        del main, handler

    def logcritical(msg):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('Log_Uploader '+time+'.log')
        path = logpath()
        fullpath = '%s/%s'%(path, logfile)
        
        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []

        main.setLevel(logging.CRITICAL)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.critical(msg)
        main.removeHandler(handler)
        del main, handler

class create_logUPLOAD():
    def logdebug(msg):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('UPLOADER '+time+'.log')
        path = logpath()
        fullpath = '%s/%s'%(path, logfile)

        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []

        main.setLevel(logging.DEBUG)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.debug(msg)
        main.removeHandler(handler)
        del main, handler
    
    def loginfo(msg):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('UPLOADER '+time+'.log')
        path = logpath()
        fullpath = '%s/%s'%(path, logfile)

        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []

        main.setLevel(logging.INFO)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.info(msg)
        main.removeHandler(handler)
        del main, handler

    def logwarning(msg):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('UPLOADER '+time+'.log')
        path = logpath()
        fullpath = '%s/%s'%(path, logfile)

        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []
        
        main.setLevel(logging.WARNING)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.warning(msg)
        main.removeHandler(handler)
        del main, handler
    
    def logerror(msg):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('UPLOADER '+time+'.log')
        path = logpath()
        fullpath = '%s/%s'%(path, logfile)

        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []

        main.setLevel(logging.ERROR)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.error(msg)
        main.removeHandler(handler)
        del main, handler

    def logcritical(msg):
        date = datetime.today()
        time = datetime.strftime(date, '%Y-%m-%d')

        logfile = ('UPLOADER '+time+'.log')
        path = logpath()
        fullpath = '%s/%s'%(path, logfile)
        
        main = logging.getLogger(__name__)
        if main.hasHandlers():
            # Logger is already configured, remove all handlers
            main.handlers = []

        main.setLevel(logging.CRITICAL)
        handler = logging.FileHandler(fullpath)

        format = logging.Formatter('%(asctime)s  %(name)s %(levelname)s: %(message)s')
        handler.setFormatter(format)

        main.addHandler(handler)
        return main.critical(msg)
        main.removeHandler(handler)
        del main, handle