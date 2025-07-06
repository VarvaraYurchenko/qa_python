# sprint_4

# Тесты для приложения BooksCollector

## Описание реализованных тестов

1. *test_add_new_book_valid_name_is_added*  
Проверяет, что книга с валидным названием добавляется в add_new_book.

2. *test_add_new_book_duplicate_is_not_added*  
Проверяет, что не происходит повторное добавление книги в add_new_book.

3. *test_add_new_book_invalid_name_is_not_added*  
Проверяет, что книга с невалидным именем (пустая строка или больше 40 символов) не добавляется в add_new_book.
Используется параметризация.

4. *test_set_book_genre_valid_genre_is_set*  
Проверяет, что set_book_genre устанавливает жанр, если он входит в список допустимых.

5. *test_set_book_genre_invalid_genre_is_not_set*  
Проверяет, что set_book_genre не устанавливает жанр, если он не входит в список допустимых.

6. *test_get_book_genre_returns_correct_genre*  
Проверяет, что метод get_book_genre возвращает корректный жанр для указанной книги.

7. *test_get_books_with_specific_genre_returns_correct_books*  
Проверяет, что метод get_books_with_specific_genre возвращает правильный список книг по указанному жанру.

8. *test_get_books_genre_returns_correct_dict*  
Проверяет, что метод get_books_genre возвращает актуальный и корректный словарь книг с жанрами.

9. *test_get_books_for_children_without_age_rating*  
Проверяет, что метод get_books_for_children исключает книги с возрастным рейтингом.
Также проверяется отсутствие таких книг в результате.

10. *test_add_book_in_favorites_book_is_added*  
Проверяет, что метод add_book_in_favorites добавляет книгу в избранное, если она уже добавлена в список книг.

11. *test_add_book_in_favorites_duplicate_is_not_added*  
Проверяет, что метод add_book_in_favorites не добавляет повторно одну и ту же книгу.

12. *test_delete_book_from_favorites_book_is_deleted*  
Проверяет, что метод delete_book_from_favorites удаляет книгу из избранного, если она там есть.

13. *test_get_list_of_favorites_books_returns_list_of_favorites*  
Проверяет, что метод get_list_of_favorites_books возвращает список избранных книг.

