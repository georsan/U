k = 1;
f = @(t,m) - k.*m;
a = 0;
b = 1;
M = 5;
ya = 300;
heun = my_heun_function_Sandoval_Jorge(f,a,b,M,ya);
disp(heun);