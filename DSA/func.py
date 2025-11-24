def send_emails(name, email):
    return f'Email sended for {email}, named as {name}'

peoples = [
    {
        'name': 'pedro',
        'email': 'pedro@gmailcom'
    },
    {
        'name': 'cadu',
        'email': 'cadu@gmailcom'
    },
    {
        'name': 'rodrigo',
        'email': 'rodrigo@gmailcom'
    }
]

for people in peoples:
    sended_emails = send_emails(people['name'], people['email'])
    print(sended_emails)