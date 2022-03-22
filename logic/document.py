class Document:
    """
    Class used to represent a Document
    """

    def __init__(self, id_document: int, title_document: str = 'Title', num_document_pages: int = 0,
                 category: str = 'None', author: str = 'None'):
        """ Document constructor objet.

        :param id_document: id of document.
        :type id_document: int
        :param title_document: Title of document.
        :type title_document: str
        :param num_document_pages: Number of document pages.
        :type num_document_pages: int
        """
        self._id_document = id_document
        self._title_document = title_document
        self._num_document_pages = num_document_pages
        self._category = category
        self._author = author

    @property
    def id_document(self) -> int:
        """ Returns id document of the document.
        :returns: id of document.
        :rtype: int
        """
        return self._id_document

    @id_document.setter
    def id_document(self, id_document):
        """ The id of the document.
        :param id_document: id of document.
        :type: int
        """
        self._id_document = id_document

    @property
    def title_document(self):
        """ Returns title document of the document.
        :returns: title of document.
        :rtype: str
        """
        return self._title_document

    @title_document.setter
    def title_document(self, title_document):
        """ The title of the document.
        :param title_document: title of document.
        :type: str
        """
        self._title_document = title_document

    @property
    def num_document_pages(self):
        """ Returns num document pages of the document.
        :returns: num document pages of document.
        :rtype: int
        """
        return self._num_document_pages

    @num_document_pages.setter
    def num_document_pages(self, num_document_pages):
        """ The number of document pages of the document.
        :param num_document_pages: num of document pages of document.
        :type: int
        """
        self._num_document_pages = num_document_pages

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    def __str__(self):
        return '({0}, {1}, {2}, {3}, {4})'.format(self.id_document, self.title_document, self.num_document_pages, self.category, self.author)
