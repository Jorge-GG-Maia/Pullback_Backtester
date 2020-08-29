Este é um trading system automatizado em Python voltado a detectar variações bruscas de certos ativos da Bolsa de Valores,
o trading system se baseia em executar umma operação na ponta contrária a de qualquer variação que se distancie demais da 
média de retornos do ativo, com timeframe de D+1.

Como utilizar:
    
    Basta inserir na pasta DataBase os dados históricos das ações desejadas, em arquivo CSV contendo data no formato "DD/MM/YYYY" e a cotação (usando ponto 
como separação de decimais) do período correspondente (recomenda-se no mínimo 1 ano de histórico), e nomeando o arquivo com o código da ação desejada, (EX.: PETR4.csv). Este trading system funciona em qualquer timeframe (diário, semanal ou mensal). Quanto mais ações sejam adicionadas, maior a frequência de operações.

    As datas e cotações correspondentes devem estar dispostas em ordem crescente. Partindo da data mais antiga até a mais recente, sendo de preferencia
a data mais recente a do fechamento do período atual, no qual o programa projetará as ordens para o período seguinte, caso sejam detectadas. Este script
conta com ferramentas de backtest apresentando os retornos acumulados naquele determinado ativo durante o período adicionado, e apresenta para fins de 
referência o retorno do Buy and Hold para o mesmo ativo durante o período


Como operar:
    
    Ao adicionar os históricos de cotações nos formatos adequados e executar o script, o sistema irá calcular baseado na média dos retornos, e do desvio
padrão dos retornos de cada um dos ativos, se há operações disponíveis, apresentando, caso haja no formato:
    
    *CODIGO DA AÇÃO ( Acumulado: *Retornos acumulados, B&H: *Retornos do Buy and Hold no período ): Posição percebida (1: Compra, -1: Venda)**

Caso não haja nenhuma posição tenha sido identificada para o período, o sistema retornará "Nenhuma operação detectada."


Recomenda-se o uso deste script em conjunto com outros scripts de web scraping para manter os dados históricos sempre atualizados


***** ESTE SISTEMA DEVE SER USADO PARA FINS DE ESTUDO ACERCA DO COMPORTAMENTO DOS ATIVOS NO MERCADO FINANCEIRO DE CAPITAIS, OU COMO FERRAMENTA AUXILIAR PARA BACKTEST E CONSTRUÇÃO DE ESTRATÉGIAS QUANTITATIVAS PRÓPRIAS PARA QUEM OS USE, NÃO TENDO PORTANTO QUALQUER FINALIDADE COMO DE RECOMENDAÇÃO DE INVESTIMENTO.

***** A CONSTRUÇÃO E PUBLICAÇÃO DESTE SISTEMA NÃO POSSUI FINS LUCRATIVOS.


 

    































