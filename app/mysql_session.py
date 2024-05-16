import mysql.connector
    
class MySQLSession(object):
  def __init__(self, account):
    self.account = account
    
  def __enter__(self):
    self.connect = mysql.connector.connect(
      db      = self.account["db"],
      host    = self.account["host"],
      user    = self.account["user"],
      passwd  = self.account["pass"],
      port    = self.account["port"],
      charset = "utf8")
    return self.connect
    
  def __exit__(self, exception_type, exception_value, traceback):
    self.connect.close()
