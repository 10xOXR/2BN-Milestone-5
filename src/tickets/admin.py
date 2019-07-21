from django.contrib import admin
from .models import Ticket, Comment, Upvote, TicketStatus, TicketType

admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(Upvote)
admin.site.register(TicketStatus)
admin.site.register(TicketType)
