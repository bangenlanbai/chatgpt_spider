import requests
from bs4 import BeautifulSoup


class Parser:
    def parse(self, html):
        # extract data from HTML using BeautifulSoup or similar library
        soup = BeautifulSoup(html, 'html.parser')
        data = {'title': soup.title.string}
        return data


class Store:
    def store(self, data):
        # store data in a database or file
        pass


class Middleware:
    def process(self, data):
        # perform additional processing on data before storing it
        data['uppercase_title'] = data['title'].upper()
        return data


class ProxyPool:
    def get_proxy(self):
        # return a proxy server from the pool
        pass


class TaskQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, url, proxy=None):
        self.queue.append({'url': url, 'proxy': proxy})

    def get_task(self):
        return self.queue.pop(0)


class CrawlerTask:
    def __init__(self, url, parser, store, middleware=None, proxy_pool=None, task_queue=None):
        self.url = url
        self.parser = parser
        self.store = store
        self.middleware = middleware
        self.proxy_pool = proxy_pool
        self.task_queue = task_queue
        self.stopped = False

    def start(self):
        while not self.stopped:
            # get next task from queue
            task = self.task_queue.get_task()
            if not task:
                break
            url = task['url']
            proxy = task['proxy']

            # use proxy if provided
            if proxy:
                response = requests.get(url, proxies={'http': proxy})
            else:
                response = requests.get(url)

            # parse and store data
            data = self.parser.parse(response.text)
            if self.middleware:
                data = self.middleware.process(data)
            self.store.store(data)

    def stop(self):
        self.stopped = True

    def get_status(self):
        return {'stopped': self.stopped}


# example usage
parser = Parser()
store = Store()
middleware = Middleware()
proxy_pool = ProxyPool()
task_queue = TaskQueue()

# add some tasks to the queue
task_queue.add_task('http://example.com/page1')
task_queue.add_task('http://example.com/page2', proxy=proxy_pool.get_proxy())

# create a crawler task
crawler_task = CrawlerTask(
    'http://example.com',
    parser,
    store,
    middleware=middleware,
    proxy_pool=proxy_pool
)

# start the task
crawler_task.start()

# stop the task
crawler_task.stop()

# get the status of the task
status = crawler_task.get_status()
print(status)  # {'stopped': True}

