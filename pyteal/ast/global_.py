from enum import Enum

from ..types import TealType
from .expr import LeafExpr

class GlobalField(Enum):
     min_txn_fee = 0
     min_balance = 1
     max_txn_life = 2
     zero_address = 3
     group_size = 4

type_of_global_field = {
     GlobalField.min_txn_fee: TealType.uint64,
     GlobalField.min_balance: TealType.uint64,
     GlobalField.max_txn_life: TealType.uint64,
     GlobalField.zero_address: TealType.bytes,
     GlobalField.group_size: TealType.uint64
}

str_of_global_field = {
     GlobalField.min_txn_fee: "MinTxnFee",
     GlobalField.min_balance: "MinBalance",
     GlobalField.max_txn_life: "MaxTxnLife",
     GlobalField.zero_address: "ZeroAddress",
     GlobalField.group_size: "GroupSize"
}   

class Global(LeafExpr):

    # default constructor
    def __init__(self, field:GlobalField) -> None:
        self.field = field

    def __teal__(self):
        return [["global", str_of_global_field[self.field]]]
         
    def __str__(self):
        return "(Global {})".format(str_of_global_field[self.field])

    @classmethod
    def min_txn_fee(cls):
        return cls(GlobalField.min_txn_fee)

    @classmethod
    def min_balance(cls):
        return cls(GlobalField.min_balance)

    @classmethod
    def max_txn_life(cls):
        return cls(GlobalField.max_txn_life)

    @classmethod
    def zero_address(cls):
        return cls(GlobalField.zero_address)

    @classmethod
    def group_size(cls):
        return cls(GlobalField.group_size)

    def type_of(self):
        return type_of_global_field[self.field]
