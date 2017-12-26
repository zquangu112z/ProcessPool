import concurrent.futures
import glob
import time


def process_tasks(filename):
    time.sleep(2)
    return 2


if __name__ == '__main__':
    images = glob.glob("/home/zquangu112z/Fiisoft/process-pool/input/*.ppm")
    print("There are %d images" % len(images))
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # iterator = executor.map(process_tasks, images)
        # print(list(iterator))

        futures = {executor.submit(process_tasks, image) for image in images}
        concurrent.futures.wait(futures)

    end = time.time()
    print("Done task in %f seconds" % (end - start))
