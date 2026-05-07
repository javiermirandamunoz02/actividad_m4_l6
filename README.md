# actividad_m4_l6
actividad_m4_l6

¿Qué diferencia notaste entre write() y append()?


write (modo 'w'): Borra todo lo que existe en el archivo y escribe desde cero. Si el archivo no existe, lo crea.

append (modo 'a'): Mantiene lo que ya estaba escrito y agrega el nuevo texto al final.

¿Qué ventaja tiene usar with open(...) frente a abrir y cerrar manualmente?


Seguridad: El bloque with cierra el archivo automáticamente, incluso si el programa falla o hay un error.

Orden: Evita que el archivo quede "bloqueado" por el sistema operativo, lo que permite que otros programas lo usen sin problemas.

Eficiencia: Te ahorras escribir .close() y aseguras que los datos se guarden correctamente en el disco duro sin pérdida de información.