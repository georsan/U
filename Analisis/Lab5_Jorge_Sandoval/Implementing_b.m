A = [1 2 -3 4; 4 8 12 -8; 2 3 2 1; -3 -1 1 -4];
b = [3; 60; 1; 5];

[L,U]=my_lu_Sandoval_Jorge(A);
X=U\(L\b);
X


