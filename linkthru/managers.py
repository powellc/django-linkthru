from django.db import models

class LinkThruManager(models.Manager):
    """ A Custom Manager for link thrus """

    def get_random_link(self, link_zone):
        """
        Returns a random linkthru that belongs to the specified zone
        
        """
        try:
            link = self.get_query_set().filter(zone__slug=link_zone, enabled=True).order_by('?')[0]
        except IndexError:
            return None;

        return link

    def enabled(self):
        return self.get_query_set().filter(enabled=True)
