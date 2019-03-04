import time
import argparse

from win10toast import ToastNotifier

APP_NAME = 'Simple Timer'


def toast_when_finished(toast_duration, start_msg, end_msg):
    def decorator(f):
        toaster = ToastNotifier()
        def wrapper(*args, **kwargs):
            # notify when timer starts
            toaster.show_toast(
                title=APP_NAME,
                msg=start_msg,
                duration=toast_duration,
                threaded=True
            )
            ret_val = f(*args, **kwargs)
            time.sleep(2)
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
    toast_duration=1,
    start_msg='Timer of {} minute(s) is running. Go do your job!',
    end_msg='Yo! your time is up lol')
def start_timer(minutes):
    print('That\'s it, you\'ll be notified after {} minute(s)'.format(minutes))
    time.sleep(minutes*60)


def main():
    parser = argparse.ArgumentParser(
        description='A utility timer alarm which notifies your Windows 10 machine when timer is finished'
    )

    parser.add_argument('-o', '--hours', action='store', type=int, default=0,
                        help='Duration of timer in hours')
    parser.add_argument('-m', '--minutes', action='store', type=int, default=5,
                        help='Duration of timer in minutes')
    args = parser.parse_args()
    duration = args.hours*60 + args.minutes
    start_timer(duration)
    print('Yo! Your time is up!')


if __name__ == '__main__':
    main()


