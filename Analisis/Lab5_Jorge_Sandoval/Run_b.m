A = [1 2 -3 4; 4 8 12 -8; 2 3 2 1; -3 -1 1 -4];
b = [3; 60; 1; 5];

[L,U]=my_lu_Sandoval_Jorge(A);
X=U\(L\b);
X

%C.
%Se pudo observar que con la función lu() los valores de L y U son
%diferentes a los obtenidos por la función que my_lu_Sandoval_Jorge eso es
%debido a la diferencia de como se programo la ultima función
%por lo tanto se puede inferir que hay diferentes metodos para desarrollar dicho algoritmo.