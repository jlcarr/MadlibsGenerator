"""
For BlankBlank:

To decode and retrieve bad actor based on IP run this in your shell

>>>  from django.contrib.sessions.models import Session
>>>  qs = Session.objects.all()
>>>  for q in qs:
>>>     session_data = q.get_decoded()
>>>     ip_address = session_data.get('ip_address')

"""
from __future__ import annotations

from typing import Callable

from django.http import HttpRequest
from django.http.response import HttpResponseBase


class IpMiddleware:
    def __init__(self, get_response: (Callable[[HttpRequest], HttpResponseBase])) -> None:
        self.get_response = get_response

    def __call__(
            self, request: HttpRequest
    ) -> HttpResponseBase:
        ip_address = request.META.get('REMOTE_ADDR')
        # Set the IP address in the session
        request.session['ip_address'] = ip_address
        return self.get_response(request)


