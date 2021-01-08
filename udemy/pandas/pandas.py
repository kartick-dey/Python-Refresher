{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "from numpy.random import randn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "np.random.seed(101)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'],['W', 'X', 'Y', 'Z'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
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
       "      <th>W</th>\n",
       "      <th>X</th>\n",
       "      <th>Y</th>\n",
       "      <th>Z</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>A</th>\n",
       "      <td>-0.747489</td>\n",
       "      <td>1.709142</td>\n",
       "      <td>-0.544701</td>\n",
       "      <td>-0.008810</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>B</th>\n",
       "      <td>-0.028248</td>\n",
       "      <td>0.061550</td>\n",
       "      <td>-0.327798</td>\n",
       "      <td>0.011397</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>C</th>\n",
       "      <td>-0.055215</td>\n",
       "      <td>-0.434698</td>\n",
       "      <td>-0.083334</td>\n",
       "      <td>0.445915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>D</th>\n",
       "      <td>-1.438141</td>\n",
       "      <td>-0.314142</td>\n",
       "      <td>-0.210444</td>\n",
       "      <td>-0.196216</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>E</th>\n",
       "      <td>1.228846</td>\n",
       "      <td>1.191585</td>\n",
       "      <td>0.490549</td>\n",
       "      <td>-0.698623</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          W         X         Y         Z\n",
       "A -0.747489  1.709142 -0.544701 -0.008810\n",
       "B -0.028248  0.061550 -0.327798  0.011397\n",
       "C -0.055215 -0.434698 -0.083334  0.445915\n",
       "D -1.438141 -0.314142 -0.210444 -0.196216\n",
       "E  1.228846  1.191585  0.490549 -0.698623"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
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
