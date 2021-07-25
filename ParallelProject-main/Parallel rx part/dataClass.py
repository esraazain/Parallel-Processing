class News:
    def __init__(self,author,title,description,url,publishedAt,content):
        self.author= author
        self.title=title
        self.description=description
        self.url=url
        self.publishedAt=publishedAt
        self.content=content

   

    def __repr__(self):
        return "News('{}','{}','{}','{}','{}','{}')".format(self.author,self.title,self.description,self.url,self.publishedAt,self.content)