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
        collector.add_new_book('Хроники Нарнии') # Добавляем книгу повторно
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

    # Проверяем, что get_book_genre возвращает корректный жанр
    def test_get_book_genre_returns_correct_genre(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    # Проверяем, что get_books_with_specific_genre возвращает корректные книги
    def test_get_books_with_specific_genre_returns_correct_books(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Десять негритят']

    # Проверяем, что get_books_genre возвращает корректный текущий словарь
    def test_get_books_genre_returns_correct_dict(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')
        expected_dict = {
            'Дюна': 'Фантастика',
            'Десять негритят': 'Детективы'
        }
        assert collector.get_books_genre() == expected_dict

    # Проверяем, что get_books_for_children исключает книги с возрастным рейтингом
    def test_get_books_for_children_without_age_rating(self, collector):
        collector.add_new_book('Каникулы Бонифация')
        collector.set_book_genre('Каникулы Бонифация', 'Мультфильмы')
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')
        collector.add_new_book('Трое в лодке, не считая собаки')
        collector.set_book_genre('Трое в лодке, не считая собаки', 'Комедии')
        assert collector.get_books_for_children() == ['Каникулы Бонифация', 'Трое в лодке, не считая собаки']
        assert 'Десять негритят' not in collector.get_books_for_children()

    # Проверяем, что add_book_in_favorites добавляет книгу в избранное
    def test_add_book_in_favorites_book_is_added(self, collector):
        collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_books_genre()
        collector.add_book_in_favorites('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

    # Проверяем, что add_book_in_favorites не добавляет повторно книгу в избранное
    def test_add_book_in_favorites_duplicate_is_not_added(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер') # Добавляем книгу в избранное повторно
        assert len(collector.get_list_of_favorites_books()) == 1

    # Проверяем, что delete_book_from_favorites удаляет книгу из избранного, когда она там есть
    def test_delete_book_from_favorites_book_is_deleted(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()

    # Проверяем, что get_list_of_favorites_books возвращает список избранных книг
    def test_get_list_of_favorites_books_returns_list_of_favorites(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Дюна')
        collector.add_new_book('Десять негритят')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер', 'Дюна']
