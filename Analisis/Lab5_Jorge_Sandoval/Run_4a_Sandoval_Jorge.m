%Ecuación
%---------------
%10P+15M+40G=300
%P-M-G=0
%M-2G=0
%---------------

%Script
A=[10 15 40;1 -1 -1;0 1 -2];
b=[300;0;0];
[L,U]=my_lu_Sandoval_Jorge(A);
X=U\(L\b);
X

%Sophia necesita vender 9 pequeñas , 6 medianas y 3 grandes.
