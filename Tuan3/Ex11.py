import numpy as np
A = np.array([2, 4, 1, 6, 7, 2, 3, 5, 9]).reshape(3, 3)
print("Is A matrix square or not?", A.shape[0] == A.shape[1])
print("Is A matrix symmetric or not?", np.allclose(A, A.T))
print("Is A matrix skew-symmetric or not?", np.allclose(A, -A.T))
# Find Upper triangular matrix of A. tam giac tren
print(np.tril(A))
# Find Lower triangular matrix of A.
print(np.triu(A))

'''
numpy.allclose() hàm được sử dụng để tìm xem hai mảng có bằng nhau về phần tử trong một dung sai hay không. Các giá trị dung sai là dương, thường là các số rất nhỏ. Chênh lệch tương đối (rtol * abs (arr2)) và chênh lệch tuyệt đối atol được cộng lại với nhau để so sánh với chênh lệch tuyệt đối giữa arr1 và arr2 . Nếu một trong hai mảng chứa một hoặc nhiều NaN, thì trả về Sai. Infs được coi là bằng nhau nếu chúng ở cùng một vị trí và cùng dấu trong cả hai mảng.

Nếu phương trình sau là True, thì allclose trả về True.
absolute(arr1 - arr2) <= (atol + rtol * absolute(arr2))
Vì, Phương trình trên không đối xứng trong arr1 và arr2, Vì vậy, allclose (arr1, arr2) có thể khác với allclose (arr2, arr1) trong một số trường hợp hiếm hoi.

Cú pháp: numpy.allclose (arr1, arr2, rtol, atol, equal_nan = False)

Các tham số:
arr1: [array_like] Nhập mảng đầu tiên.
arr2: [array_like] Nhập mảng thứ 2.
rtol: [float] Tham số dung sai tương đối.
atol: [float] Tham số dung sai tuyệt đối.
Bằng_nan: [bool] Liệu có thể so sánh NaN bằng nhau không. Nếu Đúng, NaN trong arr1 sẽ được coi là bằng NaN trong arr2 trong mảng đầu ra.

Return: [bool] Trả về True nếu hai mảng bằng nhau trong dung sai đã cho, nếu không thì trả về False.
'''
