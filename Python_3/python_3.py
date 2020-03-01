class Array:
    arr = []
    __count = 0
    def __init__(self, arr = []):
        self.arr = arr
        Array.__count += 1
        print("Создан объект Множества")

    def __del__(self):
        Array.__count -= 1
        print("Уничтожен объект Множества")

    def __setattr__(self, key, value):
        if key == "arr":
            self.__dict__[key] = value
        else:
            raise AttributeError

    def getCount(self):
        print(Array.__count)

    def addElem(self, a):
        self.arr.append(a)

    def delElem(self, a):
        try:
            self.arr.remove(a)
            print("Удалено первое вхождение элемента", a)
            self.output()
        except ValueError:
            print("Такого элемента нет")

    def crossing(self, arr):
        resultArr = []
        for i in range(len(self.arr)):
            if self.arr[i] in arr:
                resultArr.append(self.arr[i])
        print("Результат пересечения: \t")
        print(resultArr)

    def residual(self, arr):
        resultArr = []
        for i in range(len(self.arr)):
            is_contains = False
            for j in range(len(arr)):
                if self.arr[i] == arr[j]:
                    is_contains = True
            if is_contains == False:
                resultArr.append(self.arr[i])
        print("Результат разности: \t")
        print(resultArr)

    def output(self):
        print(self.arr)

    def arraysWithEvenElems(arr_of_arrs):
        print("-------------------------------------")
        for i in range(len(arr_of_arrs)):
            is_even = True
            for j in range(len(arr_of_arrs[i].arr)):
                if arr_of_arrs[i].arr[j] % 2 == 1:
                    is_even = False
            if is_even == True:
                print(arr_of_arrs[i].arr)
        print("------------------------------------")

    def arraysWithNegativeElems(arr_of_arrs):
        print("-------------------------------------")
        for i in range(len(arr_of_arrs)):
            for j in range(len(arr_of_arrs[i].arr)):
                if arr_of_arrs[i].arr[j] < 0:
                    print(arr_of_arrs[i].arr)
                    break
        print("------------------------------------")

arr1 = Array()
arr2 = Array([10, 20, 30, 40, 50, 60, 70, 60])
arr3 = Array()
arr4 = Array([13, 15, 17, 19, -21, 1])
arr5 = Array([10, 11, 12, -13, -14, 15, 20])
arr1.addElem(10)
arr1.addElem(20)
arr1.addElem(30)
arr3.arr = [30, 50, 10, 70]
arr_of_arrs = [arr1, arr2, arr3, arr4, arr5]

arr1.output()
arr3.getCount()
arr2.delElem(60)
arr2.delElem(100)
arr2.crossing(arr1.arr)
arr2.residual(arr1.arr)
Array.arraysWithNegativeElems(arr_of_arrs)
Array.arraysWithEvenElems(arr_of_arrs)

del arr1
del arr2
del arr3
del arr4
del arr5