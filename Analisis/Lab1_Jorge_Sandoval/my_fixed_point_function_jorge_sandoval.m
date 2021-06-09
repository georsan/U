function P=my_fixed_point_function_jorge_sandoval(fun,a,b,p0,Iter)
if p0<a || p0>b
    msg='Error p0 fuera del rango';
    error(msg);
else
    for i=1:Iter
        p0=fun(p0);
    end
    P=p0;
end
end