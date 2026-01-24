class Node:
    def __init__(self, data):
        """
        Нэг зангилаа (node) үүсгэнэ.
        data  -> хадгалах өгөгдөл
        next  -> дараагийн node руу заах холбоос
        """
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        """
        Холбоост жагсаалтыг үүсгэнэ.
        head -> жагсаалтын эхний node
        """
        self.head = None

    def is_empty(self):
        """
        Жагсаалт хоосон эсэхийг шалгана.
        Хэрэв head == None бол хоосон гэж үзнэ.
        """
        pass

    def append(self, data):
        """
        Жагсаалтын ТӨГСГӨЛД шинэ node нэмнэ.
        - Хэрэв жагсаалт хоосон бол head болгоно
        - Үгүй бол хамгийн сүүлийн node-г олж холбоно
        """
        pass

    def prepend(self, data):
        """
        Жагсаалтын ЭХЭНД шинэ node нэмнэ.
        - Шинэ node-ийн next-г одоогийн head болгоно
        - head-г шинэ node руу заалгана
        """
        pass

    def insert_after(self, prev_data, data):
        """
        Тодорхой өгөгдөлтэй node-ийн ДАРАА шинэ node оруулна.
        - prev_data-г агуулсан node-г олно
        - Олдвол дараа нь шинэ node холбоно
        """
        pass

    def delete(self, data):
        """
        Өгөгдөл нь data-тай тэнцүү node-г устгана.
        - Хэрэв head устгах бол head-г шинэчилнэ
        - Дунд эсвэл төгсгөлөөс устгах бол холбоосыг засна
        """
        pass

    def search(self, data):
        """
        Өгөгдөл нь data-тай тэнцүү node байгаа эсэхийг шалгана.
        - Байвал True
        - Байхгүй бол False буцаана
        """
        pass

    def length(self):
        """
        Жагсаалтын нийт node-ийн тоог олно.
        - Head-ээс эхлэн дараалан тоолно
        """
        pass

    def display(self):
        """
        Жагсаалтын бүх элементүүдийг дарааллаар нь хэвлэнэ.
        Жишээ: 10 -> 20 -> 30 -> None
        """
        pass
