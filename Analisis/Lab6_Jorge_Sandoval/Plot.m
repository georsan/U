X = [0 1 2 3 4 ];
Y =3*sin((pi*X)/6).^2;
plot(X,Y)

hold on

Y1=my_LagrangePolynomial_Sandoval_Jorge(X,Y);
 plot(X,Y1)

Y2=my_NewtonPolynomial_Sandoval_Jorge(X,Y);
plot(X,Y2)

hold off