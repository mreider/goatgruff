from jsonrpc import jsonrpc_method

@jsonrpc_method('sayHello')
def whats_the_time(request, name='Lester'):
  return "Hello %s" % name

@jsonrpc_method('gimmeThat', authenticated=True)
def something_special(request, secret_data):
  return {'sauce': ['authenticated', 'sauce']}
