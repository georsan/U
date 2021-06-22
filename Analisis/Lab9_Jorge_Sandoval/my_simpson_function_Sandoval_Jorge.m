function[I]=my_simpson_function_Sandoval_Jorge(fun,a,b,M )
    h=(b-a)/M;
    s=fun(a)+fun(b);
    for i=1:2:M-1
        s=s+4*fun(a+i*h);
    end
    for i=2:2:M-2
        s=s+2*fun(a+i*h);
    end
    I=h/3*s;
   
end