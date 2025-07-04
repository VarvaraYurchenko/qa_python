import pytest
from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_valid_name_is_added(self, collector):
        collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in collector.books_genre

    def test_add_new_book_duplicate_is_not_added(self, collector):
        collector.add_new_book('Хроники Нарнии')
        collector.add_new_book('Хроники Нарнии')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('name',['', 'A' * 41])
    def test_add_new_book_invalid_name_is_not_added(self, name, collector):
        collector.add_new_book(name)
        assert name not in collector.books_genre