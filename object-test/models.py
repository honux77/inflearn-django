class Text:
    def __init__(self, str):
        self.text = str

    def __str__(self):
        return "Text: " + self.text

    def getLength(self):
        return len(self.text)

class Article(Text):
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __str__(self):
        return "Article %s %s" % (self.title, self.text)

class User:
    numUsers = 0
    # numArticle = 0
    def __init__(self, name):
        self.numArticle = 0
        self.name = name
        self.articles = []
        User.numUsers += 1

    def write(self, text):
        self.articles.append(text)
        self.numArticle += 1

    def __str__(self):
        return "User: %s %s" % (self.name, self.articles)

t = Article("hello", "This is some text")
t2 = Article("world", "This is some text2")
user = User('honux')
user.write(t)
user.write(t2)
print(t, t.getLength())
print(user, user.numArticle)
