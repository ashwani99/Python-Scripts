import time
import argparse

from win10toast import ToastNotifier

APP_NAME = 'Simple Timer'


def toast_when_finished(toast_duration, start_msg, end_msg):
    def decorator(f):
        toaster = ToastNotifier()
        def wrapper(*args, **kwargs):
            print(args)
            print(kwargs)
            # notify when timer starts
            params = args[0]
            toaster.show_toast(
                title=APP_NAME,
                msg=start_msg.format(params['hours'], params['minutes'], params['seconds']),
                duration=toast_duration,
                threaded=True
            )
            ret_val = f(*args, **kwargs)
            # notify after timer ends
            toaster.show_toast(
                title=APP_NAME,
                msg=end_msg,
                duration=toast_duration,
                threaded=True
            )
            print('all done')
            return ret_val
        return wrapper
    return decorator


@toast_when_finished(
    toast_duration=5,
    start_msg='Timer of {:02d} hours {:02d} minutes {:02d} seconds is running. Go do your job!',
    end_msg='Yo! your time is up lol')
def start_timer(duration):
    total_seconds = duration['hours']*3600 + duration['minutes']*60 + duration['seconds']
    time.sleep(total_seconds)


def show_countdown():
    pass
    

def main():
    parser = argparse.ArgumentParser(
        description='A utility timer alarm which notifies your Windows 10 machine when timer is finished'
    )

    parser.add_argument('-o', '--hours', action='store', type=int, default=0,
                        help='Duration of timer in hours')
    parser.add_argument('-m', '--minutes', action='store', type=int, default=5,
                        help='Duration of timer in minutes')
    parser.add_argument('-s', '--seconds', action='store', type=int, default=0,
                        help='Duration of timer in seconds')
    args = parser.parse_args()
    duration = vars(args)
    start_timer(duration)
    print('Yo! Your time is up!')


if __name__ == '__main__':
    main()


