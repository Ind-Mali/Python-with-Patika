{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lütfen pozitif bir değer giriniz: -2\n",
      "please enter non-negative number\n",
      "Please enter number:5\n",
      "5 sayısının faktoriyeli 120'dir\n"
     ]
    }
   ],
   "source": [
    "fak = 1\n",
    "x = int(input(\"Lütfen pozitif bir değer giriniz: \"))\n",
    "while x < 0 :\n",
    "    print(\"please enter non-negative number\")\n",
    "    x = int(input(\"Please enter number:\"))\n",
    "for i in range(1,x+1):\n",
    "    fak = i*fak\n",
    "print(\"{} sayısının faktoriyeli {}'dir\".format(x,fak))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "9\n",
      "27\n",
      "81\n"
     ]
    }
   ],
   "source": [
    "sonuc = 1\n",
    "for i in range(4):\n",
    "    sonuc*=3\n",
    "    print"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Listeler değiştirilebilir (mutable) fakat string'ler immutable değerlerdir yani değiştirilemezler. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [1,2,3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "l.append(200)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 200]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 200, 100, 123, 1234]"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.extend([100,123,1234])\n",
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [1,2,3,4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "l.insert(0,222)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[222, 1, 2, 3, 4]"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "l.insert(3,44)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[222, 1, 2, 44, 3, 4]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[222, 1, 2, 3, 4]"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.remove(44)\n",
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "try:\n",
    "    l.remove(40)\n",
    "except ValueError:\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[222, 1, 2, 3, 4]"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l = [1,2,3,4,4,4,44,222,222]\n",
    "l.count(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 4, 4, 44, 222, 222]"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "l2 = l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5, 2, 3, 4, 4, 4, 44, 222, 222]"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l[0] = 5\n",
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5, 2, 3, 4, 4, 4, 44, 222, 222]"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 20\n",
    "b = a\n",
    "a = a+5\n",
    "l = [20,30,40]\n",
    "l2 = l\n",
    "l[0] = l[0]+5\n",
    "b\n",
    "l2[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 20\n",
    "b = a\n",
    "a = a+5\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5, 5)"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = 5\n",
    "y = 7\n",
    "temp = x\n",
    "y = temp\n",
    "(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'l' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-18612d0b778f>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0ml\u001b[0m \u001b[1;32min\u001b[0m \u001b[1;36m44\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'l' is not defined"
     ]
    }
   ],
   "source": [
    "l in 44"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [1,2,3,33,44,55,[100,102,1,44]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "argument of type 'int' is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-18612d0b778f>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0ml\u001b[0m \u001b[1;32min\u001b[0m \u001b[1;36m44\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: argument of type 'int' is not iterable"
     ]
    }
   ],
   "source": [
    "l in 44"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "argument of type 'int' is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-18612d0b778f>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0ml\u001b[0m \u001b[1;32min\u001b[0m \u001b[1;36m44\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: argument of type 'int' is not iterable"
     ]
    }
   ],
   "source": [
    "l in 44"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "44 in l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter number0\n",
      "Bu sayı listede yoktur yeniden deneyiniz!!!\n",
      "Please enter number0\n",
      "Bu sayı listede yoktur yeniden deneyiniz!!!\n",
      "Please enter number1\n",
      "Bu sayı listede mevcuttur.\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    n = int(input(\"Please enter number\"))\n",
    "    if n in l:\n",
    "        print(\"Bu sayı listede mevcuttur.\")\n",
    "        break\n",
    "    else:\n",
    "        print(\"Bu sayı listede yoktur yeniden deneyiniz!!!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "dic = {\"isim\":[\"ahmet\",\"deniz\",\"mehmet\"],\n",
    "       \"puan\":[30,45,80],\n",
    "       \"spor\":[\"yüzme\",\"tenis\",\"futbol\"],\n",
    "       \"cinsiyet\":[\"Erkek\",\"Kadın\",\"Erkek\"]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>isim</th>\n",
       "      <th>puan</th>\n",
       "      <th>spor</th>\n",
       "      <th>cinsiyet</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ahmet</td>\n",
       "      <td>30</td>\n",
       "      <td>yüzme</td>\n",
       "      <td>Erkek</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>deniz</td>\n",
       "      <td>45</td>\n",
       "      <td>tenis</td>\n",
       "      <td>Kadın</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>mehmet</td>\n",
       "      <td>80</td>\n",
       "      <td>futbol</td>\n",
       "      <td>Erkek</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     isim  puan    spor cinsiyet\n",
       "0   ahmet    30   yüzme    Erkek\n",
       "1   deniz    45   tenis    Kadın\n",
       "2  mehmet    80  futbol    Erkek"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(dic)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='spor', ylabel='puan'>"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.plot(kind='scatter', x ='spor',y = 'puan', color = 'green')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ogrenciler = {\"deniz\":{\"not\":75}}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "UK\n",
      "TR\n",
      "USA\n",
      "DE\n",
      "GR\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "s = set()\n",
    "for i in range(n):\n",
    "    s.add(input())\n",
    "print (len(s))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "k = {1,2,3,4,1}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4}"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "set"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(k)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# SET\n",
    "\n",
    "Set içindeki sadece uniqe değerleri döndürür."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 6}"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "k.add(6)\n",
    "k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4}"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "k.remove(6)\n",
    "k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4}"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4}"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "k.discard(10)\n",
    "k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 10}"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "k.add(10)\n",
    "k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4}"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "k.discard(10)\n",
    "k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "s1 = set([1,2,4,3,5,7])\n",
    "s2 = set([1,2,4,6])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{3, 5, 7}"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1.difference(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{6}"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2.difference(s1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Symmetric"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{3, 5, 6, 7}"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1.symmetric_difference(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{3, 5, 6, 7}"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2.symmetric_difference(s1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# intersection ( keşisim)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 4}"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s1.intersection(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 4}"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s2.intersection(s1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# -------------------"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# non_scalar_for "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "notlar = [20,30,40,22]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "30\n",
      "40\n",
      "22\n"
     ]
    }
   ],
   "source": [
    "for e in notlar:\n",
    "    print(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "28.0\n"
     ]
    }
   ],
   "source": [
    "t = 0\n",
    "\n",
    "for e in notlar:\n",
    "    t +=e\n",
    "ortlama = t/len(notlar)\n",
    "print(ortlama)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[20, 30, 40, 22]"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "notlar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "28.0\n"
     ]
    }
   ],
   "source": [
    "k = 0\n",
    "\n",
    "for i in range(len(notlar)):\n",
    "    k += notlar[i]\n",
    "ort = k/len(notlar)\n",
    "print(ort)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "girilen_notlar = [11,21,31,41]\n",
    "\n",
    "for i in range(len(girilen_notlar)):\n",
    "    girilen_notlar[i]+=5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[16, 26, 36, 46]"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "girilen_notlar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[21, 26, 41, 51]\n"
     ]
    }
   ],
   "source": [
    "for i in range(len(girilen_notlar)):\n",
    "    \n",
    "    if i == 1:\n",
    "        continue\n",
    "    girilen_notlar[i] +=5\n",
    "print(girilen_notlar)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Kontrol edilecek olan sayıyı giriniz:23\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "11\n",
      "44\n",
      "23\n",
      "Sayınız liste içinde bulunuyor.\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"Kontrol edilecek olan sayıyı giriniz:\"))\n",
    "\n",
    "l = [2,3,4,5,11,44,23,45,100,23]\n",
    "for i in l:\n",
    "    print(i)\n",
    "    if x == i:\n",
    "        print(\"Sayınız liste içinde bulunuyor.\")\n",
    "        break\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "d = {\"studen_1\":[55,95],\"student_2\":[45,55],\"student_3\":[98,78]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "studen_1\n",
      "student_2\n",
      "student_3\n"
     ]
    }
   ],
   "source": [
    "for k in d:\n",
    "    print(k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[55, 95]\n",
      "[45, 55]\n",
      "[98, 78]\n"
     ]
    }
   ],
   "source": [
    "for i in d:\n",
    "    v = d[i]\n",
    "    print(v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[55, 95]\n",
      "[45, 55]\n",
      "[98, 78]\n"
     ]
    }
   ],
   "source": [
    "for i in d.values():\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "m = {\"student_1\":90, \"student_2\":80,\"student_3\":55}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "student_1\n"
     ]
    }
   ],
   "source": [
    "for k in m:\n",
    "    value = m[k]\n",
    "    if value > 85:\n",
    "        print(k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "key değeri: student_1 valuse değeri: 90\n",
      "key değeri: student_2 valuse değeri: 80\n",
      "key değeri: student_3 valuse değeri: 55\n"
     ]
    }
   ],
   "source": [
    "for k,v in m.items():\n",
    "    print(\"key değeri:\",k , \"valuse değeri:\",v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "for i in range(2,5,3):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# split and join methodları"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "s = \"merhaba naılsın\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['merhaba', 'naılsın']"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.split(\" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "merhabalar sizin isminiz nedir\n",
      "merhabalar-sizin-isminiz-nedir\n"
     ]
    }
   ],
   "source": [
    "def split_and_join(line):\n",
    "    x = line.split(\" \")\n",
    "    x = \"-\".join(x)\n",
    "    return x\n",
    "    \n",
    "if __name__ == '__main__':\n",
    "    line = input()\n",
    "    result = split_and_join(line)\n",
    "    print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['ad1.soyad1@mail.com', 'ad2.soyad2@gmail.com', 'ad3.soyad3@gmail.com']\n"
     ]
    }
   ],
   "source": [
    "mailler = {\"kisi1\":\"ad1.soyad1@mail.com\",\"kisi2\":\"ad2.soyad2@gmail.com\", \"kisi3\":\"ad3.soyad3@gmail.com\"}\n",
    "\n",
    "l = []\n",
    "\n",
    "for v in mailler.values():\n",
    "    l.append(v)\n",
    "    \",\".join(l)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# ----------------------"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# list comprehensions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]\n"
     ]
    }
   ],
   "source": [
    "squares = []\n",
    "\n",
    "for i in range(1,11):\n",
    "    squares.append(i*i)\n",
    "print(squares)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# list comprehension ile yapılmış hali"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "squares = [i*i for i in range(1,11)]\n",
    "squares"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [],
   "source": [
    "def cube(x):\n",
    "    return x*x*x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cubes = [cube(x) for x in range(1,11)]\n",
    "cubes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 9, 25, 49, 81]\n"
     ]
    }
   ],
   "source": [
    "odd_squares = []\n",
    "\n",
    "for i in squares:\n",
    "    if i % 2 ==1:\n",
    "        odd_squares.append(i)\n",
    "print(odd_squares)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# list comprehension ile yapılışı"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 9, 25, 49, 81]"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "odd_squares = [i for i in squares if i % 2 ==1]\n",
    "odd_squares"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# fonksiyon yaratıp onun üzerinden comprehension çalıştırmak"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [],
   "source": [
    "def iss_odd(x):\n",
    "    if x % 2 == 0:\n",
    "        return True\n",
    "    else:\n",
    "        return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4, 16, 36, 64, 100]"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "odd_squares = [i for i in squares if iss_odd(i)]\n",
    "odd_squares"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_even(y):\n",
    "    if y % 2 ==1:\n",
    "        return True\n",
    "    else:\n",
    "        return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 9, 25, 49, 81]"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "even_squares = [i for i in squares if is_even(i)]\n",
    "even_squares"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[25, 36, 62, 28, 38, 64, 30, 40, 67, 1, 27, 56, 1, 25, 55, 2, 21, 51]"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "m=[[[ 25, 36, 62],[ 28, 38, 64],[ 30, 40, 67]],[[ 1, 27, 56],[ 1, 25, 55],[ 2, 21, 51]]]\n",
    "\n",
    "new_m = [k for l in m for e in l for k in e]\n",
    "new_m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 8, 15, 16]\n"
     ]
    }
   ],
   "source": [
    "*x,y,z = (4,8,15,16,23,42)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [(1,2),(10,20)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "10\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "for a, b ,in l:\n",
    "    print(a)\n",
    "    print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2)\n",
      "(10, 20)\n"
     ]
    }
   ],
   "source": [
    "for i in l:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "adlar = [\"Tyler\",\"Blake\",\"Cory\",\"Cameron\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 indexindeki eleman: Tyler\n",
      "2 indexindeki eleman: Blake\n",
      "3 indexindeki eleman: Cory\n",
      "4 indexindeki eleman: Cameron\n"
     ]
    }
   ],
   "source": [
    "for i, e in enumerate(adlar, start = 1):\n",
    "    print(i, \"indexindeki eleman:\",e)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# ----------------------------------------------------"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# zip() komutu"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "ogrenciler = [\"ogrenci_1\",\"ogrenci_2\",\"ogrenci_3\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "notlar = [100,80,76]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ogrenci_1 100\n",
      "ogrenci_2 80\n",
      "ogrenci_3 76\n"
     ]
    }
   ],
   "source": [
    "for i in range(len(ogrenciler)):    # normal for döngüsü ile yaptığımızda bu şekil kodlama yapıyoruz.\n",
    "    s = ogrenciler[i]\n",
    "    n = notlar[i]\n",
    "    print(s,n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ogrenci_1 100\n",
      "ogrenci_2 80\n",
      "ogrenci_3 76\n"
     ]
    }
   ],
   "source": [
    "for s, n in zip(ogrenciler, notlar):   # zip ile iki ayrı listeyi birbrileri ile birleştiriyoruz.\n",
    "    print(s,n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('ogrenci_1', 100)\n",
      "('ogrenci_2', 80)\n",
      "('ogrenci_3', 76)\n"
     ]
    }
   ],
   "source": [
    "for e in zip(ogrenciler,notlar):\n",
    "    print(e)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Örnek"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "kaç adet satış yaptınız:2\n",
      "1.satıştan elde edilen para:25\n",
      "2.satıştan elde edilen para:25\n",
      "1.Satışın maliyeti:20\n",
      "2.Satışın maliyeti:20\n",
      " 1. satıştan yapılan toplam kar :5 \n",
      " 2. satıştan yapılan toplam kar :5 \n"
     ]
    }
   ],
   "source": [
    "satis = []\n",
    "maliyet = []\n",
    "karlar = []\n",
    "d ={}  \n",
    "n = int(input(\"kaç adet satış yaptınız:\"))\n",
    "\n",
    "for i in range(n):\n",
    "    k = int(input(\"{}.satıştan elde edilen para:\".format(i+1)))\n",
    "    satis.append(k)\n",
    "\n",
    "for e in range(n):\n",
    "    s = int(input(\"{}.Satışın maliyeti:\".format(e+1)))\n",
    "    maliyet.append(s)\n",
    "\n",
    "for m in range(len(maliyet)):\n",
    "    l = satis[m]\n",
    "    c = maliyet[m]\n",
    "    kar = l-c\n",
    "    karlar.append(kar)\n",
    "    print(\" {}. satıştan yapılan toplam kar :{} \".format(m+1 , kar))\n",
    "\n",
    "for i in range(n):\n",
    "    a = satis[i]\n",
    "    b = maliyet[i]\n",
    "    d[a]=b\n",
    "         "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{25: 20}"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " # zip ile yapılışı"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "kaç adet satış yaptınız:3\n",
      "1.satıştan elde edilen para:25\n",
      "2.satıştan elde edilen para:25\n",
      "3.satıştan elde edilen para:25\n",
      "1.Satışın maliyeti:20\n",
      "2.Satışın maliyeti:20\n",
      "3.Satışın maliyeti:20\n",
      " 2. satıştan yapılan toplam kar :5 \n",
      " 2. satıştan yapılan toplam kar :5 \n",
      " 2. satıştan yapılan toplam kar :5 \n"
     ]
    }
   ],
   "source": [
    "satis = []\n",
    "maliyet = []\n",
    "\n",
    "n = int(input(\"kaç adet satış yaptınız:\"))\n",
    "\n",
    "for i in range(n):\n",
    "    k = int(input(\"{}.satıştan elde edilen para:\".format(i+1)))\n",
    "    satis.append(k)\n",
    "\n",
    "for e in range(n):\n",
    "    s = int(input(\"{}.Satışın maliyeti:\".format(e+1)))\n",
    "    maliyet.append(s)\n",
    "\n",
    "for l, c in zip(satis, maliyet):   # zip yapınca format içindeki yeri ardaşık döndüremiyorum.\n",
    "    kar = l-c\n",
    "    print(\" {}. satıştan yapılan toplam kar :{} \".format(n-1 , kar))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[25, 25, 25]"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "satis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[20, 20, 20]"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "maliyet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "kar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# zip ile dictionary yaratmak"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "keys = [\"isim\",\"soyad\",\"Ülke\",\"iş\"]\n",
    "values = [\"Denis\",\"Walker\",\"Turkey\",\"Data Scientist\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "d ={}\n",
    "for i in range(len(keys)):\n",
    "    k = keys[i]\n",
    "    v = values[i]\n",
    "    d[k]=v\n",
    "               "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'isim': 'Denis', 'soyad': 'Walker', 'Ülke': 'Turkey', 'iş': 'Data Scientist'}"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'isim': 'Denis', 'soyad': 'Walker', 'Ülke': 'Turkey', 'iş': 'Data Scientist'}"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d = {}\n",
    "for k, v in zip(keys,values):\n",
    "    d[k]=v\n",
    "d"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# -----------------Foknsiyonlar-----------------------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "def square(x):\n",
    "    return x*x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "square(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "19"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "square(4)+3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "# fonksiyonda verilen değer çift ise direkt karesini al ama tek bir değer ise karesini al ve 10 ekle, \n",
    "def f(x):\n",
    "    res = x*x\n",
    "    \n",
    "    if x % 2 == 0:\n",
    "        return res\n",
    "    else:\n",
    "        return res+10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "35"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def listele(x):     \n",
    "\n",
    "    \"\"\"fonksiyonun içine verdiğimiz değerin karesini alıyor for döngüsüne giriyor \n",
    "    ve 20 ekliyor boş listeye ekliyor listeyi döndürüyor.\n",
    "    \"\"\"     \n",
    "    l = []\n",
    "    res = x*x\n",
    "    for _ in range(10):\n",
    "        res +=20\n",
    "        l.append(res)\n",
    "    return l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "?listele"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[120, 140, 160, 180, 200, 220, 240, 260, 280, 300]"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "listele(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "def f(x):\n",
    "    res = 5\n",
    "    res*=res\n",
    "    if x % 2 == 0:\n",
    "        print(\"Sonuc: \",res)\n",
    "        return res\n",
    "    else:\n",
    "        print(\"Sonuc: \",res )\n",
    "        return res+10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sonuc:  25\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sonuc:  25\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "35"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "123"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "for i in range(n):\n",
    "    i+=1\n",
    "    print(i, end=\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "def power(x,y):\n",
    "    return x**y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "power(2,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "power(2,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "def f(x):\n",
    "    return 2*x,10*x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(20, 100)"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(10)   # sonucunda tuple döndürür."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "a, b = f(5)  # a ve b değerlerini fonksiyondan gelecek olan 2 değeri atıyoruz."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "def f(x,y):\n",
    "    w = x+2\n",
    "    b = y+3\n",
    "    return w, b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(16, 20)"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(14,17)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# ---------------------------------------------------"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# predefined parameters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "def f(x,y=True):\n",
    "    if x % 2 == 0:\n",
    "        y=False\n",
    "        return y\n",
    "    return y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(7,True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# ------------------------------------------------------------\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [\"elma\",\"portakal\",\"armu\"]\n",
    "m = l\n",
    "def f(y):\n",
    "    y[0]=\"limon\"\n",
    "    return y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['limon', 'portakal', 'armu']"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['limon', 'portakal', 'armu']\n"
     ]
    }
   ],
   "source": [
    "print (m)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# ------------------------------------------------- First Class Function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [],
   "source": [
    "def kare(x):\n",
    "    return x**2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = kare"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Leap Year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2100\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "def is_leap(year):\n",
    "    leap = False\n",
    "    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)\n",
    "\n",
    "year = int(input())\n",
    "print(is_leap(year))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [],
   "source": [
    "def kare(x):\n",
    "    return x*x\n",
    "def dikdörtgen(a,b):\n",
    "    return a*b\n",
    "def alanlar_toplamı(kare,dikdörtgen):\n",
    "    toplam_alan = kare(2)+dikdörtgen(4,7)\n",
    "    return toplam_alan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'int' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-110-38c898e43957>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0malanlar_toplamı\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-107-03ebd9effff8>\u001b[0m in \u001b[0;36malanlar_toplamı\u001b[1;34m(kare, dikdörtgen)\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0malanlar_toplamı\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkare\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mdikdörtgen\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m     \u001b[0mtoplam_alan\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mkare\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0mdikdörtgen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m7\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      7\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mtoplam_alan\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'int' object is not callable"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [],
   "source": [
    "num1 = 10000000000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "num2 = 10_000_000_000      # sayıları alt tire _ ile ayırırsak bilgisayar bunu okurken normal okur."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num2-num1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [],
   "source": [
    "num3 = 0.12_11_12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.121112"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "num3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# --------------- F-Strings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"x'in değeri 4\""
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = 2\n",
    "\n",
    "f\"x'in değeri {x+2}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "isim:bora\n"
     ]
    }
   ],
   "source": [
    "isim = input(\"isim:\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'verilen isim bora'"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f\"verilen isim {isim}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'verilen isim Bora'"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f\"verilen isim {isim.capitalize()}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
