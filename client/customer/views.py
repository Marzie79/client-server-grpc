from django.http import HttpResponse

from app_service_grpc_client.client import (get_price as price, get_seller as
                                            seller, get_stuff as stuff,
                                            get_same_stuff as same_stuff)


def get_price(request) -> HttpResponse:
    response = price(account_id="5")
    return HttpResponse(response)


def get_seller(request) -> HttpResponse:
    response = seller(account_id="5")
    return HttpResponse(response)


def get_same_stuff(request) -> HttpResponse:
    response = same_stuff(service_id=5)
    return HttpResponse(response)


def get_stuff(request) -> HttpResponse:
    response = stuff(service_id=5)
    return HttpResponse(response)