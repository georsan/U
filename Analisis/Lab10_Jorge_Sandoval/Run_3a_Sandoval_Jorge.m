k=1;
a=0;
b=1;
ya=300;
M=5;
f= @(t,m)-k.*m;
euler=my_euler_function_Sandoval_Jorge(f,a,b,ya,M);
disp(euler);