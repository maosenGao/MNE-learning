from neo.Core.IO.Mixins import SerializableMixin
from abc import ABC, abstractmethod


class ClonableMixin(ABC):
    @abstractmethod
    def clone(self):
        pass


class CodeMixin:
    def __init__(self):
        self.scripts = []
        self.parameter_list = []
        self.return_type = None
        self.script_hash = None


class VerifiableMixin(ABC, SerializableMixin):

    def __init__(self):
        super(VerifiableMixin, self).__init__()
        self.scripts = []

    # <summary>
    # 反序列化未签名的数据
    # </summary>
    # <param name="reader">数据来源</param>
    @abstractmethod
    def DeserializeUnsigned(self, reader):
        pass

    # <summary>
    # 获得需要校验的脚本Hash值
    # </summary>
    # <returns>返回需要校验的脚本Hash值</returns>
    @abstractmethod
    def GetScriptHashesForVerifying(self):
        pass

    # <summary>
    # 序列化未签名的数据
    # </summary>
    # <param name="writer">存放序列化后的结果</param>
    @abstractmethod
    def SerializeUnsigned(self, writer):
        pass


class EquatableMixin:

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
