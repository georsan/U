Y = [87.97 224.70 365.26 686.98 4332.59 10759.22 30685.40 60189].*86400; 
X = [57.91 108.70 149.60 227.92 778.57 1433.53 2872.46 4495.06].*10^9;
n=size(Y,2);
 for i=1:n
 X(i)=log10(X(i).^3);
 Y(i)=log10(Y(i).^2);
 end
 
[A,B]=my_isline_Sandoval_Jorge(X,Y);

%%%%%%%%%%%%%%%%

C=4*(pi)^2/((6.674*10^-11)*(1.989*10^30));
c=10^B;
%error absoluto
Er=abs(C-c);
%error relativo
Ea=Er/C;
disp('el error absoluto es ');
disp(Ea)
