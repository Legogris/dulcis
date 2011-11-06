from celery.decorators import task
from mandelweb import data
from mandelweb import mandel

@task
def getSet(start, end, resolution, iterations):
    almonds = data.getAlmonds(start, end)
    if almonds is None or len(almonds) < resolution*resolution:
        almonds = mandel.generateSet(start, end, resolution, iterations)
        data.insertAlmonds(almonds)
    return almonds