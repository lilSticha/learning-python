
from unicodedata import name


def main():   
    name = input('Enter your full name: ')
    # check if name is empty or contains only whitespase
    if not name.strip():
        print('Error: Name cannot be empty or contain only whitespace')
        return
    else:
        name = name.strip().title()
    
    job = input('Enter your job position: ')
    # check if job is empty or contains only whitespace    
    if not job.strip():
        print('Error: Job position cannot be empty or contain only whitespace')
        return
    else:
        job = job.strip().lower()

    # Check if job is CEO, CTO, or CFO and convert to uppercase
    if job in ('ceo', 'cto', 'cfo'):
        job = job.upper()
    else:
        job = job.title()

    # using print_card function to print the card
    print_card(name, job)
    print_num_a(name)



def print_card(name, job):
    print('-------------------------')
    print(f'| {name:<23} |' + '\n' + f'| {job:<23} |')
    print('-------------------------')

def print_num_a(a:int)-> None:
    print(f"{a.count('a') + a.count('A')}")

#if __name__ == '__main__':
main()
