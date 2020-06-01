

import hashlib, struct
from datetime import datetime
 
version = 0x20000000
previous_block = "000000000000000000013ac78094ea7584a6d87020d33d12ad10c87752cf188d"
markle_root = "93371570b3f7c9bed52a464c4af77b25d57313d91789cab4e5d36f874c3bbceb"
time_ = "2020/01/26 15:56:16"
bits = 387124344
nonce_corect = 3745729861
nonce = 0

bs = bits >> 24
bm = bits & 0xffffff
target = '%064x' % (bm << (8*(bs - 3)))


while nonce < 0x100000000:
    version_header=struct.pack("<L", version)
    previous_block_header = previous_block.decode("hex")[::-1]
    markle_root_header = markle_root.decode("hex")[::-1]
    unixtime_ = int(datetime.strptime(time_, "%Y/%m/%d %H:%M:%S").strftime('%s'))
    time_header = struct.pack("<L", unixtime_)
    bits_header = struct.pack("<L", bits)
    nonce_header = struct.pack("<L", nonce)
    header = version_header + previous_block_header + markle_root_header + time_header + bits_header + nonce_header
    hash = hashlib.sha256(hashlib.sha256(header).digest()).digest()
    print "nonce:"+str(nonce), "hash:"+str(hash[::-1].encode('hex'))
    if hash[::-1].encode('hex') < target:
        print 'success'
        break
    nonce += 1
