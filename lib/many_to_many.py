class Author:
    def __init__(self,name):
        self.name = name
        self._contracts = []

    def contracts(self):
        return self._contracts
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)
    
    def sign_contract(self, date, book, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def books(self):
        return [contract.book for contract in self._contracts]
  




class Book:
    def __init__(self,title, name = ""):
        self.title=title
        self.name = name
        self._contracts = []
        self._authors = []


    def contracts(self):
        return self._contracts
    
    def authors(self):
        return self._authors
    
    def add_author(self,author):
        self._authors.append(author)

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author) and isinstance(book, Book) and isinstance(date, str) and isinstance(royalties, int):
            self.author = author
            self.book = book
            self.date = date
            self.royalties = royalties
            author._contracts.append(self)
            book._contracts.append(self)
            book.add_author(author)
            Contract.all.append(self)
        else:
            raise Exception("Failed")

    
    @classmethod
    def contracts_by_date(cls,date):
        return sorted((contract for contract in cls.all if contract.date == date),key=lambda contract: contract.date)


