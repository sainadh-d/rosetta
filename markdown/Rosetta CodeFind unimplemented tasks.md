# Rosetta Code/Find unimplemented tasks

## Task Link
[Rosetta Code - Rosetta Code/Find unimplemented tasks](https://rosettacode.org/wiki/Rosetta_Code/Find_unimplemented_tasks)

## Java Code
## Python Code
### python_code_1.txt
```python
"""
Given the name of a language on Rosetta Code,
finds all tasks which are not implemented in that language.
"""
from operator import attrgetter
from typing import Iterator

import mwclient

URL = 'www.rosettacode.org'
API_PATH = '/mw/'


def unimplemented_tasks(language: str,
                        *,
                        url: str,
                        api_path: str) -> Iterator[str]:
    """Yields all unimplemented tasks for a specified language"""
    site = mwclient.Site(url, path=api_path)
    all_tasks = site.categories['Programming Tasks']
    language_tasks = site.categories[language]
    name = attrgetter('name')
    all_tasks_names = map(name, all_tasks)
    language_tasks_names = set(map(name, language_tasks))
    for task in all_tasks_names:
        if task not in language_tasks_names:
            yield task


if __name__ == '__main__':
    tasks = unimplemented_tasks('Python', url=URL, api_path=API_PATH)
    print(*tasks, sep='\n')

```

### python_code_2.txt
```python
"""
Given the name of a language on Rosetta Code,
finds all tasks which are not implemented in that language.
"""
from functools import partial
from operator import itemgetter
from typing import (Dict,
                    Iterator,
                    Union)

import requests

URL = 'http://www.rosettacode.org/mw/api.php'
REQUEST_PARAMETERS = dict(action='query',
                          list='categorymembers',
                          cmlimit=500,
                          rawcontinue=True,
                          format='json')


def unimplemented_tasks(language: str,
                        *,
                        url: str,
                        request_params: Dict[str, Union[str, int, bool]]
                        ) -> Iterator[str]:
    """Yields all unimplemented tasks for a specified language"""
    with requests.Session() as session:
        tasks = partial(tasks_titles,
                        session=session,
                        url=url,
                        **request_params)
        all_tasks = tasks(cmtitle='Category:Programming_Tasks')
        language_tasks = set(tasks(cmtitle=f'Category:{language}'))
        for task in all_tasks:
            if task not in language_tasks:
                yield task


def tasks_titles(*,
                 session: requests.Session,
                 url: str,
                 **params: Union[str, int, bool]) -> Iterator[str]:
    """Yields tasks names for a specified category"""
    while True:
        request = session.get(url, params=params)
        data = request.json()
        yield from map(itemgetter('title'), data['query']['categorymembers'])
        query_continue = data.get('query-continue')
        if query_continue is None:
            return
        params.update(query_continue['categorymembers'])


if __name__ == '__main__':
    tasks = unimplemented_tasks('Python',
                                url=URL,
                                request_params=REQUEST_PARAMETERS)
    print(*tasks, sep='\n')

```

### python_code_3.txt
```python
import xml.dom.minidom
import urllib, sys
 
def findrc(category):
    name = "http://www.rosettacode.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:%s&cmlimit=500&format=xml" % urllib.quote(category)
    cmcontinue, titles = '', []
    while True:
        u = urllib.urlopen(name + cmcontinue)
        xmldata = u.read()
        u.close()
        x = xml.dom.minidom.parseString(xmldata)
        titles += [i.getAttribute("title") for i in x.getElementsByTagName("cm")]
        cmcontinue = filter( None,
                             (urllib.quote(i.getAttribute("cmcontinue"))
                              for i in x.getElementsByTagName("categorymembers")) )
        if cmcontinue:
            cmcontinue = '&cmcontinue=' + cmcontinue[0]
        else:
            break
    return titles
 
alltasks = findrc("Programming_Tasks")
lang = findrc(sys.argv[1])
 
for i in [i for i in alltasks if i not in lang]:
    print i

```

### python_code_4.txt
```python
#Aamrun, 3rd February 2023

import xml.dom.minidom
import sys, urllib.parse, urllib.request
 
def findrc(category):
    name = "http://www.rosettacode.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:%s&cmlimit=500&format=xml" % urllib.parse.quote(category)
    cmcontinue, titles = '', []
    while True:
        u = urllib.request.urlopen(name + cmcontinue)
        xmldata = u.read()
        u.close()
        x = xml.dom.minidom.parseString(xmldata)
        titles += [i.getAttribute("title") for i in x.getElementsByTagName("cm")]
        cmcontinue = list(filter( None,
                             (urllib.parse.quote(i.getAttribute("cmcontinue"))
                              for i in x.getElementsByTagName("categorymembers")) ))
        if cmcontinue:
            cmcontinue = '&cmcontinue=' + cmcontinue[0]
        else:
            break
    return titles
 
alltasks = findrc("Programming_Tasks")
lang = findrc(sys.argv[1])
 
for i in [i for i in alltasks if i not in lang]:
    print(i)

```

