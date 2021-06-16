function [A,B]=my_isline_Sandoval_Jorge(X,Y)
X = X(:);
Y = Y(:);
if  size(X,1)==size(Y,1)
    xm = mean(X);
    ym = mean(Y);
    n=size(X,1);
    numer=0;
    d=0;
    Ex=0;
    Ey=0;  
    for i=1:n
        numer = numer + (X(i,1)-xm)*(Y(i,1)-ym);
        d = d + ((X(i,1)-xm)^2);
        Ey = Ey + Y(i,1);
        Ex = Ex + X(i,1);
    end
XD = numer/d;
B = (Ey-(XD*Ex))/n;

A = num2str(XD);
b = num2str(B);
if b>=0
    fun = strcat('f(x)= ',A,'*X + ',b);
else
    fun = strcat('f(x)= ',A,' *X  ',b);
end
x1 = min(X)-1:0.1:max(X)+1;
z = XD*x1 + B;
plot(x1,z,'LineWidth',2),
title('Gráfica '),
hold on,
axis([min(x1) max(x1) min(z) max(z)])
plot(X,Y,'*','LineWidth',1.5,'color','r'),
hold on,
legend(fun,'(x_k,y_k)','location','southoutside') 
end

end