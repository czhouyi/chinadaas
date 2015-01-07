from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from hbase import Hbase
from hbase.ttypes import *

class HbaseDao:
    client = None

    def __init__(self):
        transport = TSocket.TSocket('192.168.11.14', 9090)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        self.client = Hbase.Client(protocol)
        transport.open()

    def getTables(self):
        return self.client.getTableNames()

    def scan(self, tablename, count=10):
        scan = TScan() 
        idkey = self.client.scannerOpenWithScan(tablename, scan, None)
        return self.client.scannerGetList(idkey, count)

    def getRow(self, tablename, rowkey):
        return self.client.getRow(tablename, rowkey, None)

    def getColumnDescriptors(self, tablename):
        return self.client.getColumnDescriptors(tablename)

    def getTableRegions(self, tablename):
        return self.client.getTableRegions(tablename)

if __name__=='__main__':
    dao = HbaseDao()
    print dao.scan('zzjg_detail')
