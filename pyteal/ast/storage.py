from typing import Union
from abc import ABC, abstractmethod

from ..types import TealType
from .expr import Expr
from .leafexpr import LeafExpr
from .seq import Seq
from .bytes import Bytes
from .int import Int

class ExStorageKey(LeafExpr):

    @abstractmethod
    def _getValue(self) -> Expr:
        pass

    @abstractmethod
    def _getExists(self) -> Expr:
        pass

    def exists(self) -> Expr:
        return self._getExists()
    
    def __teal__(self):
        return self._getValue().__teal__()
    
    def __str__(self) -> str:
        return self._getValue().__str__()
    
    def type_of(self) -> TealType:
        return self._getValue().type_of()

class StorageKey(ExStorageKey):
    
    @abstractmethod
    def _setValue(self, value: Expr) -> Expr:
        pass
    
    @abstractmethod
    def _deleteValue(self) -> Expr:
        pass

    def set(self, value: Expr) -> Expr:
        return self._setValue(value)
    
    def delete(self) -> Expr:
        return self._deleteValue()

class LocalExStorageKey(ExStorageKey):

    def __init__(self, account: Expr, appId: Expr, key: Expr) -> None:
        self.account = account
        self.appId = appId
        self.key = key

    def _getValue(self) -> Expr:
        from .app import App
        getEx = App.localGetEx(self.account, self.appId, self.key)
        return Seq([
            getEx,
            getEx.value()
        ])
    
    def _getExists(self) -> Expr:
        from .app import App
        getEx = App.localGetEx(self.account, self.appId, self.key)
        return Seq([
            getEx,
            getEx.hasValue()
        ])

class LocalStorageKey(StorageKey):

    def __init__(self, account: Expr, key: Expr) -> None:
        self.account = account
        self.key = key

    def _getValue(self) -> Expr:
        from .app import App
        return App.localGet(self.account, self.key)
    
    def _setValue(self, value: Expr) -> Expr:
        from .app import App
        return App.localPut(self.account, self.key, value)
    
    def _deleteValue(self) -> Expr:
        from .app import App
        return App.localDel(self.account, self.key)
    
    def _getExists(self) -> Expr:
        from .app import App
        getEx = App.localGetEx(self.account, App.id(), self.key)
        return Seq([
            getEx,
            getEx.hasValue()
        ])

class GlobalExStorageKey(ExStorageKey):

    def __init__(self, app: Expr, key: Expr) -> None:
        self.app = app
        self.key = key
    
    def _getValue(self) -> Expr:
        from .app import App
        getEx = App.globalGetEx(self.app, self.key)
        return Seq([
            getEx,
            getEx.value()
        ])
    
    def _getExists(self) -> Expr:
        from .app import App
        getEx = App.globalGetEx(self.app, self.key)
        return Seq([
            getEx,
            getEx.hasValue()
        ])

class GlobalStorageKey(StorageKey):

    def __init__(self, key: Expr) -> None:
        self.key = key
    
    def _getValue(self) -> Expr:
        from .app import App
        return App.globalGet(self.key)
    
    def _setValue(self, value: Expr) -> Expr:
        from .app import App
        return App.globalPut(self.key, value)
    
    def _deleteValue(self) -> Expr:
        from .app import App
        return App.globalDel(self.key)
    
    def _getExists(self) -> Expr:
        from .app import App
        getEx = App.globalGetEx(Int(0), self.key)
        return Seq([
            getEx,
            getEx.hasValue()
        ])

class ExStorageAccessor(ABC):

    @abstractmethod
    def _access(self, key: Expr) -> ExStorageKey:
        pass

    def __getitem__(self, key: Union[str, Expr]) -> ExStorageKey:
        if type(key) == str:
            key = Bytes(key)
        return self._access(key)

class StorageAccessor(ExStorageAccessor):

    @abstractmethod
    def _access(self, key: Expr) -> StorageKey:
        pass

    def __getitem__(self, key: Union[str, Expr]) -> StorageKey:
        if type(key) == str:
            key = Bytes(key)
        return self._access(key)

class LocalExStorageAccessor(StorageAccessor):

    def __init__(self, account: Expr, appId: Expr) -> None:
        self.account = account
        self.appId = appId
    
    def _access(self, key: Expr) -> StorageKey:
        return LocalExStorageKey(self.account, self.appId, key)

class LocalStorageAccessor(StorageAccessor):

    def __init__(self, account: Expr) -> None:
        self.account = account
    
    def forApp(self, appId: Expr) -> LocalExStorageAccessor:
        return LocalExStorageAccessor(self.account, appId)
    
    def _access(self, key: Expr) -> StorageKey:
        return LocalStorageKey(self.account, key)

class GlobalStorageAccessor(StorageAccessor):

    def _access(self, key: Expr) -> StorageKey:
        return GlobalStorageKey(key)

class AccountsStorage:

    def length(self):
        from .txn import Txn
        return Txn.accounts.length()
    
    def __getitem__(self, index: Union[int, Expr]) -> LocalStorageAccessor:
        if type(index) == int:
            accessIndex = Int(index + 1)
        else:
            accessIndex = index + Int(1)
        return LocalStorageAccessor(accessIndex)

class GlobalExStorageAccessor(ExStorageAccessor):

    def __init__(self, app: Expr) -> None:
        self.app = app
    
    def _access(self, key: Expr) -> ExStorageKey:
        return GlobalExStorageKey(self.app, key)

class ForeignAppsStorage:
    
    def __getitem__(self, index: Union[int, Expr]) -> StorageAccessor:
        if type(index) == int:
            accessIndex = Int(index + 1)
        else:
            accessIndex = index + Int(1)
        return LocalStorageAccessor(accessIndex)
