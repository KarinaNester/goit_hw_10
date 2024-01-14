from authors.models import Author

def get_author(author_id):
    try:
        author = Author.objects.get(id=author_id)
        return author.fullname
    except Author.DoesNotExist:
        return None