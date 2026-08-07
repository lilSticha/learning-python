name = input('Enter your full name: ')
name = name.strip().title()
job = input('Enter your jpb position: ')
job = job.strip().lower()
if job == 'ceo' or job == 'cto' or job == 'cfo':
    job = job.upper()
else:
    job = job.title()


def print_card(name, job):
    print('-------------------------')
    print(f'| {name:<23} |' + '\n' + f'| {job:<23} |')
    print('-------------------------')


print_card(name, job)
