# EmulatorZ80
Emulator of the microprocessor z80 for the programming languages course.

## NOTAS
* Manejar todo en hexadecimal, solo binario cuando sea requerido
* todo se va a manejar en un byte (8 bits)


## Modules
**Assembler**
* Reads assembly from a text file.
* Dictionary with the machine code for each instruction.
* Generates relocatable machine code, by changing words into binary numbers.
* The result of the previous step is saved into a file.

**Linker__loader
* Leer las instrucciones ya ensambladas y generar los espacios(direcciones de registros) en memoria para cada instruccion
* establecer el program counter(Contiene la dirección de la próxima instrucción.) y el stack pointer(Contiene la dirección de la parte superior de la pila. Ver push o pop en el set de instrucciones.)

**Z80 
* hacer la funcionalidad de cada instruccion recibida por el link_loader
* establecer los registros para las intrucciones
