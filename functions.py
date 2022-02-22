class ClassificadorObesidade:

    def arvore_J48(self, dados):
        """
        Método para verificar o nível de obesidade usando árvore de decisão (J48).

        Espera-se receber um array:
        arvore_J48(array dados)

        Retorno: string
        """

        i = dados

        if i[3] <= 99.530971:
            if i[3] <= 60:
                if i[2] <= 1.66:
                    if i[3] <= 46.655622:
                        if i[2] <= 1.513202:
                            obesidade = "Normal_Weight"
                        else:
                            if i[3] <= 44.918255:
                                obesidade = "Insufficient_Weight"
                            else:
                                if i[2] <= 1.58:
                                    obesidade = "Normal_Weight"
                                else:
                                    obesidade = "Insufficient_Weight"
                    else:
                        if i[2] <= 1.53777:
                            if i[5] == "Sim":
                                if i[11] == "Sim":
                                    obesidade = "Overweight_Level_I"
                                else:
                                    if i[3] <= 56.307019:
                                        obesidade = "Normal_Weight"
                                    else:
                                        obesidade = "Overweight_Level_I"
                            else:
                                obesidade = "Normal_Weight"
                        else:
                            if i[3] <= 50.664459:
                                if i[2] <= 1.605404:
                                    obesidade = "Normal_Weight"
                                else:
                                    obesidade = "Insufficient_Weight"
                            else:
                                obesidade = "Normal_Weight"
                else:
                    if i[3] <= 54.997374:
                        obesidade = "Insufficient_Weight"
                    else:
                        if i[2] <= 1.750384:
                            obesidade = "Normal_Weight"
                        else:
                            if i[12] <= 1.330519:
                                obesidade = "Normal_Weight"
                            else:
                                obesidade = "Insufficient_Weight"
            else:
                if i[3] <= 76:
                    if i[2] <= 1.5891:
                        if i[5] == "Sim":
                            if i[3] <= 70:
                                obesidade = "Overweight_Level_I"
                            else:
                                obesidade = "Obesity_Type_I"
                        else:
                            obesidade = "Overweight_Level_II"
                    else:
                        if i[2] <= 1.734832:
                            if i[3] <= 72:
                                if i[2] <= 1.648143:
                                    if i[3] <= 64.4:
                                        obesidade = "Normal_Weight"
                                    else:
                                        obesidade = "Overweight_Level_I"
                                else:
                                    if float(i[1]) <= 27.474245:
                                        obesidade = "Normal_Weight"
                                    else:
                                        if i[6] <= 2.805533:
                                            obesidade = "Overweight_Level_I"
                                        else:
                                            obesidade = "Normal_Weight"
                            else:
                                if float(i[1]) <= 20.438478:
                                    if float(i[1]) <= 18.48207:
                                        obesidade = "Overweight_Level_I"
                                    else:
                                        obesidade = "Overweight_Level_II"
                                else:
                                    obesidade = "Overweight_Level_I"
                        else:
                            if i[2] <= 1.85:
                                if i[3] <= 75.306702:
                                    obesidade = "Normal_Weight"
                                else:
                                    if float(i[1]) <= 28.493397:
                                        obesidade = "Normal_Weight"
                                    else:
                                        obesidade = "Overweight_Level_I"
                            else:
                                if i[3] <= 65.423942:
                                    obesidade = "Insufficient_Weight"
                                else:
                                    obesidade = "Normal_Weight"
                else:
                    if i[2] <= 1.729177:
                        if i[2] <= 1.64639:
                            if i[3] <= 92:
                                obesidade = "Obesity_Type_I"
                            else:
                                obesidade = "Obesity_Type_II"
                        else:
                            if i[3] <= 85.316199:
                                if i[2] <= 1.665199:
                                    if i[3] <= 81.384224:
                                        obesidade = "Overweight_Level_II"
                                    else:
                                        obesidade = "Obesity_Type_I"
                                else:
                                    obesidade = "Overweight_Level_II"
                            else:
                                if i[3] <= 88.675503:
                                    if i[2] <= 1.694997:
                                        obesidade = "Obesity_Type_I"
                                    else:
                                        obesidade = "Overweight_Level_II"
                                else:
                                    obesidade = "Obesity_Type_I"
                    else:
                        if i[3] <= 91:
                            if i[2] <= 1.799779:
                                if i[3] <= 83.26312:
                                    if float(i[1]) <= 30.163408:
                                        obesidade = "Overweight_Level_I"
                                    else:
                                        obesidade = "Overweight_Level_II"
                                else:
                                    if float(i[7]) <= 3.054899:
                                        obesidade = "Overweight_Level_II"
                                    else:
                                        obesidade = "Overweight_Level_I"
                            else:
                                if i[3] <= 84.49798:
                                    obesidade = "Normal_Weight"
                                else:
                                    if i[8] == "Não":
                                        obesidade = "Overweight_Level_I"
                                    if i[8] == "Às vezes":
                                        obesidade = "Overweight_Level_I"
                                    if i[8] == "Frequentemente":
                                        obesidade = "Normal_Weight"
                                    if i[8] == "Sempre":
                                        obesidade = "Overweight_Level_I"
                        else:
                            if i[2] <= 1.794827:
                                obesidade = "Obesity_Type_I"
                            else:
                                obesidade = "Overweight_Lavel_II"
        else:
            if i[0] == "Feminino":
                obesidade = "Obesity_Type_III"
            else:
                if float(i[1]) <= 22.524036:
                    if i[6] <= 2.571274:
                        obesidade = "Obesity_Type_I"
                    else:
                        if i[12] <= 0.967627:
                            obesidade = "Obesity_Type_II"
                        else:
                            obesidade = "Obesity_Type_I"
                else:
                    if i[3] <= 109.599453:
                        if i[2] <= 1.750384:
                            if i[10] <= 1.768111:
                                obesidade = "Obesity_Type_II"
                            else:
                                obesidade = "Obesity_Type_I"
                        else:
                            if i[2] <= 1.86516:
                                obesidade = "Obesity_Type_I"
                            else:
                                obesidade = "Overweight_Level_II"
                    else:
                        obesidade = "Obesity_Type_II"
        
        return obesidade


    def renomear_respostas(self, dados):
        """
        Método para percorrer o vetor de respostas e renomear. Isso é necessário
        para que a nomenclatura esteja de acordo com os nomes usados Não J48.

        Espera-se receber um array:
        renomear_respostas(array dados)

        Retorno: array
        """

        for i in  range(len(dados)):
            
            x = dados[i]
                
            if x == 'Entre 1 e 2':
                dados[i] = 1
                
            if x == '3 refeições':
                dados[i] = 2
                
            if x == 'Mais que 3':
                dados[i] = 3
                
            if x == 'Menos de 1L':
                dados[i] = 1
                
            if x == 'Entre 1L e 2L':
                dados[i] = 2
                
            if x == 'Mais de 2L':
                dados[i] = 3
                
            if x == 'Não bebo':
                dados[i] = 'Não'
                
            if x == 'Não faço':
                dados[i] = 0
                
            if x == '1 ou 2 dias':
                dados[i] = 1
                
            if x == '3 ou 4 dias':
                dados[i] = 2
                
            if x == '5 dias ou mais':
                dados[i] = 3
                
            if x == 'De 0 a 2 horas':
                dados[i] = 0
                
            if x == 'De 3 a 5 horas':
                dados[i] = 1
                
            if x == 'Mais de 5 horas':
                dados[i] = 2

        return dados
    
    def classificar_obesidade(self, dados):
        """
        Método para receber os dados de entrada do usuário e retornar uma resposta
        relacionado ao seu nível de obesidade.

        Espera-se receber um array:
        classificar_obesidade(array dados)

        Retorno: string
        """
        criticidade = 0

        dados_novo = self.renomear_respostas(dados)
        obesidade = self.arvore_J48(dados_novo)

        if obesidade == 'Insufficient_Weight':
            obesidade = 'Peso Insuficiente'
            criticidade = 1
        if obesidade == 'Normal_Weight':
            obesidade = 'Peso Normal'
        if obesidade == 'Overweight_Level_I':
            obesidade = 'Sobrepeso Nível I'
            criticidade = 1
        if obesidade == 'Overweight_Level_II':
            obesidade = 'Sobrepeso Nível II'
            criticidade = 2
        if obesidade == 'Obesity_Type_I':
            obesidade = 'Obesidade Tipo I'
            criticidade = 3
        if obesidade == 'Obesity_Type_II':
            obesidade = 'Obesidade Tipo II'
            criticidade = 4
        if obesidade == 'Obesity_Type_III':
            obesidade = 'Obesidade Tipo III'
            criticidade = 5
        
        return obesidade, criticidade               
            
