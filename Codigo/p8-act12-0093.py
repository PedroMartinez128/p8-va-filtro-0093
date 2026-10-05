import cv2
print("-----Pedro Martinez 0093-----")
# Cargar la imagen
imagen = cv2.imread("C:\IA_Gpo3-H\VA_0093\p8-act12-0093\Imagenes/Lechuza-0093.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(
    imagen,
    5
)

# Mostrar imágenes
cv2.imshow("Imagen original lechuza 0093", imagen)
cv2.imshow("Imagen con filtro de mediana lechuza 0093", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "../resultados/Lechuza-0093.jpg",
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("../resultados/paisaje_mediana.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("-----Pedro Martinez 0093-----")