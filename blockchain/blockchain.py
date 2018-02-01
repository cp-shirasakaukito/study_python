import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        # すべてのブロックをchainに保持する
        self.chain = []
        # current_transactionsでブロック化されていないトランザクションを保持する
        self.current_transactions = []

        # ジェネシスブロックを作る
        self.new_block(previous_hash="1", proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        新しいブロックを作ってチェーンに追加する。
        :type proof: int the proof given by the proof of work algorithm
        :type previous_hash: str Hash of previous block
        :rtype: dict New Block
        """

        # トランザクションをブロック化する
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # トランザクションがブロック化されたためリセットする
        self.current_transactions = []

        # チェ-ンにブロックを渡す
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        新しいトランザクションを作ってcurrent_transactionsに追加する。
        :type sender: basestring Address of the Sender
        :type recipient: basestring Address of the Recipient
        :type amount: int amount
        :rtype: int The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass

# TODO 何をトリガーにブロックが追加されるのだろう
# TODO デコレータの概念を今度理解する。 https://qiita.com/_rdtr/items/d3bc1a8d4b7eb375c368