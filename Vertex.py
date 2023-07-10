class Vertex:

    def __init__(self, name : str):
        self.__content : str = name
        self.__degree : int = 0

    def getContent(self) -> str:
        return self.__content

    def getDegree(self) -> int:
        return self.__degree

    def setDegree(self, degree: int) -> None:
        self.__degree = degree