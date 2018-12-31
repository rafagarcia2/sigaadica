from django.db import models


class Professor(models.Model):
    codigo = models.IntegerField('Código', unique=True)
    nome = models.CharField('Nome', max_length=100)
    vinculo = models.CharField('Vínculo', max_length=100)

    ativo = models.BooleanField('Ativo', default=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ('nome', 'codigo')


class Departamento(models.Model):
    codigo = models.IntegerField('codigo')
    nome = models.CharField('Nome', max_length=100)

    ativo = models.BooleanField('Ativo', default=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ('nome', 'codigo')


class Curso(models.Model):
    departamento = models.ForeignKey(Departamento, verbose_name='Departamento', on_delete=models.CASCADE)
    codigo = models.IntegerField('codigo')
    nome = models.CharField('Nome', max_length=100)

    ativo = models.BooleanField('Ativo', default=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ('nome', 'codigo')


class Disciplina(models.Model):
    id_componente = models.IntegerField('id_componente', unique=True)
    nome = models.CharField('Nome', max_length=200)
    codigo = models.CharField('codigo', max_length=200)
    departamento = models.CharField('Departamento', max_length=200)

    ativo = models.BooleanField('Ativo', default=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ('departamento', 'nome', 'id_componente',)


class Turma(models.Model):
    codigo = models.IntegerField('codigo', unique=True)
    disciplina = models.ForeignKey(Disciplina, to_field='id_componente', verbose_name='Disciplina', on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, to_field='codigo', verbose_name='Professor', on_delete=models.CASCADE)
    anoperiodo = models.CharField('Ano/Periodo', max_length=10)

    qnt_discentes = models.IntegerField('Quantidade de Discentes')
    qnt_aprovados = models.IntegerField('Quantidade de Aprovados')
    qnt_reprovacao = models.IntegerField('Quantidade de Reprovados')

    qnt_trancamentos = models.IntegerField('Quantidade de Trancamentos')
    qnt_aprovados_primeira = models.IntegerField('Quantidade de Aprovados na primeira vez que pagou')
    qnt_reposicao = models.IntegerField('Quantidade de Reposições')

    taxa_aprovacao = models.DecimalField('Taxa de Aprovação', decimal_places=2, max_digits=5)
    taxa_reprovacao = models.DecimalField('Taxa de Reprovação', decimal_places=2, max_digits=5)
    evasao = models.DecimalField('Quantidade de Trancamentos', decimal_places=2, max_digits=5)

    media_turma = models.DecimalField('Média da Turma', decimal_places=2, max_digits=5)
    media_faltas = models.DecimalField('Média da Faltas', decimal_places=2, max_digits=5)

    ativo = models.BooleanField('Ativo', default=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.codigo, self.disciplina)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ('disciplina', 'codigo',)


class Avaliacao(models.Model):
    codigo = models.IntegerField('codigo')
    turma = models.ForeignKey(Turma, verbose_name='Turma', on_delete=models.CASCADE)
    postura_profissional_media = models.DecimalField('Média da Postura Profissional', decimal_places=2, max_digits=5)
    postura_profissional_dp = models.DecimalField('Desvio Padrão da Postura Profissional do docente', decimal_places=2, max_digits=5)
    atuacao_profissional_media = models.DecimalField('Média da Atuacação Profissional do docente', decimal_places=2, max_digits=5)
    atuacao_profissional_dp = models.DecimalField('Desvio Padrão da Atuação Profissional do docente', decimal_places=2, max_digits=5)
    autoavaliacao_aluno_media = models.DecimalField('Média da Autoavaliação do Discente', decimal_places=2, max_digits=5)
    autoavaliacao_aluno_dp = models.DecimalField('Desvio Padrão da Autoavaliação do Discente', decimal_places=2, max_digits=5)

    ativo = models.BooleanField('Ativo', default=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.codigo, self.turma)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ('codigo', 'turma',)
