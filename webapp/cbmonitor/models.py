from django.db import models


class Cluster(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, primary_key=True, blank=False)

    def __str__(self):
        return self.name


class Server(models.Model):

    id = models.AutoField(primary_key=True)
    class Meta:
        unique_together = ["address", "cluster"]

    cluster = models.ForeignKey("Cluster", on_delete=models.PROTECT)
    address = models.CharField(max_length=80, blank=False)

    def __str__(self):
        return self.address


class Bucket(models.Model):

    class Meta:
        unique_together = ["name", "cluster"]

    name = models.CharField(max_length=32, default="default")
    cluster = models.ForeignKey("Cluster", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Index(models.Model):

    id = models.AutoField(primary_key=True)
    class Meta:
        unique_together = ["name", "cluster"]

    name = models.CharField(max_length=32, default="idx")
    cluster = models.ForeignKey("Cluster", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Observable(models.Model):

    id = models.AutoField(primary_key=True)
    class Meta:
        unique_together = ["name", "cluster", "server", "bucket", "index"]

    name = models.CharField(max_length=128)
    cluster = models.ForeignKey("Cluster", on_delete=models.PROTECT)
    server = models.ForeignKey("Server", on_delete=models.PROTECT, null=True, blank=True)
    bucket = models.ForeignKey("Bucket", null=True, blank=True, on_delete=models.PROTECT)
    index = models.ForeignKey("Index", null=True, blank=True, on_delete=models.PROTECT)
    collector = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Snapshot(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, primary_key=True, blank=False)
    ts_from = models.DateTimeField(blank=True, null=True)
    ts_to = models.DateTimeField(blank=True, null=True)
    cluster = models.ForeignKey("Cluster", on_delete=models.PROTECT)

    def __str__(self):
        return self.name
