from django.db import models

class Task(models.Model): #Define a classe Task que herda da classe Model 
  
  title = models.CharField(max_length = 50) # Define um campo de caracteres (string) que possui no máximo 50 caracteres
  
  description = models.TextField() # Define um campo de texto para armazenar uma descrição mais longa
  
  due_date = models.DateField() # Define um campo de data para armazenar a data de vencimento da tarefa
  
  done = models.BooleanField() # Define um campo booleano para indicar se a tarefa foi concluída (True) ou não (False)
