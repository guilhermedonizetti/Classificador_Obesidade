<h1 align="center">Classificador_Obesidade</h1>
<p align="center">Um programa com interface e árvore de decisão para classificação de obesidade em uma pessoa :computer:</p>

<b>Objetivo: </b>um porgrama em que o usuário possa informar resposta de coisas do seu dia-a-dia e com base nisso obter uma resposta sobre o nível de obesidade (se tiver).

<b>Desenvolvimento:</b> Foi usado um <i>dataset</i> de 2.111 registros com 17 atributos. Desse total, 80% (1.689 registros) foram usados para treino e 20 % (422) usado para teste. O algoritmo usado foi o J48, que é excelente para examinar dados de forma categórica, através do Weka. A árvore de decisão criada acertou 93,4% dos testes.



<b>Ferramentas:</b> foi usado o framework <b>Streamlit</b> (Python) para criar a interface do programa, <b>Weka</b> para fazer a mineração de dados e encontrar padrões para criar a árvore de decisão, e foi porgramado em <b>Python</b>.

<img align="center" src="https://github.com/guilhermedonizetti/Classificador_Obesidade/blob/master/images/imagem1.png" >

Os 17 atributos que são levados em consideração são:<br>
<ul>
  <li>Consumo de alimentos calóricos</li>
  <li>Consumo de vegetais</li>
  <li>Número de refeições principais</li>
  <li>Comida entre refeições</li>
  <li>Quantidade de água por dia</li>
  <li>Consumo de bebida alcoólica</li>
  <li>Fumante</li>
  <li>Hábito de monitorar o consumo de calorias por dia</li>
  <li>Histórico de obesidade na família</li>
  <li>Atividades físicas</li>
  <li>Tempo em dispositivos digitais</li>
  <li>Meio de transporte usado</li>
  <li>Gênero</li>
  <li>Idade</li>
  <li>Altura</li>
  <li>Peso</li>
</ul>

<b>Fontes:</b> o <i>dataset</i> usado pode ser encontrado <i><a href="https://archive.ics.uci.edu/ml/datasets/Estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition+">no repositório de arquivos .arff do UCI Machine Learning Repository</a></i>. A pesquisa que desenvolveu esse dataset pode ser encontrada na plataforma <i><a href="https://www.sciencedirect.com/science/article/pii/S2352340919306985?via%3Dihub">ScienceDirect</a></i>.

<br>

<p align="center">
<b>Python, Weka, Streamlit, DataMining</b><br>Guilherme Donizetti - 2022.
</p>
