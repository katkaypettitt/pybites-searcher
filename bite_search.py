import json
from pprint import pprint

# TODO: Put json file name in variable below
pybites_json = ''

with open(pybites_json, 'r') as f:
    data = json.load(f)

bites = data['bites']

print('''Welcome to Bite Search. How can I help you?
Enter "1" if you want to search via Bite number.
Enter "2" if you want to search via Learning Path.
Enter "3" if you want to search via tag.
Enter "4" if you want to see all completed Bites.
Enter "5" if you want to see all Bites.
Enter "exit" to quit.''')

while True:
    command = input('> ')

    if command == '2':
        print('Here is a list of all of the Learning Paths:')
        print('Algorithms')
        print('Bioinformatics')
        print('Collections Module')
        print('Data Analysis')
        print('Data Formats')
        print('Datetimes and Timezones')
        print('Decorators and Context Managers')
        print('Itertools')
        print('Object Oriented Programming')
        print('Pytest')
        print('Python Beginner')
        print('Regular Expressions')
        print('String Manipulation')
        print('Web Scraping')
        print()
        print('Which path would you like to look at?')

        wanted_path = input('> ')

        full_list = []
        for bite in bites:
            if wanted_path in bite['in_paths'].split(','):
                full_list.append(bite['bite'])

        completed_list = []
        for bite in bites:
            if wanted_path in bite['in_paths'].split(',') and bite['completed'] is True:
                completed_list.append(bite['bite'])

        print(f'Here is a list of all Bites in the "{wanted_path}" Learning Path.')
        print('\n'.join(full_list))
        print()
        print(f'Here is a list of all completed Bites in the "{wanted_path}" Learning Path.')
        print('\n'.join(completed_list))
        print()
        print('Do you want to view the code for one of these Bites? [y/n]')

    if command == '1' or command == 'y':
        print('Please type the Bite number you are searching for.')
        bite_number = input('> ')
        try:
            wanted_bite = f'Bite {bite_number}.'
            specific_bite_name = []
            specific_bite_code = []
            for bite in bites:
                if bite['bite'].startswith(wanted_bite):
                    specific_bite_name.append(bite['bite'])
                    specific_bite_code.append(bite['passing_code'])
            print(specific_bite_name[0])
            print(specific_bite_code[0])
        except IndexError:
            wanted_bite = f'Intro Bite {bite_number}.'
            specific_bite_name = []
            specific_bite_code = []
            for bite in bites:
                if bite['bite'].startswith(wanted_bite):
                    specific_bite_name.append(bite['bite'])
                    specific_bite_code.append(bite['passing_code'])
            print(specific_bite_name[0])
            print(specific_bite_code[0])
        print()
        print('Do you want to view the code for another Bite? [y/n]')

    if command == '3':
        tags = []
        for bite in bites:
            tag_list = bite['tags'].split()
            tags.append(tag_list)

        tag_set = sorted(set(item for subl in tags for item in subl))

        print('There are over 200 tags used for Bites. Here they are:')
        pprint(tag_set, compact=True)
        print()
        print('Please enter the tag you would like to search under.')

        wanted_tag = input('> ')
        print(f'Here are all of the Bites with the tag "{wanted_tag}":')
        for bite in bites:
            if wanted_tag in bite['tags'].split():
                print(bite['bite'])

        print()
        print('Do you want to view the code for a Bite? [y/n]')

    if command == '4':
        completed_bites = []
        for bite in bites:
            if bite['completed'] is True:
                completed_bites.append(bite)
        print(f'There are {len(completed_bites)} completed Bites in total. Are you sure? [y/n]')
        command = input('> ')
        if command == 'y':
            pprint(completed_bites)
        else:
            print('No problem. Goodbye!')
            break

    if command == '5':
        print(f'There are {len(bites)} Bites in total. Are you sure? [y/n]')
        command = input('> ')
        if command == 'y':
            pprint(bites)
        else:
            print('No problem. Goodbye!')
            break

    if command == 'exit' or command == 'n':
        print('No problem. Goodbye!')
        break
