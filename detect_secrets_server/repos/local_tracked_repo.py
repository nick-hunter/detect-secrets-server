from __future__ import absolute_import

from .base_tracked_repo import BaseTrackedRepo
from detect_secrets_server.storage.file import FileStorageWithLocalGit


class LocalTrackedRepo(BaseTrackedRepo):

    STORAGE_CLASS = FileStorageWithLocalGit

    def cron(self):
        return "%s %s" % (super(LocalTrackedRepo, self).cron(), '--local')
