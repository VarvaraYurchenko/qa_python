import pytest
from main import BooksCollector

class TestBooksCollector:
    # Проверяем, что книга с валидным названием добавляется в add_new_book
    def test_add_new_book_valid_name_is_added(self, collector):
        collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in collector.books_genre

    # Проверяем, что не происходит повторное добавление книги в add_new_book
    def test_add_new_book_duplicate_is_not_added(self, collector):
        collector.add_new_book('Хроники Нарнии')
        collector.add_new_book('Хроники Нарнии')
        assert len(collector.books_genre) == 1

    # Проверяем, что книга с невалидным именем (0 или больше 40 символов) не добавляется в add_new_book
    @pytest.mark.parametrize('name',['', 'A' * 41])
    def test_add_new_book_invalid_name_is_not_added(self, name, collector):
        collector.add_new_book(name)
        assert name not in collector.books_genre

    # Проверяем, что set_book_genre устанавливает жанр при использовании книги из books_genre и жанра из genre
    def test_set_book_genre_valid_genre_is_set(self, collector):
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')
        assert collector.books_genre['Десять негритят'] == 'Детективы'

    # Проверяем, что set_book_genre не устанавливает жанр при использовании невалидного жанра
    def test_set_book_genre_invalid_genre_is_not_set(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Новый жанр')
        assert collector.books_genre['Гарри Поттер'] == ''
