using System;

namespace ConsoleApp1
{
    class Simple
    {


        static void Main(string[] args)
        {
            colores();
            /*
            string hex_valor = "2CF";
            int int_valor = Convert.ToInt32(hex_valor, 16);
            Console.WriteLine("numero hexadecimal = {0}", hex_valor);
            Console.WriteLine("numero decimal = {0}", int_valor);
            Console.ReadLine();
            int hexadecimalDecimal(String hexadecimal)
            {
                int result = 0;
                int contar = hexadecimal.Length - 1;
                for (int i = 0; i < hexadecimal.Length; i++)
                {
                    int conversion = 0;
                    switch (hexadecimal[i])
                    {
                        case 'A': conversion = 10; break;
                        case 'B': conversion = 11; break;
                        case 'C': conversion = 12; break;
                        case 'D': conversion = 13; break;
                        case 'E': conversion = 14; break;
                        case 'F': conversion = 15; break;
                        default: conversion = -48 + (int)hexadecimal[i]; break; // -48 because of ASCII
                    }
                    result += conversion * (int)(Math.Pow(16, contar));
                    contar--;
                }
                return result;
            }
            */
            string hexadecimal = "2CF";
            int numero = 0;
            int j = 0;

            const int DIVISOR = 16;

            for (int i = 0; i < hexadecimal.Length; i++)
            {

                
                
                if (hexadecimal[i] >= '0' && hexadecimal[i] <= '9')
                {
                    j = hexadecimal.Length - 1;
                    numero += (int)Math.Pow(DIVISOR, j) * Convert.ToInt32(hexadecimal[i] + "");
                    j--;
                }
                else if (hexadecimal[i] >= 'A' && hexadecimal[i] <= 'F')
                {
                    j = hexadecimal.Length - 1;
                    numero += (int)Math.Pow(DIVISOR, j) * Convert.ToInt32((hexadecimal[i] - 'A' + 10) + "");
                    j--;
                }
                else
                {
                    numero = numero - 1;
                }
                

            }

          


            Console.WriteLine(numero);
        }

        
















