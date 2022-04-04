from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(null=False, blank=False, max_length=500)
    creator = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Get url for user's detail view.
        Returns:
            str: URL for project detail.

        """
        return reverse("projects:detail", kwargs={"pk": self.pk})

    def __str__(self):
        """Get str ref for model title

        Returns:
            str: self.name.

        """
        return self.name
