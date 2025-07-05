import pytest
from main import BooksCollector

# Возвращает пустой экземпляр BooksCollector
@pytest.fixture
def collector():
    return BooksCollector()