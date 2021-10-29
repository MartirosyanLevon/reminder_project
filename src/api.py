import beepy
import click
import time

from multiprocessing import Process
from pynotifier import Notification

from reminder import Reminder

reminds = {}

local_time = time.localtime()
current_time = time.strftime("%H:%M",  local_time)
click.secho(current_time, fg='blue')


def set_remind():
    '''Don't receive an argument's,
    only returning key value and times.  '''

    key = click.prompt('Please add the title of remind')
    value = click.prompt('Please add the text', type=str)
    reminder = Reminder(key, value)
    reminder.set_time()
    return key, value, reminder.times


def remind_list(key, value, times):
    '''Receive parameters key,value and times,
    return reminds dict.  '''

    reminds[key] = {'value': value, 'times': times}
    return reminds


def view_reminds(reminds):
    '''Receive reminds dict,if is not empty showing
    remind title,text and time for alert.  '''

    if reminds == {}:
        click.secho("You haven't reminder_proj yet", fg='red')

    for key, val in reminds.items():
        click.secho(key, fg='green')
        click.secho(val['value'], fg='yellow')
        click.secho(val['times'], fg='red')


def del_remind(reminds, key_del):
    '''Receive reminds dict and key_del variable,
    if dict is not empty and key_del in dict  deleting,
    else showing wrong key,showing existing keys and asking
    try to input correct key.  '''

    print(reminds)
    while True:
        if reminds == {}:
            click.secho("You haven't reminder_proj yet", fg='red')
            break
        else:
            if key_del in reminds:
                val = reminds.pop(key_del)
                if val['process']:
                    val['process'].terminate()
                    while val['process'].is_alive():
                        continue
                    val['process'].close()
            else:
                click.secho(f"({key_del}),Not such remind,Please "
                            f"write a correct remind title", fg='red')
                view_reminds_keys(reminds)
                key_del = click.prompt('Please write the title of'
                                       'remind which do you want to delete')


def view_reminds_keys(reminds):
    '''Receive reminds dict,if is not empty
    showing  only dict keys.   '''

    if reminds == {}:
        click.secho("You haven't reminder_proj yet", fg='red')
    for k in reminds:
        click.secho(k, fg='green')


def remind(current_time, times, key, value):
    '''Receive current_time,times(time for alert),
    key(title in alert) and value(text in alert message).   '''

    while True:
        if times == current_time and reminds[key]['alive']:
            Notification(
                title=key,
                description=value,
                icon_path='/absolute/path/to/image/icon.png',
                duration=5,
                urgency='critical'
            ).send()
            beepy.beep(sound=6)
            reminds[key].update({'alive': False})
            break
        else:
            local_time = time.localtime()
            current_time = time.strftime("%H:%M", local_time)


if __name__ == '__main__':
    while True:
        if click.confirm('Do you want to add new remind ?'):
            key, value, times = set_remind()
            local_time = time.localtime()
            current_time = time.strftime("%H:%M", local_time)
            xp = Process(target=remind, args=(current_time,
                                              times, key, value), daemon=True)
            reminds[key] = {'value': value, 'times': times,
                            'process': xp, 'alive': True}
            xp.start()
        if click.confirm('Do you want to see your reminds ?'):
            view_reminds(reminds)
        if click.confirm('Do you want to delete your reminds ?'):
            key_del = click.prompt('Please write the title of'
                                   'remind which do you want to delete')
            del_remind(reminds, key_del)
