# -*- coding: utf-8 -*-
# Copyright (C) Scott Coughlin (2017 - 2020)
#
# This file is part of cosmic.
#
# cosmic is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cosmic is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cosmic.  If not, see <http://www.gnu.org/licenses/>.

import numpy

__author__ = 'Scott Coughlin <scott.coughlin@ligo.org>'

"""

*       Initialization eata set for fitting formulae.
*       -----------------------------------------------------------
*
      real*8 xz(76),xt(31),xl(72),xr(119),xg(112),xh(99)
*
* eata for Lzams(1->35) ane Rzams(36->76)
*
"""
xz = numpy.array([
       3.970417e-01, -3.2913574e-01, 3.4776688e-01, 3.7470851e-01,
       9.011915e-02,
       8.527626e+00,-2.441225973e+01, 5.643597107e+01, 3.706152575e+01,
       5.4562406e+00,
       2.5546e-04, -1.23461e-03, -2.3246e-04,  4.5519e-04,
       1.6176e-04,
       5.432889e+00, -8.62157806e+00, 1.344202049e+01,
       1.451584135e+01, 3.39793084e+00,
       5.563579e+00,-1.032345224e+01, 1.944322980e+01,
       1.897361347e+01, 4.16903097e+00,
       7.8866060e-01, -2.90870942e+00,  6.54713531e+00,
       4.05606657e+00, 5.3287322e-01,
       5.86685e-03, -1.704237e-02, 3.872348e-02, 2.570041e-02,
       3.83376e-03,
       1.715359e+00, 6.2246212e-01, -9.2557761e-01, -1.16996966e+00,
      -3.0631491e-01,
       6.597788e+00, -4.2450044e-01,-1.213339427e+01,-1.073509484e+01,
      -2.51487077e+00,
       1.008855000e+01, -7.11727086e+00,-3.167119479e+01,
      -2.424848322e+01,-5.33608972e+00,
       1.012495e+00, 3.2699690e-01, -9.23418e-03, -3.876858e-02,
      -4.12750e-03,
       7.490166e-02, 2.410413e-02, 7.233664e-02, 3.040467e-02,
       1.97741e-03, 1.077422e-02,
       3.082234e+00, 9.447205e-01, -2.15200882e+00, -2.49219496e+00,
      -6.3848738e-01,
       1.784778e+01, -7.4534569e+00,-4.896066856e+01,-4.005386135e+01,
      -9.09331816e+00,
       2.2582e-04, -1.86899e-03, 3.88783e-03, 1.42402e-03,-7.671e-05])

"""
*
* eata for Tbgb(1->17) ane Thook(18->31)
*
"""

xt =numpy.array([1.593890e+03, 2.053038e+03, 1.231226e+03,
              2.327785e+02, 2.706708e+03, 1.483131e+03,
              5.772723e+02, 7.411230e+01, 1.466143e+02,
             -1.048442e+02,-6.795374e+01,-1.391127e+01,
              4.141960e-02, 4.564888e-02, 2.958542e-02,
              5.571483e-03, 3.426349e-01,
              1.949814e+01, 1.758178e+00,-6.008212e+00,
             -4.470533e+00, 4.903830e+00, 5.212154e-02,
              3.166411e-02,-2.750074e-03,-2.271549e-03,
              1.312179e+00,-3.294936e-01, 9.231860e-02,
              2.610989e-02, 8.073972e-01])

"""
*
* eata for Ltms(1->27), Lalpha(28->43), Lbeta(44->56) ane Lhook(57->72)
*
"""
xl = numpy.array([1.031538e+00,-2.434480e-01, 7.732821e+00,
              6.460705e+00, 1.374484e+00, 1.043715e+00,
             -1.577474e+00,-5.168234e+00,-5.596506e+00,
             -1.299394e+00, 7.859573e+02,-8.542048e+00,
             -2.642511e+01,-9.585707e+00, 3.858911e+03,
              2.459681e+03,-7.630093e+01,-3.486057e+02,
             -4.861703e+01, 2.888720e+02, 2.952979e+02,
              1.850341e+02, 3.797254e+01, 7.196580e+00,
              5.613746e-01, 3.805871e-01, 8.398728e-02,
              2.321400e-01, 1.828075e-03,-2.232007e-02,
             -3.378734e-03, 1.163659e-02, 3.427682e-03,
              1.421393e-03,-3.710666e-03, 1.048020e-02,
             -1.231921e-02,-1.686860e-02,-4.234354e-03,
              1.555590e+00,-3.223927e-01,-5.197429e-01,
             -1.066441e-01,
              3.855707e-01,-6.104166e-01, 5.676742e+00,
              1.060894e+01, 5.284014e+00, 3.579064e-01,
             -6.442936e-01, 5.494644e+00, 1.054952e+01,
              5.280991e+00, 9.587587e-01, 8.777464e-01,
              2.017321e-01,
              1.910302e-01, 1.158624e-01, 3.348990e-02,
              2.599706e-03, 3.931056e-01, 7.277637e-02,
             -1.366593e-01,-4.508946e-02, 3.267776e-01,
              1.204424e-01, 9.988332e-02, 2.455361e-02,
              5.990212e-01, 5.570264e-02, 6.207626e-02,
              1.777283e-02])
