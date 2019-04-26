"""
Created on Sat Apr 20 10:37:37 2019

@author: Peng1104
"""

#Versão do FileController
__version__ = "1.0"

#Coverte um dicionario em um JSONFile
def DictToJSONFile(JsonPath, dicionario, save=False):
	if ((type(JsonPath) == str and len(JsonPath) > 0) or type(JsonPath) == JSONFile) and type(dicionario) == dict and type(save) == bool:
		File = None

		if type(JsonPath) == str:
			File = JSONFile(JsonPath)
		else:
			File = JsonPath

		File.data = dicionario

		if save:
			File.save()

		return File
	else:
		raise TypeError("JsonPath precisa ser uma String com pelo menos 1 caractere ou um JSONFile e/ou dicionario tem que ser um Dicionario e/ou save tem que ser um Booleano!")

#Converte um arquivo JSON em um dicionario
def JSONFileToDict(JsonPath):
	if (type(JsonPath) == str and len(JsonPath) > 0) or type(JsonPath) == JSONFile:
		if type(JsonPath) == str:
			return JSONFile(JsonPath).data
		else:
			return JsonPath.data
	else:
		raise TypeError("JsonPath precisa ser uma String com pelo menos 1 caractere ou um JSONFile!")

#Converte um arquivo JSON em um arquivo YAML (retorna um novo YamlFile)
def JSONFileToYamlFile(JsonPath, YamlPath, save=False):
	if ((type(YamlPath) == str and len(YamlPath) > 0) or type(YamlPath) == YamlFile) and type(save) == bool:
		File = None

		if type(YamlPath) == str:
			File = YamlFile(YamlPath)
		else:
			File = YamlPath

		File.data = JsonFileToDict(JsonPath)

		if save:
			File.save()

		return File
	else:
		raise TypeError("YamlPath precisa ser uma String com pelo menos 1 caractere ou um YamlFile e/ou save tem que ser um Booleano!")

#Coverte um dicionario em um YamlFile
def DictToYamlFile(YamlPath, dicionario, save=False):
	if ((type(YamlPath) == str and len(YamlPath) > 0) or type(YamlPath) == YamlFile) and type(dicionario) == dict and type(save) == bool:
		File = None

		if type(YamlFile) == str:
			File = YamlFile(YamlPath)
		else:
			File = YamlPath

		if save:
			File.save()

		File.data = dicionario

		return File
	else:
		raise TypeError("YamlPath precisa ser uma String com pelo menos 1 caractere ou um YamlFile e/ou dicionario tem que ser um Dicionario e/ou save tem que ser um Booleano!")

#Converte um arquivo YAML para um dicionario
def YamlFileToDict(YamlPath):
	if (type(YamlPath) == str and len(YamlPath) > 0) or type(YamlPath) == YamlFile:
		if type(YamlPath) == str:
			return YamlFile(YamlPath).data
		else:
			return YamlPath.data
	else:
		raise TypeError("YamlPath precisa ser uma String com pelo menos 1 caractere ou um YamlFile!")

#Converte um arquivo YAML para um arquivo JSON (retorna um novo JSONFile)
def YamlFileToJSONFile(YamlPath, JsonPath, save=False):
	if ((type(JsonPath) == str and len(JsonPath) > 0) or type(JsonPath) == JSONFile) and type(save) == bool:
		File = None

		if type(JsonPath) == str:
			File = JSONFile(JsonPath)
		else:
			File = JsonPath

		File.data = YamlFileToDict(YamlPath)

		if save:
			File.save()

		return File
	else:
		raise TypeError("JsonPath precisa ser uma String com pelo menos 1 caractere ou um JSONFile e/ou save tem que ser um Booleano!")

