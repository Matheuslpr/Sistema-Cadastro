Este projeto foi desenvolvido como um trabalho da faculdade, no curso de Análise e Desenvolvimento de Sistemas da PUC-PR. O objetivo principal foi construir um sistema simples de cadastro acadêmico, utilizando a linguagem Python e armazenando os dados em arquivos JSON.

O sistema permite gerenciar cinco tipos de entidades principais: estudantes, professores, disciplinas, turmas e matrículas. Para cada uma dessas entidades é possível criar novos registros, listar os dados existentes, atualizar informações e excluir registros quando necessário.

Durante o desenvolvimento, foram utilizadas várias estruturas da linguagem Python, como listas, dicionários e tratamento de exceções com try/except, além de boas práticas de organização e reutilização de código por meio de funções. As informações são salvas localmente em arquivos .json, o que permite que os dados persistam entre uma execução e outra do programa, mesmo sem o uso de banco de dados.

A interação com o sistema é feita via terminal, por meio de menus que guiam o usuário entre as opções disponíveis. Além das funções básicas de cadastro, o sistema também cuida de relacionamentos entre entidades, como por exemplo: uma turma está ligada a um professor e a uma disciplina, e uma matrícula vincula um estudante a uma turma. Tudo isso com verificações para evitar inconsistências, como códigos repetidos ou relacionamentos com entidades que não existem.

Esse projeto teve como finalidade consolidar conhecimentos de lógica de programação, estrutura de dados, persistência de dados em arquivos e relacionamento entre entidades, preparando a base para sistemas mais complexos no futuro.
