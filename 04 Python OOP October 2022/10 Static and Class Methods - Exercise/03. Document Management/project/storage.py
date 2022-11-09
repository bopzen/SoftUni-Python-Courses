from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.find_category(category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.find_topic(topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = self.find_document(document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.find_category(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.find_topic(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.find_document(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        return self.find_document(document_id)

    def find_category(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                return category

    def find_topic(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                return topic

    def find_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        return '\n'.join(str(document) for document in self.documents)