        public static long SumaDesendente(long nn1)
        {
            /*
             * //Declaro Variables
            long n1, cantidad, numero, p1, p2, p3, p4, p5, p6, p7, p8, p9, resultado;
            //ingreso el numero
            n1 = long.Parse(Console.ReadLine());
            numero = n1;
            //Metodo para contar las cifras del numero y cantidad es igual a la cantidad de cifras
            cantidad = SumaDesendente(n1);

            if (cantidad == 3)
            {
                p1 = numero % 100;
                p2 = p1 % 10;
                resultado = numero + p1 + p2;
                Console.WriteLine(resultado);
            }
            if (cantidad == 4)
            {
                p1 = numero % 1000;
                p2 = p1 % 100;
                p3 = p2 % 10;
                resultado = numero + p1 + p2 + p3;
                Console.WriteLine(resultado);
            } else if (cantidad == 5)
            {
                p1 = numero % 10000;
                p2 = p1 % 1000;
                p3 = p2 % 100;
                p4 = p3 % 10;
                resultado = numero + p1 + p2 + p3 + p4;
                Console.WriteLine(resultado);
            } else if (cantidad == 6)
            {
                p1 = numero % 100000;
                p2 = p1 % 10000;
                p3 = p2 % 1000;
                p4 = p3 % 100;
                p5 = p4 % 10;
                resultado = numero + p1 + p2 + p3 + p4 + p5;
                Console.WriteLine(resultado);
            } else if (cantidad == 7)
            {
                p1 = numero % 1000000;
                p2 = p1 % 100000;
                p3 = p2 % 10000;
                p4 = p3 % 1000;
                p5 = p4 % 100;
                p6 = p5 % 10;
                resultado = numero + p1 + p2 + p3 + p4 + p5 + p6;
                Console.WriteLine(resultado);
            } else if (cantidad == 8)
            {
                p1 = numero % 10000000;
                p2 = p1 % 1000000;
                p3 = p2 % 100000;
                p4 = p3 % 10000;
                p5 = p4 % 1000;
                p6 = p5 % 100;
                p7 = p6 % 10;
                resultado = numero + p1 + p2 + p3 + p4 + p5 + p6 + p7;
                Console.WriteLine(resultado);
            } else if (cantidad == 9)
            {
                p1 = numero % 100000000;
                p2 = p1 % 10000000;
                p3 = p2 % 1000000;
                p4 = p3 % 100000;
                p5 = p4 % 10000;
                p6 = p5 % 1000;
                p7 = p6 % 100;
                p8 = p7 % 10;
                resultado = numero + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8;
                Console.WriteLine(resultado);
            } else if (cantidad == 9)
            {
                p1 = numero % 1000000000;
                p2 = p1 % 100000000;
                p3 = p2 % 10000000;
                p4 = p3 % 1000000;
                p5 = p4 % 100000;
                p6 = p5 % 10000;
                p7 = p6 % 1000;
                p8 = p7 % 100;
                p9 = p8 % 100;
                resultado = numero + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9;
                Console.WriteLine(resultado);
            }
            */
            long contador;
            contador = 0;
            while (nn1 > 0)
            {
                nn1 = nn1 / 10;
                contador = contador + 1;
            }
            return contador;
        }
        public static void colores()
        {
            Console.BackgroundColor = ConsoleColor.Yellow;
            Console.ForegroundColor = ConsoleColor.Black;
            Console.Clear();

        }
        public class calculadora
        {
            /*
             * //Declaro variables
            int resultado,A,B,opcion;
            //encabezado
            Console.WriteLine("CALCULADORA DE CONSOLA");
            //Leo los datos
            Console.WriteLine("MENU:\n" +
                "1. Suma\n2. Resta\n3. Multiplicaciòn\n4. Diviciòn");
            //nro1 = int.Parse(Console.ReadLine());
            Console.WriteLine("QUE OPERACIÒN VAS HACER?");
            opcion = int.Parse(Console.ReadLine());
            Console.WriteLine("PON EL PRIMER NUMERO");
            A = int.Parse(Console.ReadLine());
            Console.WriteLine("PON EL SEGUNDO NUMERO");
            B = int.Parse(Console.ReadLine());
            resultado = 0;
            //Ejecuto el modulo segun la opciòn
            switch (opcion)
            {
                case 1:
                    {
                        resultado = calculadora.suma(A,B);
                        break;
                    }
                case 2:
                    {
                        resultado = calculadora.resta(A, B);
                        break;
                    }
                case 3:
                    {
                        resultado = calculadora.multiplicacion(A, B);
                        break;
                    }
                case 4:
                    {
                        resultado = calculadora.division(A, B);
                        break;
                    }
            }
            //Salida
            Console.WriteLine("LA OPERACIÒN QUE ESTAS HACIENDO ENTRE " + A + " Y " + B + " DA COMO RESULTADO " + resultado);
            */
            public static int suma(int n1, int n2)
            {
                return n1 + n2;
            }
            public static int resta(int n1, int n2)
            {
                return n1 - n2;
            }
            public static int multiplicacion(int n1, int n2)
            {
                return n1 * n2;
            }
            public static int division(int n1, int n2)
            {
                return n1 / n2;
            }

