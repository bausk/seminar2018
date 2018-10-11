import asyncio
from time import sleep
from multiprocessing import Manager, cpu_count
from concurrent.futures import ThreadPoolExecutor


def AsyncProcessQueue(maxsize=0):
    m = Manager()
    q = m.Queue(maxsize=maxsize)
    return _ProcQueue(q)


class _ProcQueue(object):
    def __init__(self, q):
        self._queue = q
        self._real_executor = None
        self._cancelled_join = False

    @property
    def _executor(self):
        if not self._real_executor:
            self._real_executor = ThreadPoolExecutor(max_workers=cpu_count())
        return self._real_executor

    def __getstate__(self):
        self_dict = self.__dict__
        self_dict['_real_executor'] = None
        return self_dict

    def __getattr__(self, name):
        if name in ['qsize', 'empty', 'full', 'put', 'put_nowait',
                    'get', 'get_nowait', 'close']:
            return getattr(self._queue, name)
        else:
            raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, name))

    async def coro_put(self, item):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(self._executor, self.put, item)

    async def coro_get(self):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(self._executor, self.get)

    def cancel_join_thread(self):
        self._cancelled_join = True
        self._queue.cancel_join_thread()

    def join_thread(self):
        self._queue.join_thread()
        if self._real_executor and not self._cancelled_join:
            self._real_executor.shutdown()


async def _do_coro_proc_work(q, stuff, stuff2):
    ok = stuff + stuff2
    print("Passing %s to parent" % ok)
    sleep(10)
    await q.coro_put(ok)  # Non-blocking
    sleep(10)
    item = q.get()  # Can be used with the normal blocking API, too
    print("got %s back from parent" % item)


def do_coro_proc_work(q, stuff, stuff2):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_do_coro_proc_work(q, stuff, stuff2))

