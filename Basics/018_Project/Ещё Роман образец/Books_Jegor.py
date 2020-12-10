# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:16:28 2020
@author: Jegor
"""

# Пользователь вводит название книги
book_name=input("Введите название книги")
book_name=book_name.casefold()
book_name=book_name.capitalize()
# Программа прочёсывает файлы, пытаясь найти автора, обзор и ссылку

# Автор

def get_autor():
    # Создаём список с элементами название;автор
    autor=open("books.txt","r",encoding=("utf-8"))
    autor_list=autor.read().splitlines()
    # определяем индекс элемента, который нам нужен
    for i in autor_list:
        if book_name in i:
            autor_index=autor_list.index(i)
            # создаём переменную с текстом название;автор
            autor_line=str(autor_list[autor_index])
            #отделяем имя автора от названия книги
            for i in range(0,len(autor_line)):
                if autor_line[i]==";":
                    autor=autor_line[i+1:len(autor_line)]
                    return autor
        
        
# Обзор
        
def get_review():
    # Создаём список с элементами название;обзор
    review=open("booksinfo.txt","r",encoding=("utf-8"))
    review_list=review.read().splitlines()
    # определяем индекс элемента, который нам нужен
    for i in review_list:
        if book_name in i:
            review_index=review_list.index(i)      
            # создаём переменную с текстом название;автор
            review_line=str(review_list[review_index])
            #отделяем имя автора от названия книги
            for i in range(0,len(review_line)):
                if review_line[i]==";":
                    review=review_line[i+1:len(review_line)]
                    return review
       
# Ссылка        
        
def get_link():
    # Создаём список с элементами название;ссылка
    link=open("bookbuy.txt","r",encoding=("utf-8"))
    link_list=link.read().splitlines()
    # определяем индекс элемента, который нам нужен
    for i in link_list:
        if book_name in i:
            link_index=link_list.index(i)      
            # создаём переменную с текстом название;автор
            link_line=str(link_list[link_index])
            #отделяем имя автора от названия книги
            for i in range(0,len(link_line)):
                if link_line[i]==";":
                    link=link_line[i+1:len(link_line)]
                    return link

#Проверка
def checkout():
    autor=open("books.txt","r",encoding=("utf-8"))
    autor_list=autor.read().splitlines()
    for i in autor_list:
        if book_name in i:
            break
        else:
            print("Книга не найдена")
            print()
            break
     
checkout()
autor=get_autor()
review=get_review()
link=get_link()
print("Автор этой книги: ",autor)
print("О чём эта книга: ",review)
print("Ссылка на скачивание: ",link)