"""
*
* eata for Rtms(1->40), Ralpha(41->64), Rbeta(65->83), Rgamma(84->103)
* ane Rhook(104->119)
*
"""
xr = numpy.array([2.187715e-01,-2.154437e+00,-3.768678e+00,
             -1.975518e+00,-3.021475e-01, 1.466440e+00,
              1.839725e+00, 6.442199e+00, 4.023635e+00,
              6.957529e-01, 2.652091e+01, 8.178458e+01,
              1.156058e+02, 7.633811e+01, 1.950698e+01,
              1.472103e+00,-2.947609e+00,-3.312828e+00,
             -9.945065e-01, 3.071048e+00,-5.679941e+00,
             -9.745523e+00,-3.594543e+00,-8.672073e-02,
              2.617890e+00, 1.019135e+00,-3.292551e-02,
             -7.445123e-02, 1.075567e-02, 1.773287e-02,
              9.610479e-03, 1.732469e-03, 1.476246e+00,
              1.899331e+00, 1.195010e+00, 3.035051e-01,
              5.502535e+00,-6.601663e-02, 9.968707e-02,
              3.599801e-02,
              4.907546e-01,-1.683928e-01,-3.108742e-01,
             -7.202918e-02, 4.537070e+00,-4.465455e+00,
             -1.612690e+00,-1.623246e+00, 1.796220e+00,
              2.814020e-01, 1.423325e+00, 3.421036e-01,
              2.256216e+00, 3.773400e-01, 1.537867e+00,
              4.396373e-01, 1.564231e-03, 1.653042e-03,
             -4.439786e-03,-4.951011e-03,-1.216530e-03,
              5.210157e+00,-4.143695e+00,-2.120870e+00,
              1.071489e+00,-1.164852e-01,-8.623831e-02,
             -1.582349e-02, 7.108492e-01, 7.935927e-01,
              3.926983e-01, 3.622146e-02, 3.478514e+00,
             -2.585474e-02,-1.512955e-02,-2.833691e-03,
              3.969331e-03, 4.539076e-03, 1.720906e-03,
              1.897857e-04, 9.132108e-01,-1.653695e-01,
              3.636784e-02,
              1.192334e-02, 1.083057e-02, 1.230969e+00,
              1.551656e+00,-1.668868e-01, 5.818123e-01,
             -1.105027e+01,-1.668070e+01, 7.615495e-01,
              1.068243e-01,-2.011333e-01,-9.371415e-02,
             -1.015564e-01,-2.161264e-01,-5.182516e-02,
             -3.868776e-01,-5.457078e-01,-1.463472e-01,
              9.409838e+00, 1.522928e+00,
              7.330122e-01, 5.192827e-01, 2.316416e-01,
              8.346941e-03, 1.172768e+00,-1.209262e-01,
             -1.193023e-01,-2.859837e-02, 3.982622e-01,
             -2.296279e-01,-2.262539e-01,-5.219837e-02,
              3.571038e+00,-2.223625e-02,-2.611794e-02,
             -6.359648e-03])
