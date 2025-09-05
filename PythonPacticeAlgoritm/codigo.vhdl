an <= "1110"  --habilitador display de 7 segmentos uno solo

--pines del display
-- 0   0    0   0    0    0    0    0
-- p   g    f   e    d    c    b    a
-- n8  p7   p8  17  n6   m7   110  n9

-- Crear sentencia para definir el encendido del display
segmentos <= "11000000" WHEN datos = "0000" ELSE -- mostrar 0
             "11111001" WHEN datos = "0001" ELSE -- mostrar 1
             "10100100" WHEN datos = "0010" ELSE -- mostrar 2
             "10110000" WHEN datos = "0011" ELSE -- mostrar 3
             "10011001" WHEN datos = "0100" ELSE -- mostrar 4
             "10010010" WHEN datos = "0101" ELSE -- mostrar 5
             "10000011" WHEN datos = "0110" ELSE -- mostrar 6
             "11111000" WHEN datos = "0111" ELSE -- mostrar 7
             "10000000" WHEN datos = "1000" ELSE -- mostrar 8
             "10011000" WHEN datos = "1001" ELSE -- mostrar 9
             "01111111";                       -- apagar (valor por defecto)

# Definir entradas (datos)
NET "datos[0]" LOC = P9;
NET "datos[1]" LOC = R9;
NET "datos[2]" LOC = T7;
NET "datos[3]" LOC = T6;

# Definir habilitador del display
NET "an[0]" LOC = M11;
NET "an[1]" LOC = P11;
NET "an[2]" LOC = M10;
NET "an[3]" LOC = M9;

# Definir pines del display 7 segmentos
NET "segmentos[0]" LOC = N9;
NET "segmentos[1]" LOC = L10;
NET "segmentos[2]" LOC = M8;
NET "segmentos[3]" LOC = M7;
NET "segmentos[4]" LOC = L7;
NET "segmentos[5]" LOC = P8;
NET "segmentos[6]" LOC = P7;
NET "segmentos[7]" LOC = N8;


datos <= "0000"; wait for 100 ns; 
datos <= "1000"; wait for 100 ns; 
datos <= "0111"; wait for 100 ns;