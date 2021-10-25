[y,E] = my_rk4_function_Sandoval_Jorge(0.2,0,0.4);
disp('Valores calculados por RK para h = 0.2: ')
disp(y);
disp('Error del valor de la función en 0.4 en RK con respecto al real:')
disp(E);

[y,E] = my_rk4_function_Sandoval_Jorge(0.1,0,0.4);
disp('Valores calculados por RK para h = 0.1')
disp(y);
disp('Error del valor de la función en 0.4 en RK con respecto al real:')
disp(E);