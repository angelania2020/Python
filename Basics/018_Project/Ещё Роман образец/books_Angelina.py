print('Добро пожаловать в библиотеку!')
class Books:
    book=''
    author=''
    review=''
    buy=''
    def add_book(self,book):
        self.book=book
    def add_author(self,author):
        self.author=author
    def add_review(self,review):
        self.review=review
    def add_buy(self,buy):
        self.buy=buy
    def write_to_files:
        with open('bookbuy.txt','a',encoding=('utf-8-sig')) as s:
            s.write(str(book))
            s.write(';')
            s.write(str(buy))
        
    def display(self):
        print()
        
print("Если вы желаете добавить книгу в свою библитеку, нажмите 1.")
user=int(input())
if user==1:
    newbook=Books()
    newbook.add_book(input("Введите название новой книги: "))
    newbook.add_author(input("Введите автора новой книги: "))
    newbook.add_review(input("Введите описание новой книги: "))
    newbook.add_buy(input("Введите ссылку на покупку новой книги: "))
    newbook.write_to_files()

        
    
        
        
        
        
        
        
        
        
        
        
        