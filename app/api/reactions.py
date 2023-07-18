from app.users.models import User


class ReactionsCache:
    """Class for storing reactions."""

    def __init__(self):
        self.reactions = {}

    def add_post_to_cache(self, post_id: int):
        """Adds post to cache."""
        if post_id not in self.reactions:
            self.reactions[post_id] = {
                'likes': set(),
                'dislikes': set(),
            }

    def add_like(self, post_id: int, user: User):
        """Adds like to post."""
        self.add_post_to_cache(post_id)
        self.reactions[post_id]['dislikes'].discard(user.email)
        self.reactions[post_id]['likes'].add(user.email)

    def add_dislike(self, post_id: int, user: User):
        """Adds dislike to post."""
        self.add_post_to_cache(post_id)
        self.reactions[post_id]['likes'].discard(user.email)
        self.reactions[post_id]['dislikes'].add(user.email)


reactions_cache = ReactionsCache()
