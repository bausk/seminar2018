import sys
from PIL import Image
import io
import asyncio
from aiohttp import ClientSession
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
from q import AsyncProcessQueue

URL = "https://dog.ceo/api/breeds/image/random"


async def retrieve_url(queue):
    print('[1] Started as coroutine...')
    while True:
        await asyncio.sleep(1)
        print("[1] is publishing url to process")
        await queue.put(URL)


async def get_image(q_from, q_to):
    print('[2] Started as coroutine...')
    session = ClientSession()
    while True:
        data = await q_from.get()
        print('[2] is getting image from network')
        async with session.get(data) as r:
            result = await r.json()
            url = result['message']
            img = await session.get(url)
            print(url)
            image = await img.read()
        await q_to.coro_put(image)


def resize_img(q_from, q_to):
    print('[3] Started in subprocess...')
    while True:
        img_bytes = q_from.get()
        print('[3] is resizing on CPU in subprocess')
        if img_bytes is None:
            q_from.put(img_bytes)
            break
        image = Image.open(io.BytesIO(img_bytes)) #Why not before?
        image.thumbnail((128, 128), Image.ANTIALIAS)
        q_to.put(image)
    return True


async def publish_data(queue):
    print('[4] Started as coroutine...')
    while True:
        data = await queue.coro_get()  # Try getting here!
        print('[4] is printing image data')
        print('Thumbnail is {}x{}'.format(data.width, data.height))


async def process_data(in_queue, out_queue, loop):
    print('Creating {} IO-blocking tasks...'.format(cpu_count()))
    blocking_tasks = []
    executor = ProcessPoolExecutor(max_workers=cpu_count())
    for i in range(cpu_count()):
        blocking_tasks.append(asyncio.ensure_future(
            loop.run_in_executor(executor, resize_img, in_queue, out_queue)
            )
        )
    completed, pending = await asyncio.wait(blocking_tasks)
    results = [t.result() for t in completed]
    print(results)
    sys.stdout.flush()
    await out_queue.coro_put(None)
    return


if __name__ == "__main__":
    print('starting up...')

    queue_urls = asyncio.Queue(50)
    queue_images = AsyncProcessQueue(50)
    queue_thumbnails = AsyncProcessQueue(50)

    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.create_task(retrieve_url(queue_urls))
    loop.create_task(get_image(queue_urls, queue_images))
    loop.create_task(process_data(queue_images, queue_thumbnails, loop))
    loop.create_task(publish_data(queue_thumbnails))

    pending = asyncio.Task.all_tasks()
    print('firing up loop...')
    loop.run_until_complete(asyncio.gather(*pending))