#Classe para criar e processar um YamlFile
class YamlFile(FileController):
	import yaml
	import re

	#Versão da classe YamlFile
	__version__ = "1.0"

	def __init__(self, FilePath):
		FileController.__init__(self, FilePath)

		#Verefica a versâo do PyYAML se é igual ou superior a 5.1
		if re.search("^\d+(.\d+)?$", yaml.__version__) and float(yaml.__version__) < 5.1:
			raise ImportError("ERRO! Não Foi possível achar o modulo PyYAML 5.1 ou superior")
			

	#Carrega os dados do arquivo
	def reload(self):
		with open(self.FilePath, 'r', encoding="utf-8") as file:
			self.data = yaml.load(file.read(), Loader=yaml.FullLoader)

	#Salva os dados para o arquivo
	def save(self):
		with open(self.FilePath, 'w', encoding="utf-8") as file:
			file.write(yaml.dump(self.data, allow_unicode=True, default_flow_style=False, sort_keys=False))

#Classe para criar e processar um JSONFile
class JSONFile(FileController):
	import json

	#Versão da classe JSONFile
	__version__ = "1.0"

	def __init__(self, FilePath):
		FileController.__init__(self, FilePath)

	#Carrega os dados do arquivo
	def reload(self):
		with open(self.FilePath, 'r', encoding="utf-8") as file:
			self.data = json.load(file)

	#Salva os dados para o arquivo
	def save(self):
		with open(self.FilePath, 'w', encoding="utf-8") as file:
			file.write(json.dumps(self.data, ensure_ascii=False, indent="\t"))

