{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ad968110-c1cf-42dc-ba4a-644092e8a574",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "toplama:\n",
      " [[ 3  7]\n",
      " [10 18]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "A=np.array([[2, 4], [5, 8]]) \n",
    "B=np.array([[1, 3], [5,10]]) \n",
    "print (\"toplama:\\n\", A+B)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "bfcb48db-0b66-44e0-8c37-a29bef95aef8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "vurma:\n",
      " [[22 46]\n",
      " [45 95]]\n"
     ]
    }
   ],
   "source": [
    "print(\"vurma:\\n\", np.dot(A,B))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a0056e91-1b47-4e27-b8db-ff232405efa4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A-nin determinanti: -3.999999999999999\n"
     ]
    }
   ],
   "source": [
    "\n",
    "print(\"A-nin determinanti:\" , np.linalg.det(A))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3bbeb04e-319f-4d86-956a-9c72b26b7925",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A matrisinin tersi: [[-2.    1.  ]\n",
      " [ 1.25 -0.5 ]]\n"
     ]
    }
   ],
   "source": [
    "det = np.linalg.det(A)\n",
    "if det==0:\n",
    "     print(\"bu matrisin tersi yoxdur:\")\n",
    "else:\n",
    "     print(\"A matrisinin tersi:\", np.linalg.inv(A))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7bd10e97-7f82-4be8-961b-631a10a276f5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
