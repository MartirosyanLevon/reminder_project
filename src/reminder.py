import click


def get_input(text):
    return input(text)


class Reminder:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def set_time(self):
        '''Nothing to receive,checking input time format
        if correct,returning time.  '''

        a = True
        while a:
            tim = get_input('Enter the time remind. for example (18:30) : ')
            while a:
                if len(tim) < 5:
                    click.secho(f'{tim} is too shorter:', fg='red')
                    break
                if len(tim) > 5:
                    click.secho(f'{tim} is too longer:', fg='red')
                    break
                if tim[2] != ':':
                    tim[2].replace(tim[2], ':')
                if tim[:2].isdigit() and tim[3:5].isdigit():
                    if int(tim[0]) > 1 and int(tim[1]) > 3:
                        click.secho(f'{tim} Wrong time format:')
                        break
                    if int(tim[3]) > 5:
                        click.secho(f'{tim} Wrong time format:')
                        break
                    a = False
                    self.times = tim
                else:
                    break