"""
*
* eata for Lbgb(1->24), Lbagb(25->44), Rgb(45->66), Ragb(67->100),
* Mchei(101->102) ane Mcbagb(103->112)
*
"""
xg = numpy.array([9.511033e+01, 6.819618e+01,-1.045625e+01,
                 -1.474939e+01, 3.113458e+01, 1.012033e+01,
                 -4.650511e+00,-2.463185e+00, 1.413057e+00,
                  4.578814e-01,-6.850581e-02,-5.588658e-02,
                  3.910862e+01, 5.196646e+01, 2.264970e+01,
                  2.873680e+00, 4.597479e+00,-2.855179e-01,
                  2.709724e-01, 6.682518e+00, 2.827718e-01,
                 -7.294429e-02, 4.637345e+00, 9.301992e+00,
                  1.626062e+02,-1.168838e+01,-5.498343e+00,
                  3.336833e-01,-1.458043e-01,-2.011751e-02,
                  7.425137e+01, 1.790236e+01, 3.033910e+01,
                  1.018259e+01, 9.268325e+02,-9.739859e+01,
                 -7.702152e+01,-3.158268e+01, 1.127018e+01,
                  1.622158e+00,-1.443664e+00,-9.474699e-01,
                  2.474401e+00, 3.892972e-01,
                  9.960283e-01, 8.164393e-01, 2.383830e+00,
                  2.223436e+00, 8.638115e-01, 1.231572e-01,
                  2.561062e-01, 7.072646e-02,-5.444596e-02,
                 -5.798167e-02,-1.349129e-02, 1.157338e+00,
                  1.467883e+00, 4.299661e+00, 3.130500e+00,
                  6.992080e-01, 1.640687e-02, 4.022765e-01,
                  3.050010e-01, 9.962137e-01, 7.914079e-01,
                  1.728098e-01,
                  1.125124e+00, 1.306486e+00, 3.622359e+00,
                  2.601976e+00, 3.031270e-01,-1.343798e-01,
                  3.349489e-01, 4.531269e-03, 1.131793e-01,
                  2.300156e-01, 7.632745e-02, 1.467794e+00,
                  2.798142e+00, 9.455580e+00, 8.963904e+00,
                  3.339719e+00, 4.426929e-01, 4.658512e-01,
                  2.597451e-01, 9.048179e-01, 7.394505e-01,
                  1.607092e-01, 1.110866e+00, 9.623856e-01,
                  2.735487e+00, 2.445602e+00, 8.826352e-01,
                  1.140142e-01,-1.584333e-01,-1.728865e-01,
                 -4.461431e-01,-3.925259e-01,-1.276203e-01,
                 -1.308728e-02,
                  9.796164e-02, 1.350554e+00,
                  1.445216e-01,-6.180219e-02, 3.093878e-02,
                  1.567090e-02, 1.304129e+00, 1.395919e-01,
                  4.142455e-03,-9.732503e-03, 5.114149e-01,
                 -1.160850e-02])
"""
*
* eata for Lhei(1->14), Lhe(15->25) Rmin(26->43), The(44->65),
* Tbl(66->79), Lzahb(80->87) ane Rzahb(88->99)
*
"""
xh = numpy.array([2.751631e+03, 3.557098e+02,
                 -3.820831e-02, 5.872664e-02, 1.5e+01,
                  1.071738e+02,-8.970339e+01,-3.949739e+01,
                  7.348793e+02,-1.531020e+02,-3.793700e+01,
                  9.219293e+00,-2.005865e+00,-5.561309e-01,
                  2.917412e+00, 1.575290e+00, 5.751814e-01,
                  6.371760e-01, 3.880523e-01, 4.916389e+00,
                  2.862149e+00, 7.844850e-01, 3.629118e+00,
                 -9.112722e-01, 1.042291e+00,
                  1.609901e+01, 7.391573e+00, 2.277010e+01,
                  8.334227e+00, 1.747500e-01, 6.271202e-02,
                 -2.324229e-02,-1.844559e-02, 2.752869e+00,
                  2.729201e-02, 4.996927e-01, 2.496551e-01,
                 -9.138012e-02,-3.671407e-01, 3.518506e+00,
                  1.112440e+00,-4.556216e-01,-2.179426e-01,
                  1.314955e+02, 2.009258e+01,-5.143082e-01,
                 -1.379140e+00, 1.823973e+01,-3.074559e+00,
                 -4.307878e+00, 1.5e1,
                  2.327037e+00, 2.403445e+00, 1.208407e+00,
                  2.087263e-01, 1.079113e-01, 1.762409e-02,
                  1.096601e-02, 3.058818e-03, 2.327409e+00,
                  6.901582e-01,-2.158431e-01,-1.084117e-01,
                  1.997378e+00,-8.126205e-01,
                  2.214315e+00,-1.975747e+00, 4.805428e-01,
                  2.471620e+00,-5.401682e+00, 3.247361e+00,
                  5.072525e+00, 1.146189e+01, 6.961724e+00,
                  1.316965e+00, 5.139740e+00, 1.127733e+00,
                  2.344416e-01,-3.793726e-01,
                  5.496045e+01,-1.289968e+01, 6.385758e+00,
                  1.832694e+00,-5.766608e-02, 5.696128e-02,
                  1.211104e+02, 1.647903e+00,
                  2.063983e+00, 7.363827e-01, 2.654323e-01,
                 -6.140719e-02, 2.214088e+02, 2.187113e+02,
                  1.170177e+01,-2.635340e+01, 2.003160e+00,
                  9.388871e-01, 9.656450e-01, 2.362266e-01])
