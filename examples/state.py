from pyteal import *

def approval_program():

    globalStatus = Global.storage[Bytes("status")]
    globalExample = Seq([
        If(globalStatus.exists(),
            Assert(globalStatus == Int(0)),
            globalStatus.set(Int(1))
        ),
        globalStatus.delete(),
    ])

    senderStatus = Txn.senderStorage[Bytes("status")]
    localSenderExample = Seq([
        If(senderStatus.exists(),
            Assert(senderStatus == Int(0)),
            senderStatus.set(Int(10))
        ),
        senderStatus.delete()
    ])

    firstAccountStatus = Txn.accountStorage[0][Bytes("status")]
    localAccountExample = Seq([
        If(firstAccountStatus.exists(),
            Assert(firstAccountStatus == Int(0)),
            firstAccountStatus.set(Int(10))
        ),
        firstAccountStatus.delete()
    ])

    globalForeignStatus = Txn.foreignAppStorage[0][Bytes("status")]
    globalForeignExample = Assert(And(
        globalForeignStatus.exists(),
        globalForeignStatus == Int(0)
    ))

    senderForeignStatus = Txn.senderStorage.forApp(Int(1234))[Bytes("status")]
    localsenderForeignExample = Assert(And(
        senderForeignStatus.exists(),
        senderForeignStatus == Int(10)
    ))

    firstAccountForeignStatus = Txn.accountStorage[0].forApp(Int(1234))[Bytes("status")]
    localAccountForeignExample = Assert(And(
        firstAccountForeignStatus.exists(),
        firstAccountForeignStatus == Int(10)
    ))

    program = Seq([
        Pop(len(Gtxn.accounts(0)) == Int(1)),
        globalExample,
        localSenderExample,
        localAccountExample,
        globalForeignExample,
        localsenderForeignExample,
        localAccountForeignExample,
        Return(Int(1))
    ])

    return program

print(compileTeal(approval_program(), Mode.Application))
