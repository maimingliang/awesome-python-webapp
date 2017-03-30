#dp.py

#数据库引擎对象：

class _Engine(object):
	"""docstring for _Engine
"""
	def __init__(self, connect):
		self._connect = connect

	def connect():
		return self._connect

engine = None

class _DbCtx(threading.local):
	"""docstring for _DbCtx"""
	def __init__(self):
		super(_DbCtx, self).__init__()
		self.conection = None
		self.transactions = 0

	def init(self):
		self.conection = _LasyConnection()
		self.transactions = 0

	def cleanup(self):
				self.conection.cleanup()
				self.conection = None
	def cursor(self):
		return self.conection.cursor()


_db_ctx = _DbCtx()


			
