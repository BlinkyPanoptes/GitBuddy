import time
import sys

loading_done = 'False'

# Loading animation
def loading_screen(message):
    global loading_done

    loading_done = 'False'

    start_time = time.time()

    while time.time() - start_time < 2:
        sys.stdout.write(f'\r{message} |')
        sys.stdout.flush()
        time.sleep(0.1)

        sys.stdout.write(f'\r{message} /')
        sys.stdout.flush()
        time.sleep(0.1)

        sys.stdout.write(f'\r{message} -')
        sys.stdout.flush()
        time.sleep(0.1)

        sys.stdout.write(f'\r{message} \\')
        sys.stdout.flush()
        time.sleep(0.1)

    loading_done = 'True'

    sys.stdout.write(f'\r{message}Done!\n')