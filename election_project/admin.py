from django.contrib import admin
from election_project.models import *

admin.site.register(Candidate)
admin.site.register(Voter)
admin.site.register(MyVotes)
admin.site.register(Appeal)
admin.site.register(MyAppeal)
# Register your models here.