            /*
            //encabezado
            Console.WriteLine("CALCULADORA DE CONSOLA");
            //declarar variables
            int A, B, opcion, resultado;
            //leer datos

            Console.WriteLine("MENU:\n" +
                "1. Suma\n2. Resta\n3. Multiplicaciòn\n4. Diviciòn");
            //nro1 = int.Parse(Console.ReadLine());
            Console.WriteLine("QUE OPERACIÒN VAS HACER?");
            opcion = int.Parse(Console.ReadLine());
            Console.WriteLine("PON EL PRIMER NUMERO");
            A = int.Parse(Console.ReadLine());
            Console.WriteLine("PON EL SEGUNDO NUMERO");
            B = int.Parse(Console.ReadLine());
            resultado = 0;

            switch (opcion)
            {
                case 1:
                    {
                        resultado = A + B;

                        break;
                    }
                case 2:
                    {
                        resultado = A - B;

                        break;
                    }
                case 3:
                    {
                        resultado = A * B;

                        break;
                    }
                case 4:
                    {
                        resultado = A / B;

                        break;
                    }
            }
            Console.WriteLine("LA OPREACION QUE ESTAS HACIENDO ES " + A + " Y " + B + " DA COMO RESULTADO " + resultado);
            */
        }
        public static void invertirNumero()
        {
            //declarar variables
            int nro1, A, B, C, nroIV;
            //leer datos
            Console.WriteLine("PON UN NUMERO DE TRES CIFRAS");
            nro1 = int.Parse(Console.ReadLine());

            A = nro1 / 100;
            nro1 = nro1 % 100;
            B = nro1 / 10;
            C = nro1 % 10;
            nroIV = ((C * 100) + (B * 10) + (A));
            string p1 = ("ahora si\n");
            string p2 = (@"estoy haciendo una\\pequeña pueba");

            Console.WriteLine("FELICIDADES EL NUMERO INVERTIDO ES " + nroIV);
            Console.WriteLine(p1);
            Console.WriteLine(p2);
        }
        public static void buscarMayor()
        {
            //encabezado
            Console.WriteLine("ESTA APLICACIÒN ENCUENTRA EL NUMERO MAYOR ENTRE TRES NUMEROS");
            //declarar variables
            int nro1, nro2, nro3;
            //leer datos
            Console.WriteLine("PON EL PRIMER NUMERO");
            nro1 = int.Parse(Console.ReadLine());
            Console.WriteLine("PON EL SEGUNDO NUMERO");
            nro2 = int.Parse(Console.ReadLine());
            Console.WriteLine("PON EL TERCER NUMERO");
            nro3 = int.Parse(Console.ReadLine());
            //procesos
            if (nro1 > nro2 && nro1 > nro3)
            {
                Console.WriteLine("EL NUMERO MAYOR ES " + nro1);
            }
            if (nro2 > nro1 && nro2 > nro3)
            {
                Console.WriteLine("EL NUMERO MAYOR ES " + nro2);
            }
            if (nro3 > nro1 && nro3 > nro2)
            {
                Console.WriteLine("EL NUMERO MAYOR ES " + nro3);
            }

        }
        public static void mayorAmenor()
        {
            //encabezado
            Console.WriteLine("ESTA APLICACIÒN ORDENA TRES NUMERO DE MAYOR A MENOR");
            //declarar variables
            int nro1, nro2, nro3, Myor, Mdio, Mnor;
            //leer datos
            Console.WriteLine("PON EL PRIMER NUMERO");
            nro1 = int.Parse(Console.ReadLine());
            Console.WriteLine("PON EL SEGUNDO NUMERO");
            nro2 = int.Parse(Console.ReadLine());
            Console.WriteLine("PON EL TERCER NUMERO");
            nro3 = int.Parse(Console.ReadLine());
            Myor = 0;
            Mdio = 0;
            Mnor = 0;
            //procesos
            if (nro1 > nro2 && nro1 > nro3)
            {
                Myor = nro1;
            }
            else
            {
                if (nro2 > nro1 && nro2 > nro3)
                {
                    Myor = nro2;
                }
                else
                {
                    if (nro3 > nro1 && nro3 > nro2)
                    {
                        Myor = nro3;
                    }
                }
            }

            if (nro1 < nro2 && nro1 < nro3)
            {
                Mnor = nro1;
            }
            else
            {
                if (nro2 < nro1 && nro2 < nro3)
                {
                    Mnor = nro2;
                }
                else
                {
                    if (nro3 < nro1 && nro3 < nro2)
                    {
                        Mnor = nro3;
                    }
                }
            }

            if (nro1 != Myor && nro1 != Mnor)
            {
                Mdio = nro1;
            }
            else
            {
                if (nro2 != Myor && nro2 != Mnor)
                {
                    Mdio = nro2;
                }
                else
                {
                    if (nro3 != Myor && nro3 != Mnor)
                    {
                        Mdio = nro3;
                    }
                }
            }

            Console.WriteLine("EL ORDEN ADECUADO DE LOS TRES NUMEROS ES " + Myor + Mdio + Mnor);


        }
        public static void try1()
        {
            Console.WriteLine("ESCRIBE UN NUMERO");
            string valorIngresado = Console.ReadLine();
            //Este condigo es para tener presente los errores del usurio para que nuestro programa cargue bien
            try
            {
                int valorComoInt = int.Parse(valorIngresado);
            }
            catch (FormatException)
            {
                Console.WriteLine("EL CARACTER O EL VALOR INGRESADO ES INCORRECTO");
            }
            catch (OverflowException)
            {
                Console.WriteLine("EL TAMAÑO DEL NUMERO INGRESADO ES DEMACIODO GRANDE O DEMACIADO CORTO");
            }
            catch (ArgumentNullException)
            {
                Console.WriteLine("NO HAS INGRESADO NINGUN VALOR");
            }
            finally
            {
                Console.WriteLine("ESTE MENSAJE SE MOSTRARA SIEMPRE COMO PRUEBA");
            }
        }
        public static void mcmTresNumeros()
        {
            int M1, M2, M3, mcd, c, mcm;
            M1 = int.Parse(Console.ReadLine());
            M2 = int.Parse(Console.ReadLine());
            M3 = int.Parse(Console.ReadLine());

            c = 2;
            mcd = 1;

            while (c <= M1 && c <= M2 && c <= M3)
            {
                while (M1 % c == 0 && M2 % c == 0 && M3 % c == 0)
                {
                    mcd = mcd * c;
                    M1 = M1 * c;
                    M2 = M2 * c;
                    M3 = M3 * c;

                }
                c = c + 1;
            }
            mcm = (M1 * M2 * M3) / mcd;
            Console.WriteLine(mcd.ToString() + mcm);
        }
        public static void MCMtresNumeros()
        {
            //Entradas
            int m1, m2, m3, a, b, c;
            int mayor, Mcm;
            m1 = Convert.ToInt32(Console.ReadLine());
            m2 = Convert.ToInt32(Console.ReadLine());
            m3 = Convert.ToInt32(Console.ReadLine());
            //Proceso
            mayor = m1;
            if (m2 > mayor)
                mayor = m2;
            if (m3 > mayor)
                mayor = m3;
            Mcm = mayor;
            a = Mcm % m1;
            b = Mcm % m2;
            c = Mcm % m3;
            Console.WriteLine(a);
            Console.WriteLine(b);
            Console.WriteLine(c);
            while ((Mcm % m1 != 0) || (Mcm % m2 != 0) || (Mcm % m3 != 0))
            {
                Console.WriteLine(Mcm);
                Mcm = Mcm + 1;
            }

            //Salida

            Console.WriteLine(Mcm);
        }
        public static int Mayor(int n1, int n2)
        {
            /*
             * Este codigo hay que pegarlo en el main
             * //Declaro Variables
            int Numero1, Numero2, resultado;
            //Leo los datos
            Console.WriteLine("PON EL PRIMER NUMERO");
            Numero1=int.Parse(Console.ReadLine());
            Console.WriteLine("PON EL SEGUNDO NUMERO");
            Numero2 = int.Parse(Console.ReadLine());
            //Ejecuto el modulo
            resultado = Mayor(Numero1,Numero2);
            Console.WriteLine("EL NUMERO MAYOR ES EL "+resultado);
            */
            if (n1 > n2)
                return n1;
            else
                return n2;
            /*
            if (n1 > n2)
                Console.WriteLine("El numero mayor es {0}", n1);
            else
                Console.WriteLine("El numero mayor es {0}", n2);
            */
        }
        public static int IfMasCorto(int N1, int N2)
        {
            int Resultado;
            /*
             * **
             * int A, B,R;
            A = int.Parse(Console.ReadLine());
            B = int.Parse(Console.ReadLine());
            R = IfMasCorto(A, B);
            Console.WriteLine(R);
            ****
            if (N1 > N2)
            {
                Resultado = N1 + N2;
                return Resultado;
            }
            else
                return N1 - N2;
            */
            Resultado = N1 > N2 ? N1 + N2 : N1 - N2;
            return Resultado;
        }
        public class hola
        {
            public static void while1al10 ()
            {
                int a, b;
                a = 1;
                b = 11;
                while(a<b)
                {
                    Console.WriteLine(a);
                    a = a + 1;
                }
            }
            public static void Pares26al10()
            {
                int a, b;
                a = 26;
                b = 8;
                while (a > b)
                {
                    Console.WriteLine(a);
                    a = a - 2;
                }
            }
            public static void DoWhile1al10()
            {
                int a, b;
                a = 1;
                b = 11;
                do
                {
                    Console.WriteLine(a);
                    a = a + 1;
                } while (a < b);
            }
            public static void del15al5Desen()
            {
                for (int i = 15; i > 4; i--)
                {
                    Console.WriteLine(i);
                }
            }
            public static void Primeros8pares()
            {
                for (int i = 2; i <= 16; i=i+2)
                {
                    int p = 1;
                    Console.WriteLine("Numero "+p+"es el "+i);
                    
                    
                }
            }
        }

