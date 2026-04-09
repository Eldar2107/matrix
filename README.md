"# matrix"  
📊 NumPy Matrix Operations Project
🇦🇿 Azərbaycan dilində

Bu layihə Python və NumPy istifadə edərək matris əməliyyatlarını göstərir. Jupyter Notebook üzərində hazırlanmışdır.

📌 Xüsusiyyətlər
Matrislərin yaradılması
Matrislərin toplanması
Matrislərin vurulması (dot product)
Determinantın hesablanması
Matrisin tərsinin tapılması (şərt ilə)
🧮 İstifadə olunan kitabxana
numpy
🚀 Kodun izahı
1. Matrislərin yaradılması
import numpy as np

A = np.array([[2, 4], [5, 8]])
B = np.array([[1, 3], [5, 10]])
2. Matrislərin toplanması
print("toplama:\n", A + B)
3. Matrislərin vurulması
print("vurma:\n", np.dot(A, B))
4. Determinantın hesablanması
print("A-nin determinanti:", np.linalg.det(A))
5. Matrisin tərsi
det = np.linalg.det(A)

if det == 0:
    print("Bu matrisin tersi yoxdur")
else:
    print("A matrisinin tersi:", np.linalg.inv(A))
⚠️ Qeydlər
Matrisin tərsi yalnız determinant ≠ 0 olduqda mövcuddur.
Hesablamalarda kiçik yuvarlaqlaşma fərqləri ola bilər.
🛠 Tələblər
pip install numpy
▶️ İşə salmaq
Jupyter Notebook açın
.ipynb faylını açın
Hüceyrələri ardıcıl çalışdırın
🇬🇧 English Version

This project demonstrates basic matrix operations using Python and NumPy in a Jupyter Notebook.

📌 Features
Matrix creation
Matrix addition
Matrix multiplication (dot product)
Determinant calculation
Matrix inverse calculation with condition checking
🧮 Library Used
numpy
🚀 Code Overview
1. Matrix Creation
import numpy as np

A = np.array([[2, 4], [5, 8]])
B = np.array([[1, 3], [5, 10]])
2. Matrix Addition
print("toplama:\n", A + B)
3. Matrix Multiplication
print("vurma:\n", np.dot(A, B))
4. Determinant Calculation
print("A-nin determinanti:", np.linalg.det(A))
5. Matrix Inverse
det = np.linalg.det(A)

if det == 0:
    print("This matrix does not have an inverse")
else:
    print("Inverse of matrix A:", np.linalg.inv(A))
⚠️ Notes
A matrix must have a non-zero determinant to have an inverse.
Minor floating-point precision differences may occur.
🛠 Requirements
pip install numpy
▶️ How to Run
Open Jupyter Notebook
Open the .ipynb file
Run cells step by step
