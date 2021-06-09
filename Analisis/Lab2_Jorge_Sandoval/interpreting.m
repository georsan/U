n = 1500;
fx = 475;
f = @(lam)n*exp(lam)+fx*((exp(lam)-1)/(lam))-2264;

xd = my_bisection_function_Sandoval_Jorge(f,0,1,100);

f(xd)


fplot(f, [0.01 1])