        public static String decimalHexadecimal(int numero)
        {

            char[] letras = { 'A', 'B', 'C', 'D', 'E', 'F' };

            String hexadecimal = "";

            const int DIVISOR = 16;
            long resto = 0;

            for (int i = numero % DIVISOR, j = 0; numero > 0; numero /= DIVISOR, i = numero % DIVISOR, j++)
            {
                resto = i % DIVISOR;
                Console.WriteLine(i);
                if (resto >= 10)
                {
                    hexadecimal = letras[resto - 10] + hexadecimal;

                }
                else
                {
                    hexadecimal = resto + hexadecimal;
                }
            }
            return hexadecimal;
        }
        public static int hexadecimalDecimal(String hexadecimal)
        {

            int numero = 0;

            const int DIVISOR = 16;

            for (int i = 0, j = hexadecimal.Length - 1; i < hexadecimal.Length; i++, j--)
            {

                if (hexadecimal[i] >= '0' && hexadecimal[i] <= '9')
                {
                    numero += (int)Math.Pow(DIVISOR, j) * Convert.ToInt32(hexadecimal[i] + "");
                }
                else if (hexadecimal[i] >= 'A' && hexadecimal[i] <= 'F')
                {
                    numero += (int)Math.Pow(DIVISOR, j) * Convert.ToInt32((hexadecimal[i] - 'A' + 10) + "");
                }
                else
                {
                    return -1;
                }

            }

            return numero;

        }
        public static long decimalBinario(int numero)
        {

            long binario = 0;

            const int DIVISOR = 2;
            long digito = 0;

            for (int i = numero % DIVISOR, j = 0; numero > 0; numero /= DIVISOR, i = numero % DIVISOR, j++)
            {
                digito = i % DIVISOR;
                binario += digito * (long)Math.Pow(10, j);
            }


            return binario;
        }
        public static void lecturaDeCaracter(string letras)
        {
            for (int i = 0; i < letras.Length; i++)
            {
                int a = letras[i];
                Console.WriteLine(a);
                //Console.WriteLine(letras.Length);
                //Console.WriteLine(letras[i]);
            }
        }
        public static string BinarioaHexadecimal(long binario)
        {
            int numero = 0;
            int digito = 0;
            const int DIVISOR = 10;
            for (long i = binario, j = 0; i > 0; i /= DIVISOR, j++)
            {
                digito = (int)i % DIVISOR;
                if (digito != 1 && digito != 0)
                {
                    numero = numero - 1;
                }
                numero += digito * (int)Math.Pow(2, j);
            }
            //La variable numero hasta aqui es un numero decimal entero
            //return numero;
            char[] letras = { 'A', 'B', 'C', 'D', 'E', 'F' };

            String hexadecimal = "";

            const int DIVISOR2 = 16;
            long resto = 0;

            for (int i = numero % DIVISOR2, j = 0; numero > 0; numero /= DIVISOR2, i = numero % DIVISOR2, j++)
            {
                resto = i % DIVISOR2;
                if (resto >= 10)
                {
                    hexadecimal = letras[resto - 10] + hexadecimal;

                }
                else
                {
                    hexadecimal = resto + hexadecimal;
                }
            }
            return hexadecimal;
        }
        public static long DecimalaOctal(long Decimal)
        {
            long p, q, Octal = 0;
            long DecimalNumero = Decimal;
            p = 1;
            for (q = DecimalNumero; q > 0; q = q / 8)
            {
                Octal = Octal + (q % 8) * p;
                p *= 10;
                DecimalNumero /= 8;
            }
            return Octal;
        }
        public static string DecimalaHexadecimal(long Decimal)
        {
            char[] letras = { 'A', 'B', 'C', 'D', 'E', 'F' };
            String hexadecimal = "";
            const int DIVISOR2 = 16;
            long resto = 0;
            for (long i = Decimal % DIVISOR2, j = 0; Decimal > 0; Decimal /= DIVISOR2, i = Decimal % DIVISOR2, j++)
            {
                resto = i % DIVISOR2;
                if (resto >= 10)
                {
                    hexadecimal = letras[resto - 10] + hexadecimal;
                }
                else
                {
                    hexadecimal = resto + hexadecimal;
                }
            }
            return hexadecimal;
        }
        public static long OctalaBinario(long octal)
        {
            long numero = 0;
            long digito = 0;
            const int DIVISOR = 10;
            for (long i = octal, j = 0; i > 0; i /= DIVISOR, j++)
            {
                digito = (long)i % DIVISOR;
                if (!(digito >= 0 && digito <= 7))
                {
                    return -1;
                }
                numero += digito * (long)Math.Pow(8, j);
            }
            //return numero;
            //La variable numero es un decimal
            long binario = 0;
            const int DIVISOR2 = 2;
            long digito2 = 0;
            for (long i = numero % DIVISOR2, j = 0; numero > 0; numero /= DIVISOR2, i = numero % DIVISOR2, j++)
            {
                digito2 = i % DIVISOR2;
                binario += digito2 * (long)Math.Pow(10, j);
            }
            return binario;
        }
        public static long OctalaDecimal(long octal)
        {
            long numero = 0;
            long digito = 0;
            const int DIVISOR = 10;
            for (long i = octal, j = 0; i > 0; i /= DIVISOR, j++)
            {
                digito = (long)i % DIVISOR;
                if (!(digito >= 0 && digito <= 7))
                {
                    return -1;
                }
                numero += digito * (long)Math.Pow(8, j);
            }
            return numero;
        }
        public static string OctalaHexadecimal(long octal)
        {
            long numero = 0;
            long digito = 0;
            const int DIVISOR = 10;
            for (long i = octal, j = 0; i > 0; i /= DIVISOR, j++)
            {
                digito = (long)i % DIVISOR;
                if (!(digito >= 0 && digito <= 7))
                {
                    numero = numero - 1;
                }
                numero += digito * (long)Math.Pow(8, j);
            }
            //return numero;
            //La varible numero es el valor de octal a decimal
            //Ahora sigue cambiar el decimal a hexadecimal
            char[] letras = { 'A', 'B', 'C', 'D', 'E', 'F' };
            String hexadecimal = "";
            const int DIVISOR2 = 16;
            long resto = 0;
            for (long i = numero % DIVISOR2, j = 0; numero > 0; numero /= DIVISOR2, i = numero % DIVISOR2, j++)
            {
                resto = i % DIVISOR2;
                if (resto >= 10)
                {
                    hexadecimal = letras[resto - 10] + hexadecimal;
                }
                else
                {
                    hexadecimal = resto + hexadecimal;
                }
            }
            return hexadecimal;
        }
        public static long HexadecimalaBinario(string hex)
        {
            long numero = 0;
            const int DIVISOR = 16;
            for (int i = 0, j = hex.Length - 1; i < hex.Length; i++, j--)
            {
                if (hex[i] >= '0' && hex[i] <= '9')
                {
                    numero += (long)Math.Pow(DIVISOR, j) * Convert.ToInt64(hex[i] + "");
                }
                else if (hex[i] >= 'A' && hex[i] <= 'F')
                {
                    numero += (long)Math.Pow(DIVISOR, j) * Convert.ToInt64((hex[i] - 'A' + 10) + "");
                }
                else
                {
                    numero = numero - 1;
                }
            }
            //return numero;
            //La varible numero es el valor de hexadecimal a decimal
            //Ahora sigue cambiar el decimal a binario
            long binario = 0;
            const int DIVISOR2 = 2;
            long digito = 0;
            for (long i = numero % DIVISOR2, j = 0; numero > 0; numero /= DIVISOR2, i = numero % DIVISOR2, j++)
            {
                digito = i % DIVISOR2;
                binario += digito * (long)Math.Pow(10, j);
            }
            return binario;
        }
        public static long HexadecimalaDecimal(string hex)
        {
            long numero = 0;
            const int DIVISOR = 16;
            for (int i = 0, j = hex.Length - 1; i < hex.Length; i++, j--)
            {
                if (hex[i] >= '0' && hex[i] <= '9')
                {
                    numero += (long)Math.Pow(DIVISOR, j) * Convert.ToInt64(hex[i] + "");
                }
                else if (hex[i] >= 'A' && hex[i] <= 'F')
                {
                    numero += (long)Math.Pow(DIVISOR, j) * Convert.ToInt64((hex[i] - 'A' + 10) + "");
                }
                else
                {
                    return -1;
                }
            }
            return numero;
        }
        public static long HexadecimalaOctal(string hex)
        {
            long numero = 0;
            const int DIVISOR = 16;
            for (int i = 0, j = hex.Length - 1; i < hex.Length; i++, j--)
            {
                if (hex[i] >= '0' && hex[i] <= '9')
                {
                    numero += (long)Math.Pow(DIVISOR, j) * Convert.ToInt64(hex[i] + "");
                }
                else if (hex[i] >= 'A' && hex[i] <= 'F')
                {
                    numero += (long)Math.Pow(DIVISOR, j) * Convert.ToInt64((hex[i] - 'A' + 10) + "");
                }
                else
                {
                    return -1;
                }
            }
            //return numero;
            //La variable numero es un decimal
            //ahora vamos a cambiar ese decimal por octal
            long p, q, Octal = 0;
            long DecimalNumero = numero;
            p = 1;
            for (q = DecimalNumero; q > 0; q = q / 8)
            {
                Octal = Octal + (q % 8) * p;
                p *= 10;
                DecimalNumero /= 8;
            }
            return Octal;
        }
       
        

    }
}
