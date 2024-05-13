# DesignPatterns
Design Patterns in Python

### Design Patterns: SOLID, FACTORY

### Some Design Patterns in Python.

## Factory Design:
### In this Design Pattern, we create a Document Maker that allows the user to choose from available formats such as PDF, DOCX, and CSV.
This example demonstrates how to implement a factory pattern for generating different types of documents based on user input.

```python
from abc import ABC, abstractmethod
from docx import Document as word
from PyPDF2 import PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import csv
import os

class Document(ABC):
    @abstractmethod
    def create_document(self):
        pass

class PdfDocument(Document):

    def create_document(self, subject: str, content: str, filename: str):
        filepath = os.path.join(os.getcwd(), filename)
        c = canvas.Canvas(filename)
        c.setTitle(content)  # Set the PDF title as the content
        c.drawString(100, 750, "Subject: " + subject)  
        c.drawString(100, 730, "Content: " + content)  
        c.save()  # Save the PDF
        
        with open(filename, 'rb') as f:
            reader = PdfReader(f)
            writer = PdfWriter()
            for page in range(len(reader.pages)):
                writer.add_page(reader.pages[page])
            
            with open(filepath, 'wb') as output_pdf:
                writer.write(output_pdf)
        
        return filepath

class WordDocument(Document):

    def create_document(self, subject : str, content : str, filename : str) -> str:
        filepath = os.path.join(os.getcwd(), filename)
        doc = word()
        doc.add_heading(subject, level=1)
        doc.add_paragraph(content)
        doc.save(filepath)
        return filepath
        
class CSVDocument(Document):

    def create_document(self, filename : str, subject : str, content: list[str]) -> str:
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([subject])
            for line in content:
                csv_writer.writerow([line])  
        return filepath

class DocumentMaker(Document):
    
    @staticmethod
    def create_document(doc_type, *args, **kwargs):
        doc_types = {
            "pdf" : PdfDocument().create_document,
            "word" : WordDocument().create_document,
            "csv" : CSVDocument().create_document
        }

        document_creator = doc_types.get(doc_type)
        if document_creator: return document_creator(*args, **kwargs)
        else : raise ValueError("Document not supported")


# Type of usage:

DocumentMaker.create_document("word", subject="Design WORD file",filename="Word Factory Design file",content="A design patterns that can be use in code!")
DocumentMaker.create_document("pdf", subject="Design PDF file",filename="Word Factory Design file",content="A design patterns that can be use in code!")
DocumentMaker.create_document("csv", subject="Design CSV file",filename="Factory Design", content="A design pattern that")
```

## SOLID Design:
### In this Design Pattern, we aim to adhere to the principles of SOLID: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion.

This section will illustrate how these principles can be applied in designing software components.
### - SRP (Single Responsibility Principle)

```python
class Employee:
    def __init__(self, func_name, func_age):
        self.func_name = func_name
        self.func_age = func_age
        self.func_salary = 0

    def display_info(self):
        print(f'Employee Name: {self.func_name} - Age: {self.func_age} - Salary: {self.func_salary}')    
```


## - OCP (Open/Closed Principle)
### - Note: In Python, applying OCP can be limited due to the lack of support for abstract classes and abstract methods.
```python
class ReportGenerator:
    def generate(self, data, report_type):
        if report_type == "pdf":
            self.generate_pdf(data)
        elif report_type == "csv":
            self.generate_csv(data)
        else:
            print("Unsupported report format.")

    def generate_pdf(self, data):
        # Logic to generate PDF
        ...

    def generate_csv(self, data):
        # Logic to generate CSV
```


## - LSP (Liskov Substitution Principle)
### - Note: Although Python allows for inheritance and polymorphism, it's important to understand that the Liskov Substitution Principle heavily relies on developer discipline.
```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

## - Note: 
#### - While Python is a flexible and powerful language, the full application of SOLID can be challenging due to some limitations of the language
#### For example, Python lacks native support for interfaces, and therefore implementing the Interface Segregation Principle may be tricky
#### Additionally, the lack of static type checking can make it difficult to precisely apply the Liskov Substitution Principle
#### However, SOLID concepts are still valuable and can be adapted in ways that make sense within the context of Python



