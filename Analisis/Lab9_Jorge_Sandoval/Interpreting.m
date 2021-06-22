fun=@(x)exp(-x^2/2);
a=0;
b=5;
M=5;


%%Simpson
I=my_simpson_function_Sandoval_Jorge(fun,a,b,M);
P=1/2+(1/sqrt(2*pi))*I;
P

%%trapezoidal
i=my_trapezoidal_function_Sandoval_Jorge(fun,a,b,M);
p=1/2+(1/sqrt(2*pi))*i;
p