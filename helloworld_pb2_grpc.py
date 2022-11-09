# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import helloworld_pb2 as helloworld__pb2


class ChatServerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ChatStream = channel.unary_stream(
        '/grpc.ChatServer/ChatStream',
        request_serializer=helloworld__pb2.Empty.SerializeToString,
        response_deserializer=helloworld__pb2.Note.FromString,
        )
    self.SendNote = channel.unary_unary(
        '/grpc.ChatServer/SendNote',
        request_serializer=helloworld__pb2.Note.SerializeToString,
        response_deserializer=helloworld__pb2.Empty.FromString,
        )
    self.SendNotemulti = channel.unary_unary(
        '/grpc.ChatServer/SendNotemulti',
        request_serializer=helloworld__pb2.ChatUserMessage.SerializeToString,
        response_deserializer=helloworld__pb2.Empty.FromString,
        )
    self.register = channel.unary_unary(
        '/grpc.ChatServer/register',
        request_serializer=helloworld__pb2.registerdetails.SerializeToString,
        response_deserializer=helloworld__pb2.APIResponse.FromString,
        )
    self.login = channel.unary_unary(
        '/grpc.ChatServer/login',
        request_serializer=helloworld__pb2.LoginRequest.SerializeToString,
        response_deserializer=helloworld__pb2.APIResponse.FromString,
        )
    self.logout = channel.unary_unary(
        '/grpc.ChatServer/logout',
        request_serializer=helloworld__pb2.Empty.SerializeToString,
        response_deserializer=helloworld__pb2.APIResponse.FromString,
        )
    self.ChatUser = channel.unary_stream(
        '/grpc.ChatServer/ChatUser',
        request_serializer=helloworld__pb2.ChatUserMessage.SerializeToString,
        response_deserializer=helloworld__pb2.Note.FromString,
        )
    self.ChatStreamUser = channel.unary_stream(
        '/grpc.ChatServer/ChatStreamUser',
        request_serializer=helloworld__pb2.Empty.SerializeToString,
        response_deserializer=helloworld__pb2.ChatUserMessage.FromString,
        )
    self.RegisteredUsers = channel.unary_stream(
        '/grpc.ChatServer/RegisteredUsers',
        request_serializer=helloworld__pb2.Empty.SerializeToString,
        response_deserializer=helloworld__pb2.registerdetails.FromString,
        )


class ChatServerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ChatStream(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendNote(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendNotemulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def login(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def logout(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ChatUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ChatStreamUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegisteredUsers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChatServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ChatStream': grpc.unary_stream_rpc_method_handler(
          servicer.ChatStream,
          request_deserializer=helloworld__pb2.Empty.FromString,
          response_serializer=helloworld__pb2.Note.SerializeToString,
      ),
      'SendNote': grpc.unary_unary_rpc_method_handler(
          servicer.SendNote,
          request_deserializer=helloworld__pb2.Note.FromString,
          response_serializer=helloworld__pb2.Empty.SerializeToString,
      ),
      'SendNotemulti': grpc.unary_unary_rpc_method_handler(
          servicer.SendNotemulti,
          request_deserializer=helloworld__pb2.ChatUserMessage.FromString,
          response_serializer=helloworld__pb2.Empty.SerializeToString,
      ),
      'register': grpc.unary_unary_rpc_method_handler(
          servicer.register,
          request_deserializer=helloworld__pb2.registerdetails.FromString,
          response_serializer=helloworld__pb2.APIResponse.SerializeToString,
      ),
      'login': grpc.unary_unary_rpc_method_handler(
          servicer.login,
          request_deserializer=helloworld__pb2.LoginRequest.FromString,
          response_serializer=helloworld__pb2.APIResponse.SerializeToString,
      ),
      'logout': grpc.unary_unary_rpc_method_handler(
          servicer.logout,
          request_deserializer=helloworld__pb2.Empty.FromString,
          response_serializer=helloworld__pb2.APIResponse.SerializeToString,
      ),
      'ChatUser': grpc.unary_stream_rpc_method_handler(
          servicer.ChatUser,
          request_deserializer=helloworld__pb2.ChatUserMessage.FromString,
          response_serializer=helloworld__pb2.Note.SerializeToString,
      ),
      'ChatStreamUser': grpc.unary_stream_rpc_method_handler(
          servicer.ChatStreamUser,
          request_deserializer=helloworld__pb2.Empty.FromString,
          response_serializer=helloworld__pb2.ChatUserMessage.SerializeToString,
      ),
      'RegisteredUsers': grpc.unary_stream_rpc_method_handler(
          servicer.RegisteredUsers,
          request_deserializer=helloworld__pb2.Empty.FromString,
          response_serializer=helloworld__pb2.registerdetails.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.ChatServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
