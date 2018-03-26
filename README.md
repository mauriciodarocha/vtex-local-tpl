# Vtex Local Templating

Os controles da Vtex renderizam simples HTMLs nas páginas e carregam alguns javascripts para o funcionamento de algumas funções da plataforma. 

Mas para a montagem de um template é necessário criar e subir um template, salvar o arquivo, criar um folder + layout, e então, poder criar o CSS e Javascript da página.

Este plugin para o Sublime Text 3 serve para evitar tudo que foi descrito acima, facilitando a montagem de páginas, landing pages e hotsites.

Você pode criar a formatação de uma página se você carregar manualmente todos os scripts e css necessários.

## O que este plugin não faz
Não espere que o plugin carregue ou crie magicamente o HTML dos controles da plataforma ou carregue automaticamente os javascripts utilizados na Vtex.

Você precisa copiar o HTML, e utilizá-lo e depois descartá-lo no documento final.


## Instalação
Baixe os arquivos em um zip ou pelo git, e copie o folder VtexLocalTpl para o folder "Packages/" do Sublime Text 3.

## Uso
Monte o HTML com os controles (tags) da Vtex normalmente, mas comente-os e coloque HTMLs (mockups) entre **<!-- delete -->** e **<!-- delete:end -->**. Assim é possível a remoção dos mockups ou html temporário rapidamente.


### Clean HTML
O comando "Clean HTML" limpa tudo que fica entre **<!-- delete -->** e **<!-- delete:end -->**. Não intercale estes comentários. O plugin irá buscar exatamente por um **<!-- delete -->** até encontrar o próximo **<!-- delete:end -->**.

Exemplo de html com mockups para a montagem da página:


    <div class="main">
        <div class="title">
            Olá mundo!
            <!-- <vtex.cmc:contentPlaceHolder id="HTML da área 1" /> -->
            <!-- delete -->
            <div class='temp'>lala</div>
            <!-- delete:end -->
        </div>
    </div>

Depois de aplicado:

    <div class="main">
        <div class="title">
             Olá mundo!
            <!-- <vtex.cmc:contentPlaceHolder id="HTML da área 1" /> -->
        </div>
    </div>


### Uncomment Vtex Tags
O comando "Uncomment Vtex Tags" retira os comentários dos elementos da vtex.

    <!-- <vtex.cmc:contentPlaceHolder id="algum conteúdo" /> -->
    <!-- <vtex:template id=" header" /> -->

Depois de aplicado:

    <vtex.cmc:contentPlaceHolder id="algum conteúdo" />
    <vtex:template id=" header" />

### Swap URL
O comando "Swap URL" troca os endereços (URIs) para as URIs finais que serão utilizadas no ambiente Vtex.

    <link href="/url-do-meu-arquivo-local/meu-arquivo.css" vtex="/arquivos/meu-arquivo.css" />
    <script vtex="/arquivos/meu-arquivo.js" src="/url-do-meu-arquivo-local/meu-arquivo.jss" ></script>

Depois de aplicado:

    <link href="/arquivos/meu-arquivo.css" />
    <script src="/arquivos/meu-arquivo.js" ></script>

### Full Clean up
Este comando executa os 3 comandos acima de cima para baixo, **Clean HTML**, **Uncomment Vtex Tags** e, por fim, **Swap URL**.

### Exemplo

Exemplo de template local:

        <!DOCTYPE html>
        <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:vtex="http://www.vtex.com.br/2009/vtex-common"
            xmlns:vtex.cmc="http://www.vtex.com.br/2009/vtex-commerce">
        <head>
            <meta charset="UTF-8">
            <title>Minha página</title>

            <!-- delete -->
            <!-- um monte de scripts e css que são necessárias temporáriamente -->
            <!-- delete:end -->

            <link href="/url-do-meu-arquivo-local/meu-arquivo.css" vtex="/arquivos/meu-arquivo.css" />
            <script vtex="/arquivos/meu-arquivo.js" src="/url-do-meu-arquivo-local/meu-arquivo.jss" ></script>

        </head>
        <body>
            <!-- subtemplate header -->
            <vtex:template id="header" />
            <!-- subtemplate header:end -->
            <!-- delete -->
            <!-- ESTE HTML SERÁ COPIADO PARA O SUBTEMPLATE HEADER -->
            <header>
                <div class="logo"><img src="/arquivos/logo.png" /></div>
                <nav><ul><li>Home</li><li>Dept 1</li></ul></nav>
            </header>
            <!-- delete:end -->

            <div class="Main">
                <section class="section-1"></section>
                <section class="section-2"></section>
                <section class="section-N"></section>
            </div>

            <!-- subtemplate footer -->
            <vtex:template id="footer" />
            <!-- subtemplate footer:end -->
            <!-- delete -->
            <!-- ESTE HTML SERÁ COPIADO PARA O SUBTEMPLATE FOOTER -->
            <footer>
                Copyright, etc, etc...
            </footer>
            <!-- delete:end -->
        </body>
        </html>

Exemplo depois de limpo:

        <!DOCTYPE html>
        <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:vtex="http://www.vtex.com.br/2009/vtex-common"
            xmlns:vtex.cmc="http://www.vtex.com.br/2009/vtex-commerce">
        <head>
            <meta charset="UTF-8">
            <title>Minha página</title>

            <link href="/arquivos/meu-arquivo.css" />
            <script src="/arquivos/meu-arquivo.js" ></script>
        </head>
        <body>
            <!-- subtemplate header -->
            <vtex:template id="header" />
            <!-- subtemplate header:end -->

            <div class="Main">
                <section class="section-1"></section>
                <section class="section-2"></section>
                <section class="section-N"></section>
            </div>

            <!-- subtemplate footer -->
            <vtex:template id="footer" />
            <!-- subtemplate footer:end -->

        </body>
        </html>

