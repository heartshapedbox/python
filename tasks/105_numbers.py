# Создайте новый файл с именем Numbers.txt. Добавьте в него пять чисел, которые хранятся в одной строке и разделяются только запятыми. После запуска программы найдите папку, в которой располагается ваша программа; убедитесь в том, что файл был создан. В системе Windows для просмотра содержимого нового текстового файла проще всего воспользоваться «Блокнотом».

import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

file = open("Numbers.txt", "w")
file.write('1, 2, 3, 4, 5')
file.close()
