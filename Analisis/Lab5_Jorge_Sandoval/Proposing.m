%Papo desea conocer la edad actual de cada integrante de su familia,sabe
%que la suma de las edades actuales son 80,dentro de 22 años La edad de que
%el tiene sera la mitad de la edad de su madre,si el padre es un año mayor
%a a la esposa.Encontrar la edad actual de cada uno

%Ecuacion 
%X + Y + Z = 80
%X -2Z = 22
%X - Y = -1

%Script
A=[1 1 1;1 0 -2;1 -1 0];
b=[80;22;-1];
[L,U]=my_lu_Sandoval_Jorge(A);
X=U\(L\b);
X