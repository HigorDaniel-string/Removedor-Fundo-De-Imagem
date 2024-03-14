from rembg import remove
from PIL import Image
print("Retirando fundo da imagem...")
input_path = 'cl.jpg'
output_path = 'cl_sem_fundo.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
print("Finalizado com sucesso!")
