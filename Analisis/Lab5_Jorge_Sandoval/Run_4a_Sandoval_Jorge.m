

%Script
A=[10 15 40;1 -1 -1;0 1 -2];
b=[300;0;0];
[L,U]=my_lu_Sandoval_Jorge(A);
X=U\(L\b);
X