#Classe pai para JSONFile e YamlFile
class FileController:
	import os
	import re
	from pathlib import Path

	#Versão da classe FileController
	__version__ = "1.0"

	#FilePath = Localização do arquivo

	def __init__(self, FilePath):
		#Verefica se FilePath é uma string
		elif type(FilePath) != str:
			raise TypeError("ERRO! FilePath deve ser uma String")
		#Verefica se existe o caminho especificado pelo FilePath
		elif Path(FilePath).exists():
			#Verefica se o caminho leva a um arquivo
			if Path(FilePath).is_file():
				#Verefica as permissões de Leitura e Escrita do arquivo
				if not os.access(FilePath, os.R_OK):
					raise PermissionError("ERRO! Não foi possível ler o arquivo: " + FilePath)
				elif not os.access(FilePath, os.W_OK):
					raise PermissionError("ERRO! Não é possivel editar o arquivo: " + FilePath)
				else:
					#Carrega as configurações inicias
					self.FilePath = FilePath
					self.data = {}
					self.reload()
			else:
				raise IsADirectoryError("ERRO! " + FilePath + " é um diretório")
		else:
			#Cria as configurações inicias
			self.FilePath = FilePath
			self.data = {}

	#Cria uma nova arvore de configuração - USO INTERNO
	def createNew(self, tree, value):
		if type(tree) == list and len(tree) > 0 and (type(value) == str or type(value) == list or type(value) == dict):
			dic = {}

			if len(tree) == 1:
				dic[tree[0]] = value
			else:
				x = len(tree) - 2
				new = {tree[-1] : value}

				while x > 0:
					new = {tree[x] : new}
					x = x - 1
				dic[tree[0]] = new

			return dic
		else:
			raise TypeError("Tipo de tree e/ou value incorreto!")

	#Processa o set - USO INTERNO
	def process_set(self, tree, dic, value):
		if type(tree) == list and len(tree) > 0 and type(dic) == dict and (type(value) == str or type(value) == list or type(value) == dict or value == None):
			#Verefica se a existe a chave na arvore de configuração
			if tree[0] in dic:
				#Verefica se é chave final
				if len(tree) == 1:
					#Verefica se key deve ser apagada
					if value == None:
						del dic[tree[0]]
					#Altera o valor
					else:
						dic[tree[0]] = value
				#Verefica se continuação é uma arvore de configuração, se não cancela a operação
				elif type(dic[tree[0]]) != dict:
					return dic
				#Entra na proxima arvore de configuração interna
				else:
					dic[tree[0]] = self.process_set(tree[1:], dic[tree[0]], value)
					#Verefica se tudo dentro da arvore foi apagado, apagando a arvore em seguinda
					if len(dic[tree[0]]) == 0:
						del dic[tree[0]]
			#Adicionar valor se o mesmo não for nulo
			elif value != None:
				if len(tree) == 1:
					dic[tree[0]] = value
				else:
					dic[tree[0]] = self.createNew(tree[1:], value)
			return dic
		else:
			raise TypeError("Tipo de tree e/ou value e/ou dic incorreto!")

	#Seta/Altera valores na configuração
	def set(self, path, value):
		if type(path) == str and len(path) > 0:
			tree = path.split(".")

			#Se o value for nulo significa apagar um item na data
			if value == None:
				self.data = self.process_set(tree, self.data, None)
			#Se o value for uma lista ou dicionario entra como tal
			if type(value) == list or type(value) == dict:
				self.data = self.process_set(tree, self.data, value)
				#Garantir que tudo seja "string"
				self.save()
				self.load()
			else:
				self.data = self.process_set(tree, self.data, "{}".format(value))
		else:
			raise TypeError("Path precisa ser uma String com pelo menos 1 caractere")

	#Processa o get - USO INTERNO
	def process_get(self, tree, dic, default_value):
		if type(tree) == list and len(tree) > 0 and type(dic) == dict and (type(default_value) == str or type(default_value) == list or type(default_value) == dict or default_value == None):
			#Verefica se a existe a chave na arvore de configuração
			if tree[0] in dic:
				#Verefica se é a chave final e retorna a string 
				if len(tree) == 1:
					return dic[tree[0]]
				#Verefica se continuação é uma arvore de configuração, se não cancela a operação
				elif type(dic[tree[0]]) != dict:
					return None
				#Entra na proxima arvore de configuração interna
				else:
					return self.process_get(tree[1:], dic[tree[0]], default_value)
			#Adiciona nos dados o valor default se o mesmo existir
			elif default_value != None:
				self.process_set(tree, dic, default_value)
				return default_value
		else:
			raise TypeError("Tipo de tree e/ou default_value e/ou dic incorreto!")

	#Pega uma String dentro dos dados
	def getString(self, path, default_value=None):
		if type(path) == str and len(path) > 0 and (type(default_value) == str or default_value == None):
			tree = path.split(".")
			return "{}".format(self.process_get(tree, self.data, default_value))
		else:
			raise TypeError("Path precisa ser uma String com pelo menos 1 caractere e/ou default_value tem que ser uma String!")

	#Pega um Float dentro dos dados
	def getFloat(self, path, default_value=None):
		if type(path) == str and len(path) > 0 and (type(default_value) == float or type(default_value) == int or default_value == None):
			string = ""

			#Pega a sting dentro dos dados
			if default_value != None:
				string = self.getString(path, "{}".format(default_value))
			else:
				string = self.getString(path, None)

			#Verefica se a string é um float
			if re.search("^-?\d+(.\d+)?$", string):
				return float(string)
			#Seta na localização o valor default se o mesmo existir
			elif default_value != None:
				self._set_(path, default_value)
				return float(default_value)
		else:
			raise TypeError("Path precisa ser uma String com pelo menos 1 caractere e/ou default_value tem que ser um Numero!")

	#Pega um Inteirno dentro dos dados
	def getInt(self, path, default_value=None):
		if type(path) == str and len(path) > 0 and (type(default_value) == int or default_value == None):
			string = ""

			#Pega a sting dentro dos dados
			if default_value != None:
				string = self.getString(path, "{}".format(default_value))
			else:
				string = self.getString(path, None)

			#Verefica se a string é um inteiro
			if re.search("^-?\d+$", string):
				return float(string)
			#Seta na localização o valor default se o mesmo existir
			elif default_value != None:
				self._set_(path, default_value)
				return default_value
		else:
			raise TypeError("Path precisa ser uma String com pelo menos 1 caractere e/ou default_value tem que ser um Inteiro!")

	#Pega um Booleano dentro dos dados
	def getBoolean(self, path, default_value=None):
		if type(path) == str and len(path) > 0 and (type(default_value) == bool or default_value == None):
			string = ""

			#Pega a sting dentro dos dados
			if default_value != None:
				string = self.getString(path, "{}".format(default_value))
			else:
				string = self.getString(path, None)

			return string.lower() == "true"
		else:
			raise TypeError("Path precisa ser uma String com pelo menos 1 caractere e/ou default_value tem que ser um Booleano!")

	#Pega uma Lista de Strings dentro dos dados
	def getStringList(self, path, default_value=None):
		if type(path) == str and len(path) > 0 and (type(default_value) == list or default_value == None):
			tree = path.split(".")

			lista = self.process_get(tree, self.data, default_value)

			if type(lista) == list:
				result = []

				for x in lista:
					result.append("{}".format(x))

				return result
			elif default_value != None:
				self._set_(path, default_value)
				return default_value
		else:
			raise TypeError("Path precisa ser uma String com pelo menos 1 caractere e/ou default_value tem que ser uma Lista!")

	#Pega uma Lista de Floats dentro dos dados
	def getFloatList(self, path, default_value=None):
		if type(path) == str and len(path) > 0 and (type(default_value) == list or default_value == None):
			tree = path.split(".")

			result = self.process_get(tree, self.data, default_value)

			if type(result) == list:
				lista = []

				#Transformando Strings em Floats
				for string in result:
					if re.search("^-?\d+(.\d+)?$", string):
						lista.append(float(string))
					else:
						lista.append(0.0)
				return lista

			elif default_value != None:
				self._set_(path, default_value)
				return default_value
		else:
			raise TypeError("Path precisa ser uma String com pelo menos 1 caractere e/ou default_value tem que ser uma Lista!")

	#Pega uma Lista de Inteiros dentro dos dados
	def getIntList(self, path, default_value=None):
		if type(path) == str and len(path) > 0 and (type(default_value) == list or default_value == None):
			tree = path.split(".")

			result = self.process_get(tree, self.data, default_value)

			if type(result) == list:
				lista = []

				#Transformando Strings em Inteiros
				for string in result:
					if re.search("^-?\d+$", string):
						lista.append(int(string))
					else:
						lista.append(0)
				return lista

			elif default_value != None:
				self._set_(path, default_value)
				return default_value
		else:
			raise TypeError("Path precisa ser uma String com pelo menos 1 caractere e/ou default_value tem que ser uma Lista!")

	#Pega uma Lista de Booleanos dentro dos dados
	def getBooleanList(self, path, default_value=None):
		if type(path) == str and len(path) > 0 and (type(default_value) == list or default_value == None):
			tree = path.split(".")

			result = self.process_get(tree, self.data, default_value)

			if type(result) == list:
				lista = []

				#Transformando Strings em Booleanos
				for string in result:
					lista.append(string.lower() == "true")
				return lista

			elif default_value != None:
				self._set_(path, default_value)
				return default_value
		else:
			raise TypeError("Path precisa ser uma String com pelo menos 1 caractere e/ou default_value tem que ser uma Lista!")

	#Pega um Dicionario dentro dos dados
	def getDict(self, path, default_value=None):
		if type(path) == str and len(path) > 0 and (type(default_value) == dict or default_value == None):
			tree = path.split(".")

			result = self.process_get(tree, self.data, default_value)

			if type(result) == dict:
				return result
			elif default_value != None:
				self._set_(path, default_value)
				return default_value
		else:
			raise TypeError("Path precisa ser uma String com pelo menos 1 caractere e/ou default_value tem que ser um Dicionario!")