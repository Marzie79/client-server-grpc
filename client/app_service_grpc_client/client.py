import logging

import grpc
from django.conf import settings

from protos import app_service_pb2_grpc, app_service_pb2

logger = logging.getLogger(__name__)



def get_seller(account_id: str,) -> app_service_pb2.SellerResponse:
    print("start seller client")
    try:
        with grpc.insecure_channel(
                f"{settings.GRPC_SERVERS['SSO_HOST']}:{settings.GRPC_SERVERS['SSO_PORT']}") as channel:
            stub = app_service_pb2_grpc.MainAppStub(channel)
            if service := stub.GetSevice(app_service_pb2.CustomerRequest(account_id=account_id)):
                return service
    except Exception as e:
        logger.exception(e)
        raise


def get_price(account_id: str,) -> app_service_pb2.PriceResponse:
    print("start price client")
    try:
        with grpc.insecure_channel(
                f"{settings.GRPC_SERVERS['SSO_HOST']}:{settings.GRPC_SERVERS['SSO_PORT']}") as channel:
            stub = app_service_pb2_grpc.MainAppStub(channel)
            for number in stub.GetPrice(app_service_pb2.CustomerRequest(account_id=account_id)):
                yield number
    except Exception as e:
        logger.exception(e)
        raise


def entry_request_iterator(service_id):
    for item in range(1, service_id):
        yield app_service_pb2.StuffRequest(service_id=item)


def get_same_stuff(service_id: int) -> app_service_pb2.StuffPriceResponse:
    print("start same stuff client")
    try:
        with grpc.insecure_channel(
                f"{settings.GRPC_SERVERS['SSO_HOST']}:{settings.GRPC_SERVERS['SSO_PORT']}") as channel:
            stub = app_service_pb2_grpc.MainAppStub(channel)
            return stub.GetSameStuff(entry_request_iterator(service_id))
    except Exception as e:
        logger.exception(e)
        raise


def get_stuff(service_id: int) -> app_service_pb2.StuffPriceResponse:
    print("start stuff client")
    try:
        with grpc.insecure_channel(
                f"{settings.GRPC_SERVERS['SSO_HOST']}:{settings.GRPC_SERVERS['SSO_PORT']}") as channel:
            stub = app_service_pb2_grpc.MainAppStub(channel)
            for number in stub.GetStuff(entry_request_iterator(service_id)):
                yield number
    except Exception as e:
        logger.exception(e)
        raise
