import nltk
import ssl

#https://stackoverflow.com/questions/41348621/ssl-error-downloading-nltk-data
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

#https://stackoverflow.com/questions/27658409/downloading-error-using-nltk-download
dler = nltk.downloader.Downloader()
dler._update_index()
dler._status_cache['panlex_lite'] = 'installed' # Trick the index to treat panlex_lite as it's already installed.
dler.download('all')
