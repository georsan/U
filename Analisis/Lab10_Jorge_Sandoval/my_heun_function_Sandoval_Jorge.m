function H = my_heun_function_Sandoval_Jorge(f,b,a,n,ya)
h = (b-a)/n;
T = zeros(1,n+1);
Y = zeros(1,n+1);
T = a:h:b;
Y(1) = ya;
for j=1:n
    k1 = feval(f,T(j),Y(j));
    k2 = feval(f,T(j+1),Y(j)+h*k1);
    Y(j+1) = Y(j) + (h/2) * (k1+k2);
end
H = [T' Y'];