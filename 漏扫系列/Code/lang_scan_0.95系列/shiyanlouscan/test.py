
import sys
import urlparse
from script import bak_check
from lib.core import webcms,PortScan
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    ww = PortScan.PortScan()
    ww.work()

    

