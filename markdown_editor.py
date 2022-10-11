class Command:

    help ='Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\nSpecial commands: !help !done'
    list_option = 'plain bold italic header link inline-code ordered-list unordered-list ' \
                  'new-line'.split()

    def __init__(self, com):
        self.com = com
        self.level = None
        self.text = None
        self.url = None

    def plan(self, text):
        self.text = text
        return self.text

    def bold(self, text):
        self.text = text
        return f'**{self.text}**'

    def inline_code(self, text):
        self.text = text
        return f'`{self.text}`'

    def link(self, text, url):
        self.text = text
        self.url = url
        return f'[{self.text}]({self.url})'

    def header(self, level, text):
        self.level = level
        self.text = text
        return f'{"#" * self.level} {self.text}\n'

    def new_line(self):
        return '\n'

    def italic(self, text):
        self.text = text
        return f'*{self.text}*'

    def option(self, text):
        self.text = text
        while True:
            number = int(input('Number of rows: '))
            if number > 1:
                break
            else:
                print('The number of rows should be greater than zero')

        if self.text == 'ordered-list':
            ordered = [f'{i}. {input(f"Row #{i}: ")}' for i in range(1, number + 1)]
            return '\n'.join(ordered) + '\n'
        elif self.text == 'unordered-list':
            unodered = [f'* {input(f"Row #{i}: ")}' for i in range(1, number + 1)]
            return '\n'.join(unodered) + '\n'


final_line = ''
while True:
    choose = input('Choose a formatter: ')
    db = Command(choose)
    if choose in db.list_option:
        if choose == 'header':
            while True:
                lev = int(input('Level: '))
                if lev in [i for i in range(1, 7)]:
                    break
                else:
                    print('The level should be within the range of 1 to 6')
            tex = input('Text: ')
            final_line += db.header(lev, tex)

        elif choose == 'plain':
            tex = input('Text: ')
            final_line += (db.plan(tex))

        elif choose == 'bold':
            tex = input('Text: ').strip().lower()
            final_line += (db.bold(tex))

        elif choose == 'link':
            label = input('Label: ')
            url_ = input('URL: ')
            final_line += (db.link(label, url_))

        elif choose == 'new-line':
            final_line += (db.new_line())

        elif choose == 'inline-code':
            tex = input('Text: ')
            final_line += (db.inline_code(tex))

        elif choose == 'italic':
            tex = input('Text: ')
            final_line += db.italic(tex)

        elif choose in 'unordered-list ordered-list'.split():
            tex = choose
            final_line += db.option(tex)

    elif choose == '!help':
        print(db.help)
    elif choose == '!done':
        with open('output.md', 'w') as file:
            file.write(final_line)
            break
    else:
        print('Unknown formatting type or command')

    print(final_line)



