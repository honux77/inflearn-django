class User:
    numUsers = 0
    def __init__(self, name):
        self.name = name
        self.articles = []
        User.numUsers += 1

    def write(self, text):
        self.articles.append(text)

    def __str__(self):
        articles_str = ", ".join(str(item) for item in self.articles)
        return "%s %s" % (self.name, articles_str)

class Text:
    def __init__(self, string):
        self.body = string

    def getLength(self):
        return len(self.body)

    def __str__(self):
        return self.body

class Article(Text):
    def __init__(self, title, body):
        self.title = title
        self.body = body
    def __str__(self):
        return "[%s] %s" % (self.title, self.body)

# t1 = Text('Hello')
t1 = Article("Good day", "It is good day to learn!")

user = User('Honux')
user.write(t1)
print("Number of User: ",User.numUsers)
print("User: ", user)
user2 = User('Crong')
print("Number of User: ",User.numUsers)
