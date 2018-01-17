from django.apps import AppConfig
import algoliasearch_django as algoliasearch

class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        blog=self.get_model('blog')
        algoliasearch.register(blog)