"""
Single Responsibility Principle:
A class should have one, and only one, reason to change.

Book Class does not follow SRP due to below reasons : 

A. For functions : getCurrentPage(), turnPage()
Reasons to change:
a. Pagination logic changes
b. Reading direction changes
This should belongs to separate class, which can be named as BookReader

B. For function getLocation()
Reason to change:
Library layout changes
Shelf system changes
This should belongs to separate class, which can be named as LibraryLocation

C. function save()
Reason to change:
File format changes
Storage path changes
This should belongs to separate class, which can be named as BookRepository
"""

from abc import ABC, abstractmethod

class Book:
 
    def getTitle():
        return "A Great Book"
 
    def getAuthor():
        return "John Doe"

    def turnPage():
        # pointer to next page
        pass
 
    def getCurrentPage():
        return "current page content"
 
    def getLocation():
        pass
        # returns the position in the library
        # ie. shelf number & room number

    def save():
        pass
        # $filename = '/documents/'. $this->getTitle(). ' - ' . $this->getAuthor();
        # file_put_contents($filename, serialize($this));

class Printer(ABC):
    @abstractmethod
    def printPage(page):
        pass

class PlainTextPrinter(Printer):
    def printPage(page):
        # echo $page;
        pass
 
class HtmlPrinter(Printer):
    def printPage(page):
        pass
        # echo '<div style="single-page">' . $page . '</div>';