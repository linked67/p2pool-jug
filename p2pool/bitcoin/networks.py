import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc
from operator import *


@defer.inlineCallbacks
def check_genesis_block(bitcoind, genesis_block_hash):
    try:
        yield bitcoind.rpc_getblock(genesis_block_hash)
    except jsonrpc.Error_for_code(-5):
        defer.returnValue(False)
    else:
        defer.returnValue(True)

nets = dict(

juggalocoin=math.Object(
        P2P_PREFIX='fec3b9de'.decode('hex'),
        P2P_PORT=39348,
        ADDRESS_VERSION=43,
        RPC_PORT=39347,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'JuggaloCoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),                           
        SUBSIDY_FUNC=lambda nBits, height: __import__('juggalocoin_subsidy').GetBlockBaseValue(nBits, height),
        BLOCKHASH_FUNC=lambda data: pack.IntType(256).unpack(__import__('xcoin_hash').getPoWHash(data)),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('xcoin_hash').getPoWHash(data)),
        BLOCK_PERIOD=60, # s
        SYMBOL='JUG',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'JuggaloCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/JuggaloCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.JuggaloCoin'), 'JuggaloCoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='',
        ADDRESS_EXPLORER_URL_PREFIX='',
        TX_EXPLORER_URL_PREFIX='',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**20 - 1), 
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
