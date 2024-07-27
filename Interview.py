class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def balanced(brackets):
    while '()' in brackets or '[]' in brackets or '{}' in brackets:
        if '()' in brackets:
            brackets = brackets.replace('()', '')
        if '[]' in brackets:
            brackets = brackets.replace('[]', '')
        if '{}' in brackets:
            brackets = brackets.replace('{}', '')
    if brackets == '':
        return 'Сбалансировано'
    else:
        return 'Не сбалансировано'


print(balanced('(((([{}]))))'))
print(balanced('[([])((([[[]]])))]{()}'))
print(balanced('{{[()]}}'))

print(balanced('}{}'))
print(balanced('{{[(])]}}'))
print(balanced('[[{())}]'))