Web Crawler Framework
This is a web crawler framework written in Python. It is designed to be highly available and easily extensible, with the following features:

Parser: responsible for extracting relevant data from the HTML content of a webpage
Store: responsible for storing the data extracted by the parser in a persistent storage like a database
Middleware: code that sits between the crawler and the parser/store to perform additional processing or handling of the data
Proxy pool: a pool of proxy servers that can be used to make HTTP requests through
Task queue: a queue that holds the URLs to be crawled, along with any additional metadata needed for the crawl
Crawler task: a class that represents a crawl task and provides an interface for interacting with the task (e.g. starting, stopping, getting status)
Usage
Here is an example of how to use the web crawler framework:
```python

import requests
from bs4 import BeautifulSoup
from webcrawler import Parser, Store, Middleware, ProxyPool, TaskQueue, CrawlerTask


class MyParser(Parser):
    def parse(self, html):
        # extract data from HTML using BeautifulSoup or similar library
        soup = BeautifulSoup(html, 'html.parser')
        data = {'title': soup.title.string}
        return data


class MyStore(Store):
    def store(self, data):
        # store data in a database or file
        pass


class MyMiddleware(Middleware):
    def process(self, data):
        # perform additional processing on data before storing it
        data['uppercase_title'] = data['title'].upper()
        return data


class MyProxyPool(ProxyPool):
    def get_proxy(self):
        # return a proxy server from the pool
        pass


class MyTaskQueue(TaskQueue):
    def __init__(self):
        self.queue = []

    def add_task(self, url, proxy=None):
        self.queue.append({'url': url, 'proxy': proxy})

    def get_task(self):
        return self.queue.pop(0)


# create a parser, store, and middleware
parser = MyParser()
store = MyStore()
middleware = MyMiddleware()

# create a proxy pool and task queue
proxy_pool = MyProxyPool()
task_queue = MyTaskQueue()

# add some tasks to the queue
task_queue.add_task('http://example.com/page1')
task_queue.add_task('http://example.com/page2', proxy=proxy_pool.get_proxy())

# create a crawler task
crawler_task = CrawlerTask(
    'http://example.com',
    parser,
    store,
    middleware=middleware,
    proxy_pool=proxy_pool,
    task_queue=task_queue
)

# start the task
crawler_task.start()

# stop the task
crawler_task.stop()

# get the status of the task
status = crawler_task.get_status()
print(status)  # {'stopped': True}

# create a parser, store, and middleware
parser = MyParser()
store = MyStore()
middleware = MyMiddleware()

# create a proxy pool and task queue
proxy_pool = MyProxyPool()
task_queue = MyTaskQueue()

# add some tasks to the queue
task_queue.add_task('http://example.com/page1')
task_queue.add_task('http://example.com/page2', proxy=proxy_pool.get_proxy())

# create a crawler task
crawler_task = CrawlerTask(
    'http://example.com',
    parser,
    store,
    middleware=middleware,
    proxy_pool=proxy_pool,
    task_queue=task_queue
)

# start the task
crawler_task.start()

# stop the task
crawler_task.stop()

# get the status of the task
status = crawler_task.get_status()
print(status)  # {'stopped': True}

```