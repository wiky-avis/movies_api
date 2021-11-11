from abc import ABC, abstractmethod


class Action(ABC):
    def __await__(self):
        return self.__call__()

    @abstractmethod
    async def __call__(self, *args, **kwargs):
        raise NotImplementedError
