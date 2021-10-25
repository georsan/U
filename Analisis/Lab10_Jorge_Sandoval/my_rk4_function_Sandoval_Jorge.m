function[y,E] = my_rk4_function_Sandoval_Jorge(h,xi,xf)
clc;
format long;
x = xi:h:xf;
y = zeros(1,length(x));
y(1) = 1/10;
F_xy = @(t,r) exp(-2*t)-2*r;
f = @(t) 1/10.*exp(-2*t)+t.*exp(-2*t);
real = f(0.4);
for i=1:(length(x)-1)
    k_1 = F_xy(x(i),y(i));
    k_2 = F_xy(x(i)+0.5*h,y(i)+0.5*h*k_1);
    k_3 = F_xy((x(i)+0.5*h),(y(i)+0.5*h*k_2));
    k_4 = F_xy((x(i)+h),(y(i)+k_3*h));
    y(i+1) = y(i) + (1/6)*(k_1+2*k_2+2*k_3+k_4)*h;
end
E = abs(real-y(length(x)));
end