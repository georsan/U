function my_newton_function_Sandoval_Jorge(fun,p0,iter)
syms x;
xk=p0;
der = matlabFunction(diff(fun,x));
for i=1:iter
    root=xk-(fun(xk)/der(xk));
    error=abs(xk-root);
    xk=root;
    
   disp("Estamos en la iteración "+ i);
   disp("El valor de la raiz en la iteracion es "+xk);
   disp("EL valor de la funcion evaluada en "+xk+" es "+fun(xk));
   disp("EL valor de la derivada evaluada en "+xk+" es "+der(xk));
   disp("El error absoluto es "+error);
   disp(" ")
end
disp(root)
end
