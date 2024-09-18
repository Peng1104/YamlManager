# FileController
Biblioteca que controla e cria arquivos JSON e YAML

## Funções:

1. __DictToJSONFile:__
	- Função:
    	- Converte um __dicionario__ em um __JSONFile__
  	- Argumentos:
    	- JsonPath - Uma __String__ ou um __JSONFile__, localização do __JSONFile__
    	- dicionario - Os dados que o __JSONFile__ deve ter
  	- Argumentos Opcionais:
    	- save - Se o __JSONFile__ deve ser salvado, (criado ou alterado) assim que os dados forem iguais ao __dicionario__
  	- Retorna:
    	- Um __JSONFile__ localizado no JsonPath
2. __JSONFileToDict:__
	- Função:
    	- Converte os dados de um __JSONFile__ em um __dicionario__
  	- Argumentos:
    	- JsonPath - Uma __String__ ou um __JSONFile__, localização do __JSONFile__
  	- Retorna:
    	- Um __dicionario__ que contem todos os dados do __JSONFile__
3. __JSONFileToYamlFile:__
	- Função:
    	- Converte os dados de um __JSONFile__ em um __YamlFile__
  	- Argumentos:
    	- JsonPath - Uma __String__ ou um __JSONFile__, localização do __JSONFile__
    	- YamlPath - Uma __String__ ou um __YamlFile__, localização do __YamlFile__
  	- Argumentos Opcionais:
    	- save - Se o __YamlFile__ deve ser salvado, (criado ou alterado) assim que os dados forem iguais ao __JSONFile__
  	- Retorna:
    	- Um __YamlFile__ localizado no YamlPath
4. __DictToYamlFile:__
	- Função:
    	- Converte um __dicionario__ em um __YamlFile__
  	- Argumentos:
    	- YamlPath - Uma __String__ ou um __YamlFile__, localização do __YamlFile__
    	- dicionario - Os dados que o __YamlFile__ deve ter
  	- Argumentos Opcionais:
    	- save - Se o __YamlFile__ deve ser salvado, (criado ou alterado) assim que os dados forem iguais ao __dicionario__
  	- Retorna:
    	- Um __YamlFile__ localizado no YamlPath
5. __YamlFileToDict:__
	- Função:
    	- Converte os dados de um __YamlFile__ em um __dicionario__
  	- Argumentos:
    	- YamlPath - Uma __String__ ou um __YamlFile__, localização do __YamlFile__
  	- Retorna:
    	- Um __dicionario__ que contem todos os dados do __YamlFile__
6. __YamlFileToJSONFile:__
	- Função:
    	- Converte os dados de um __YamlFile__ em um __JSONFile__
  	- Argumentos:
		- YamlPath - Uma __String__ ou um __YamlFile__, localização do __YamlFile__
    	- JsonPath - Uma __String__ ou um __JSONFile__, localização do __JSONFile__
  	- Argumentos Opcionais:
    	- save - Se o __JSONFile__ deve ser salvado, (criado ou alterado) assim que os dados forem iguais ao __YamlFile__
  	- Retorna:
    	- Um __JSONFile__ localizado no JsonPath

## Classes / Objetos

* __YamlFile__
* __JSONFile__
* __FileController__
