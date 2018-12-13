from django.db import models


class Professor(models.Model):
    codigo = models.IntegerField('Código')
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
    id_componente = models.IntegerField('id_componente')
    nome = models.CharField('Nome', max_length=100)
    departamento = models.CharField('Departamento', max_length=100)

    ativo = models.BooleanField('Ativo', default=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ('departamento', 'nome', 'id_componente',)


class Avaliacao(models.Model):
    codigo = models.IntegerField('codigo')
    turma = models.CharField('Turma', max_length=100)
    postura_profissional_media = models.DecimalField('Média da Postura Profissional', decimal_places=2, max_digits=5)
    postura_profissional_dp = models.DecimalField('Desvio Padrão da Postura Profissional do docente', decimal_places=2, max_digits=5)
    atuacao_profissional_media = models.DecimalField('Média da Atuacação Profissional do docente', decimal_places=2, max_digits=5)
    atuacao_profissional_dp = models.DecimalField('Desvio Padrão da Atuação Profissional do docente', decimal_places=2, max_digits=5)
    autoavaliacao_aluno_media = models.DecimalField('Média da Postura Profissional do docente', decimal_places=2, max_digits=5)
    autoavaliacao_aluno_dp = models.DecimalField('Desvio Padrão da Postura Profissional', decimal_places=2, max_digits=5)

    ativo = models.BooleanField('Ativo', default=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.codigo, self.turma)
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ('codigo', 'turma',)


class Turma(models.Model):
    codigo = models.IntegerField('codigo')
    disciplina = models.ForeignKey(Disciplina, verbose_name='Disciplina', on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, verbose_name='Professor', on_delete=models.CASCADE)
    qnt_discentes = models.IntegerField('Quantidade de Discentes')

    taxa_aprovacao = models.DecimalField('Taxa de Aprovação', decimal_places=2, max_digits=5)
    media_turma = models.DecimalField('Média da Turma', decimal_places=2, max_digits=5)
    qnt_aprovados_primeira = models.DecimalField('Quantidade de Aprovados na primeira vez que pagou', decimal_places=2, max_digits=5)
    evasao = models.DecimalField('Quantidade de Trancamentos', decimal_places=2, max_digits=5)
    autoavaliacao_aluno_media = models.DecimalField('Média da Postura Profissional do docente', decimal_places=2, max_digits=5)
    autoavaliacao_aluno_dp = models.DecimalField('Desvio Padrão da Postura Profissional', decimal_places=2, max_digits=5)

    ativo = models.BooleanField('Ativo', default=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.codigo, self.disciplina)
    
    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ('disciplina', 'codigo',)