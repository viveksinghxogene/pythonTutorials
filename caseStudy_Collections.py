list1 = ['python', 'django', 'docker', 'drf']

match list1:
    case ['python', 'django']:
        print("python and django")
    case ['django', 'docker']:
        print("django and docker")
    case ['docker', 'drf']:
        print("docker and drf")
    case ['python', 'django', 'docker', 'drf']:
        print('All courses are selected')
    case _:
        print('No course selected')