X = [-8 -2 0 4 6]; 
Y = [6.8 5.0 2.2 0.5 -1.3]; 
Fx = [7.32 3.81 2.64 0.30 -0.87];
n=size(X,2);
[A,B]=my_isline_Sandoval_Jorge(X,Y);
er=0;
for i=1:n
    er = er + (abs(Fx(i)-Y(i)))^2;
    
end
Er = sqrt(er/n);
disp('El error es ');
disp(Er);