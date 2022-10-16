from protos import app_service_pb2_grpc, app_service_pb2

def grpc_seller_service(server):
    app_service_pb2_grpc.add_MainAppServicer_to_server(MainAppServicer(), server)


class MainAppServicer(app_service_pb2_grpc.MainAppServicer):
    def GetSevice(self, request, context):
        account_id = request.account_id
        print('We are in seller server side ', account_id)
        return app_service_pb2.SellerResponse(service_id=account_id,
                                                      message='hello',
                                                      service_list=['test', 'test_one'],
                                                      )

    def GetPrice(self, request, context):
        account_id = request.account_id
        print('We are in price server side ', account_id)
        count_list = 4
        for i in range(0, count_list):
            yield app_service_pb2.PriceResponse(service_id=account_id,
                                                      message='bye',
                                                      service_list=['test', 'test_two'],)


    def GetSameStuff(self, request_iterator, context):
        print('We are in same stuff server side')
        service_id = None
        for request in request_iterator:
            service_id = request.service_id
            print('We are in stuff server side ', service_id)
        if service_id:     
            return app_service_pb2.StuffPriceResponse(price=str(service_id))


    def GetStuff(self, request_iterator, context):
        print('We are in stuff server side')
        for request in request_iterator:
            service_id = request.service_id
            print('We are in stuff server side ', service_id)
            yield app_service_pb2.StuffPriceResponse(price=str(service_id))


    


    
    
# network.bind_host
# (Static, string) The network address(es) to which the node should bind in order to listen for incoming connections. Accepts a list of IP addresses, hostnames, and special values. Defaults to the address given by network.host. Use this setting only if binding to multiple addresses or using different addresses for publishing and binding.
# network.publish_host
# (Static, string) The network address that clients and other nodes can use to contact this node. Accepts an IP address, a hostname, or a special value. Defaults to the address given by network.host. Use this setting only if binding to multiple addresses or using different addresses for publishing and binding.

    