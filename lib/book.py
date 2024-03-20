#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self._title = title
        self._page_count = page_count
    
    @property
    def title(self):
        """The title property"""
        return self._title
        
    @title.setter
    def title(self, title):
        pass

    @property
    def page_count(self):
        """Page count property"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        """Page count must be an integer"""
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print('page_count must be an integer')
    
    def turn_page(self):
        print('Flipping the page...wow, you read fast!')